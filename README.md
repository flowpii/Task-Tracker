# Task-Tracker
Task Tracker(任务跟踪器，新手版项目)


Programming Language  程序设计语言
CLI  命令行界面
Filesystem  文件系统
beginner  初学者
Task Tracker   任务跟踪器
Build a CLI app to track your tasks and manage your to-do list.
构建 CLI 应用程序来跟踪您的任务并管理您的待办事项列表。

Started working 
  开始工作
9m ago
. Follow 
  .跟随
these tips  这些提示
 to get most out of it.
  以充分利用它。

Stop Working  停止工作
Started Working  开始工作

Submit Solution  提交解决方案
5 upvotes  5 个赞成票
10 upvotes  10 个赞成
Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on. This project will help you practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.
Task tracker 是一个用于跟踪和管理您的任务的项目。在此任务中，您将构建一个简单的命令行界面 （CLI） 来跟踪您需要执行的作、已完成的作以及您当前正在处理的内容。该项目将帮助您练习编程技能，包括使用文件系统、处理用户输入和构建简单的 CLI 应用程序。

Requirements  要求
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
Example  例
The list of commands and their usage is given below:
命令列表及其用法如下：

# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
Task Properties  任务属性
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

Getting Started  开始
Here are a few steps to help you get started with the Task Tracker CLI project:
以下是帮助您开始使用 Task Tracker CLI 项目的几个步骤：

Set Up Your Development Environment
设置您的开发环境
Choose a programming language you are comfortable with (e.g., Python, JavaScript, etc.).
选择您熟悉的编程语言（例如 Python、JavaScript 等）。
Ensure you have a code editor or IDE installed (e.g., VSCode, PyCharm).
确保您已安装代码编辑器或 IDE（例如 VSCode、PyCharm）。
Project Initialization  项目初始化
Create a new project directory for your Task Tracker CLI.
为您的 Task Tracker CLI 创建一个新的项目目录。
Initialize a version control system (e.g., Git) to manage your project.
初始化版本控制系统（例如 Git）以管理您的项目。
Implementing Features  实现功能
Start by creating a basic CLI structure to handle user inputs.
首先创建一个基本的 CLI 结构来处理用户输入。
Implement each feature one by one, ensuring to test thoroughly before moving to the next e.g. implement adding task functionality first, listing next, then updating, marking as in progress, etc.
逐个实现每个功能，确保在进入下一个功能之前进行彻底测试，例如，首先实现添加任务功能，列出下一个，然后更新，标记为正在进行等。
Testing and Debugging  测试和调试
Test each feature individually to ensure they work as expected. Look at the JSON file to verify that the tasks are being stored correctly.
单独测试每个功能，以确保它们按预期工作。查看 JSON 文件以验证任务是否正确存储。
Debug any issues that arise during development.
调试开发过程中出现的任何问题。
Finalizing the Project  完成项目
Ensure all features are implemented and tested.
确保所有功能都已实施和测试。
Clean up your code and add comments where necessary.
清理代码并在必要时添加注释。
Write a good readme file on how to use your Task Tracker CLI.
编写一份关于如何使用 Task Tracker CLI 的优秀自述文件。
By the end of this project, you will have developed a practical tool that can help you or others manage tasks efficiently. This project lays a solid foundation for more advanced programming projects and real-world applications.
在本项目结束时，您将开发出一个实用的工具，可以帮助您或其他人有效地管理任务。该项目为更高级的编程项目和实际应用奠定了坚实的基础。
