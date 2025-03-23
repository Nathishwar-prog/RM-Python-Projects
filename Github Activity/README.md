# GitHub Activity CLI

## Overview
GitHub Activity CLI is a simple command-line tool that fetches and displays a GitHub user's recent activity. It utilizes the GitHub API to retrieve public events associated with a given username and presents them in a human-readable format.

## Features
- Fetches the most recent GitHub activity for a specified user.
- Displays up to 5 recent events in a user-friendly format.
- Handles errors such as invalid usernames or API failures gracefully.
- Uses only built-in Python libraries (no external dependencies).

## Prerequisites
- Python 3.x installed on your system.
- An active internet connection.

## Installation
No installation is required. Just clone or download the script and run it using Python.

## Usage
Run the following command in your terminal:
```sh
python github_activity_cli.py <github_username>
```
Example:
```sh
python github_activity_cli.py Nathishwar-prog
```

### Sample Output:
```
Recent activity of 'Nathishwar-prog':
 Pushed commits to Nathishwar-prog/RM-Python-Projects
- Pushed commits to Nathishwar-prog/RM-Python-Projects
- Pushed commits to Nathishwar-prog/RM-Python-Projects
- Pushed commits to Nathishwar-prog/RM-Python-Projects
- Pushed commits to Nathishwar-prog/RM-Python-Projects

```

## How It Works
1. The script takes a GitHub username as an argument.
2. It makes an API request to `https://api.github.com/users/<username>/events`.
3. It parses the JSON response and extracts the most relevant details.
4. It prints a formatted list of the user’s recent activity.
5. Handles errors like:
   - Invalid usernames (404 errors)
   - Network failures
   - Users with no recent activity

## Error Handling
- If the username does not exist, the script displays: `Error: User not found.`
- If there is no internet connection, the script displays: `Error: Failed to fetch data. Check your internet connection.`
- If no recent activity is found, the script informs the user.

## Supported Event Types
The CLI supports and translates the following GitHub events:
- `PushEvent` → **"Pushed commits to"**
- `PullRequestEvent` → **"Opened a pull request in"**
- `IssuesEvent` → **"Opened a new issue in"**
- `ForkEvent` → **"Forked"**
- `WatchEvent` → **"Starred"**

## License
This project is open-source and available under the MIT License.

## Author
Developed by Nathishwar ->  https://github.com/Nathishwar-prog

