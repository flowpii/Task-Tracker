import argparse
import json
import os
from datetime import datetime


# 文件操作函数
def read_tasks():
    """读取任务列表"""
    if not os.path.exists('../tasks.json'):
        return []
    try:
        with open('../tasks.json', 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Warning: Invalid JSON file, initializing new task list")
        return []


def save_tasks(tasks):
    """保存任务列表"""
    with open('../tasks.json', 'w') as f:
        json.dump(tasks, f, indent=2)


# 辅助函数
def find_task(tasks, task_id):
    """根据ID查找任务"""
    return next((t for t in tasks if t['id'] == task_id), None)


def validate_task_id(func):
    """ID验证装饰器"""

    def wrapper(args):
        tasks = read_tasks()
        if not find_task(tasks, args.id):
            print(f"Error: Task {args.id} not found")
            return
        return func(args)

    return wrapper


# 命令处理函数
def add_task(args):
    """添加新任务"""
    tasks = read_tasks()
    new_id = max([t['id'] for t in tasks], default=0) + 1

    task = {
        "id": new_id,
        "description": args.description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")


@validate_task_id
def update_task(args):
    """更新任务描述"""
    tasks = read_tasks()
    task = find_task(tasks, args.id)

    task['description'] = args.new_description
    task['updatedAt'] = datetime.now().isoformat()

    save_tasks(tasks)
    print(f"Task {args.id} updated")


@validate_task_id
def delete_task(args):
    """删除任务"""
    tasks = read_tasks()
    tasks = [t for t in tasks if t['id'] != args.id]

    save_tasks(tasks)
    print(f"Task {args.id} deleted")


@validate_task_id
def mark_status(args):
    """标记任务状态"""
    tasks = read_tasks()
    task = find_task(tasks, args.id)

    task['status'] = args.status
    task['updatedAt'] = datetime.now().isoformat()

    save_tasks(tasks)
    print(f"Task {args.id} marked as {args.status}")


def list_tasks(args):
    """列出任务"""
    tasks = read_tasks()
    status_filter = args.status.lower() if args.status else None

    if status_filter:
        tasks = [t for t in tasks if t['status'] == status_filter]

    if not tasks:
        print("No tasks found")
        return

    for task in tasks:
        status = task['status'].upper().ljust(12)
        print(f"#{task['id']} [{status}] {task['description']}")
        print(f"  Created:  {task['createdAt']}")
        print(f"  Updated:  {task['updatedAt']}\n")


def main():
    # 主解析器
    parser = argparse.ArgumentParser(
        description='Task Tracker CLI',
        prog='task-cli'
    )
    subparsers = parser.add_subparsers(
        title='commands',
        dest='command',
        required=True
    )

    # Add 命令
    add_parser = subparsers.add_parser('add', help='Add new task')
    add_parser.add_argument('description', type=str, help='Task description')
    add_parser.set_defaults(func=add_task)

    # Update 命令
    update_parser = subparsers.add_parser('update', help='Update task description')
    update_parser.add_argument('id', type=int, help='Task ID')
    update_parser.add_argument('new_description', type=str, help='New description')
    update_parser.set_defaults(func=update_task)

    # Delete 命令
    delete_parser = subparsers.add_parser('delete', help='Delete task')
    delete_parser.add_argument('id', type=int, help='Task ID')
    delete_parser.set_defaults(func=delete_task)

    # Mark 状态命令
    for status in ['done', 'in-progress', 'todo']:
        parser_mark = subparsers.add_parser(
            f'mark-{status}',
            help=f'Mark task as {status}'
        )
        parser_mark.add_argument('id', type=int, help='Task ID')
        parser_mark.set_defaults(func=mark_status, status=status)

    # List 命令
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument(
        'status',
        nargs='?',
        choices=['all', 'done', 'todo', 'in-progress'],
        help='Filter by status'
    )
    list_parser.set_defaults(func=list_tasks)

    # 解析参数
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()