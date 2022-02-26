#!/bin/bash

# to use the script:
# chmod +x commit.sh
# ./commit.sh "file name or folder" "message to this commit"
# A simple bash script to commit to repo

echo "${1}" "${2}"

# git-add - command to add any new or modified files to the index
echo "Add changes in files or directory..."
git add "${1}"

# The git commit command will save all staged changes, 
# along with a brief description from the user, 
# in a “commit” to the local repository.
echo "committing..."
git commit -m "${2}"

# pull the last version of the repo
echo "pull: repository"
git pull origin master

# The git push command is used to upload local repository 
# content to a remote repository. Pushing is how you transfer 
# commits from your local repository to a remote repo. 
echo "and push to remote repository right now!"
git push origin master

echo "All done!"
