import os
import subprocess
import sys

# Get the current directory
current_dir = os.getcwd()
git_path = "D:\\Program Files\\Git\\cmd\\git.exe"

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Use os.path.join to create the relative paths
repos_file = os.path.join(script_dir, 'repos.txt')

# Read the repos.txt file into a list
with open(repos_file, "r") as file:
    repos = [line.strip() for line in file]

# Check the command that was run
if len(sys.argv) > 1:
    command = sys.argv[1]
else:
    command = None

# Declare the dir_name variable
dir_name = current_dir

if command == 'init':
    # Check if the current directory already exists in the repos.txt file
    if current_dir in repos:
        # Print the git repo details
        print(subprocess.check_output([git_path, "status"]).decode())
    else:
        # Call the real git init
        subprocess.call([git_path, "init"])
        print("Done initializing the git repo.")
elif command == 'clone':
    # Get the repository URL from the command-line arguments
    if len(sys.argv) > 2:
        repo_url = sys.argv[2]
    else:
        print("Error: No repository URL provided.")
        sys.exit(1)

    # Call git clone with the repository URL
    subprocess.call([git_path, "clone", repo_url])
    print("Done cloning the repository.")

    # Change the dir_name to the cloned repository's directory
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    dir_name = os.path.join(current_dir, repo_name)
elif command == 'showall':
    # Print all the repositories in the repos.txt file and then end the script
    for repo in repos:
        dir_name, branch_name, _ = repo.split(' ')
        if os.path.exists(dir_name):
            os.chdir(dir_name)
            try:
                # Check if the directory is a git repository
                subprocess.check_output([git_path, "rev-parse", "--is-inside-work-tree"]).decode().strip()
                print("----- Git Repository Details for {} -----".format(dir_name))
                print("Branch: {}".format(branch_name))
                print("Status:")
                print(subprocess.check_output([git_path, "status"]).decode())
                print("Remote repository:")
                print(subprocess.check_output([git_path, "remote", "-v"]).decode())
                print("----------------------------------")
            except subprocess.CalledProcessError:
                print("Directory {} is not a git repository".format(dir_name))
    sys.exit(0)
elif command == 'delete':
    # Check if the current directory is a git repository
    try:
        subprocess.check_output([git_path, "rev-parse", "--is-inside-work-tree"]).decode().strip()
        dir_name = os.path.basename(current_dir)
        # Delete the entire directory
        subprocess.call(["rd", "/S", "/Q", current_dir], shell=True)
        print("Deleted the directory {}.".format(dir_name))
    except subprocess.CalledProcessError:
        print("Directory {} is not a git repository".format(current_dir))

    # Remove the current directory from the repos.txt file
    repos = [repo for repo in repos if not repo.startswith(current_dir)]
    with open(repos_file, "w") as file:
        for repo in repos:
            file.write(repo + '\n')
    print("Updated the repos.txt file.")
    sys.exit(0)
else:
    subprocess.call([git_path] + sys.argv[1:])
    sys.exit(0)

# Ask the user if they want the script to manage git push every half hour
manage_push = input("Do you want the script to manage git push every half hour? (y/n) ")

if manage_push.lower() == 'y':
    # Ask the user for the branch name
    branch_name = input("Please enter the branch name to which changes should be pushed: ")

    # Append the dir_name, branch name and a marker next to the repo name in the repos.txt file
    with open(repos_file, "a") as file:
        file.write(dir_name + " " + branch_name + " *\n")
    print("The script will now manage git push every half hour.")