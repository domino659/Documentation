## Push
  git status # Statut file
  git add <FILE/*>
  git commit -m "<MSG COMMIT>"
  git push

## Branch
  git branch # List branche
  git branch <NAME> # Create branche
  git branch -d <NAME> # Delete branche
  git checkout <NAME> # Move to branche
  git checkout -b <NAME> # Move to branche and create it if needed
  git fetch <remote> # Pull all branch from git

## Merge
  git checkout -b <DEV-BRANCH> <MAIN> 
  git add <FILE>
  git commit -m "<MSG COMMIT>"
  git checkout <MAIN>
  git merge <DEV-BRANCH>

## Stash
  git stash # Store last change in memory
  git stash list # List of stash and id
  git stash apply # Apply last stash
  git stash apply stash@{<ID>} # Apply stash by ID
