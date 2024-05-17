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
