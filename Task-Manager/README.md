# Task Manager

## Overview
This is a simple command-line task manager written in Python. It allows users to add, update, delete, and list tasks, as well as mark them with different statuses.

## Features
- Add a task with a description.
- Update an existing task.
- Delete a task.
- Mark tasks as "done," "not done," or "in progress."
- List tasks based on their status.

## Requirements
- Python 3.x

## Installation
1. Clone this repository or download the script.
2. Ensure Python is installed on your system.

## Usage
Run the script from the command line with the following commands:

### Add a task:
```sh
python task_manager.py add "Task description"
```

### Update a task:
```sh
python task_manager.py update <task_id> "Updated description"
```

### Delete a task:
```sh
python task_manager.py delete <task_id>
```

### Mark a task as done:
```sh
python task_manager.py mark <task_id> done
```

### Mark a task as in progress:
```sh
python task_manager.py mark <task_id> in progress
```

### List all tasks:
```sh
python task_manager.py list
```

### List tasks based on status:
```sh
python task_manager.py list-done
python task_manager.py list-not-done
python task_manager.py list-in-progress
```

## File Structure
- `task.json` : Stores all tasks persistently.
- `task_manager.py` : The main script handling task management.

## Notes
- If `task.json` does not exist, it will be created automatically.
- Ensure you provide the correct task ID when updating or deleting a task.

## License
This project is open-source and free to use.https://roadmap.sh/projects/task-tracker

