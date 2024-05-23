## Git Commands

# Create a New Branch
git branch feature-xyz

# Switch to the New Branch
git checkout feature-xyz

# confirm you're on the new branch by running:
git branch

# Push the Branch to Remote Repository (if needed)
If you want to push the new branch to a remote repository, use the git push command followed by the remote name (usually origin) and the branch name:
git push origin feature-xyz

# Summary of Commands
cd path/to/your/repository          # Navigate to your repository
git branch feature-xyz              # Create a new branch (alternative to next step)
git checkout -b feature-xyz         # Create and switch to a new branch in one step
git checkout feature-xyz            # Switch to the new branch (if created using git branch)
git push origin feature-xyz         # Push the new branch to the remote repository

# To merge changes from a feature branch into the main branch (often called master or main), you can use Git's merge functionality. Here's how to do it:
Ensure Your Working Directory is Clean
Before merging, ensure your working directory is clean by committing or stashing any changes you have. You can check the status using:

git status


# Checkout the Main Branch
First, you need to switch to the main branch. If your main branch is called master, you can use:

git checkout master/main

# Merge the Feature Branch into Main
Once you're on the main branch, you can merge the changes from your feature branch. Use the following command:

git merge feature-branch


# Resolve Any Merge Conflicts
If there are any merge conflicts, Git will notify you. You'll need to resolve these conflicts manually. Git will mark the conflicted areas in your files. Once you've resolved the conflicts, you need to add the files and commit the changes:

git add .
git commit              # Write a commit message describing the merge.


# Push the Changes to the Remote Repository
Finally, after merging, push the changes to the remote repository:

git push origin master/main


# Optional: Delete the Feature Branch
If you no longer need the feature branch, you can delete it:

git branch -d feature-branch
