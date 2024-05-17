# Git Automation Project

This project provides a set of Python scripts to automate and manage Git repositories on your local machine. It extends the functionality of standard Git commands and adds new commands for managing multiple repositories.

## Prerequisites

Before you start using this project, make sure you have Git installed on your machine. You can download Git from [here](https://git-scm.com/downloads).

## Setting Up

1. Clone this repository to your local machine.
2. Open the `git.py` and `git-push.py` files in a text editor.
3. In both files, replace the `git_path` variable with the path to your Git executable. The path should look something like this: `C:\\Program Files\\Git\\cmd\\git.exe`.

## Usage

This project provides the following commands:

- `init`: Initializes a new Git repository in the current directory.
- `clone <repo_url>`: Clones a Git repository from the provided URL.
- `showall`: Shows details of all the repositories listed in the `repos.txt` file.
- `delete`: Deletes the Git repository in the current directory.

To run a command, open a terminal in the directory containing the `git.py` script and type `python git.py <command>`. Replace `<command>` with one of the commands listed above.

When you initialize or clone a repository, the script will ask if you want it to manage Git pushes for that repository. If you agree, the script will automatically add, commit, and push changes to the specified branch every half hour.

To enable this feature, you need to run the `git-push.py` script in the background. You can do this by opening a terminal in the directory containing the `git-push.py` script and typing `python git-push.py &`.

## Logs

The `git-push.py` script logs all its activities to the `git-logs.log` file. This includes information messages about the start of a new cycle, warnings about directories that are not Git repositories, and information about updates to the `repos.txt` file.
## Contributing

Contributions are welcome! Please feel free to submit a pull request.



```
This project is a set of Python scripts designed to automate and manage Git repositories on your local machine. It extends the functionality of standard Git commands and adds new commands for managing multiple repositories.

The main script, `git.py`, provides commands for initializing a new Git repository, cloning an existing repository, showing details of all managed repositories, and deleting a repository. It also offers an option to manage Git pushes for a repository, which means it will automatically add, commit, and push changes to the specified branch every half hour.

The `git-push.py` script is responsible for managing Git pushes. It runs in an infinite loop, checking every half hour if there are changes in the repositories that are marked to be managed. If it detects changes, it adds, commits, and pushes them to the specified branch. All its activities are logged to the `git-logs.log` file.

The `repos.txt` file is a list of all repositories that are managed by the scripts. Each line in the file represents a repository and contains the directory of the repository, the branch to which changes should be pushed, and a marker indicating if the repository is managed by the `git-push.py` script.

The problem that this project solves is the manual management of Git repositories. It can be time-consuming and error-prone to manually add, commit, and push changes to multiple repositories. This project automates these tasks, saving time and reducing the chance of errors.

The project was improved by adding the ability to manage Git pushes. This feature was implemented in the `git-push.py` script, which runs in the background and automatically pushes changes every half hour. This eliminates the need to manually push changes, making the management of Git repositories even more effortless.

The project also includes a logging feature, which logs all activities of the `git-push.py` script to the `git-logs.log` file. This allows you to easily track what the script is doing and troubleshoot any issues that may arise.

In conclusion, this project provides a set of tools that automate and simplify the management of Git repositories. It saves time, reduces the chance of errors, and provides a log of all activities for easy troubleshooting.
```