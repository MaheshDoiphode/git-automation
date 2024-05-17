import os, subprocess, time, logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename=r"C:\Users\P1357911\Desktop\testingpython\git-automation\git-logs.log", level=logging.INFO)

def manage_git_push():
    git_path = "D:\\Program Files\\Git\\cmd\\git.exe"
    while True:
        logging.info("----- Starting new cycle at %s -----" % datetime.now())
        with open(r"C:\Users\P1357911\Desktop\testingpython\git-automation\repos.txt", "r") as file:
            repos = [line.strip() for line in file]

        # Create a new list to store the updated repos
        updated_repos = []

        for repo in repos:
            dir_name, branch_name, _ = repo.split(' ')

            # Check if the directory exists
            if os.path.exists(dir_name):
                os.chdir(dir_name)
                # Check if the directory is a git repository
                try:
                    subprocess.check_output([git_path, "rev-parse", "--is-inside-work-tree"]).decode().strip()
                except subprocess.CalledProcessError:
                    # The directory is not a git repository, so continue with the next repo
                    logging.warning("Directory %s is not a git repository" % dir_name)
                    continue

                logging.info("Processing repository %s" % dir_name)

                # If the repo is supposed to be managed by the script, perform git operations
                if repo.endswith('*'):
                    # Check if there are changes
                    status_output = subprocess.check_output([git_path, "status", "--porcelain"]).decode()
                    if status_output:
                        # There are changes, so add, commit, and push
                        logging.info("Changes detected in repository %s. Adding changes." % dir_name)
                        subprocess.call([git_path, "add", "."])
                        logging.info("Changes added. Committing changes.")
                        subprocess.call([git_path, "commit", "-m", "automated commit"])
                        logging.info("Changes committed. Pushing changes.")
                        subprocess.call([git_path, "push","origin", branch_name])
                        logging.info("Changes pushed for repository %s" % dir_name)

                # Add the repo to the updated list
                updated_repos.append(repo)

        # Write the updated list back to repos.txt
        logging.info("Updating repos.txt")
        with open(r"C:\Users\P1357911\Desktop\testingpython\git-automation\repos.txt", "w") as file:
            for repo in updated_repos:
                file.write(repo + '\n')
        logging.info("repos.txt updated")

        time.sleep(1800)

manage_git_push()