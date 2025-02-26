# Task-Tracker
Task Tracker(任务跟踪器，新手版项目)
任务追踪器
Task tracker 是一个用于跟踪和管理您的任务的项目。在此任务中，您将构建一个简单的命令行界面 （CLI） 来跟踪您需要执行的作、已完成的作以及您当前正在处理的内容。该项目将帮助您练习编程技能，包括使用文件系统、处理用户输入和构建简单的 CLI 应用程序。

# Requirements  要求
The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:
应用程序应从命令行运行，接受用户作和输入作为参数，并将任务存储在 JSON 文件中。用户应该能够：

Add, Update, and Delete tasks
添加、更新和删除任务
Mark a task as in progress or done
将任务标记为 in progress 或 done
List all tasks  列出所有任务
List all tasks that are done
列出已完成的所有任务
List all tasks that are not done
列出所有未完成的任务
List all tasks that are in progress
列出所有正在进行的任务
Here are some constraints to guide the implementation:
以下是指导实施的一些约束：

You can use any programming language to build this project.
您可以使用任何编程语言来构建此项目。
Use positional arguments in command line to accept user inputs.
在命令行中使用位置参数来接受用户输入。
Use a JSON file to store the tasks in the current directory.
使用 JSON 文件将任务存储在当前目录中。
The JSON file should be created if it does not exist.
如果 JSON 文件不存在，则应创建 JSON 文件。
Use the native file system module of your programming language to interact with the JSON file.
使用编程语言的本机文件系统模块与 JSON 文件进行交互。
Do not use any external libraries or frameworks to build this project.
请勿使用任何外部库或框架来构建此项目。
Ensure to handle errors and edge cases gracefully.
确保妥善处理错误和边缘情况。

# Example  例
The list of commands and their usage is given below:
命令列表及其用法如下：

##Adding a new task
task-cli add "Buy groceries"
##Output: Task added successfully (ID: 1)

##Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

##Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

##Listing all tasks
task-cli list

##Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress

# Task Properties  任务属性
Each task should have the following properties:
每个任务应具有以下属性：

id: A unique identifier for the task
id：任务的唯一标识符
description: A short description of the task
description：任务的简短描述
status: The status of the task (todo, in-progress, done)
status：任务的状态（todo、in-progress、done）
createdAt: The date and time when the task was created
createdAt：创建任务的日期和时间
updatedAt: The date and time when the task was last updated
updatedAt：上次更新任务的日期和时间
Make sure to add these properties to the JSON file when adding a new task and update them when updating a task.
确保在添加新任务时将这些属性添加到 JSON 文件中，并在更新任务时更新这些属性。

# 项目开发环境
解释器Python3.12

# 项目测试
