## [Sommaire](README.md)

# Commande Basic

## Push
```
    git status
    git add <FILE/*>
    git commit -m "<MSG COMMIT>"
    git push
```

<br>

## Pull
Get up to date with remote branche

    git pull <REMOTE>

<br>

## Branch
 
List branche

    git branch
 
Create branche

    git branch <NAME>

Delete branche

    git branch -d <NAME>
 
Move to branche

    git checkout <NAME>

Move to branche and create it if needed

    git checkout -b <NAME>
 
Pull all branch from git

    git fetch <remote>

<br>

## Merge

    git checkout -b <DEV-BRANCH> <MAIN> 
    git add <FILE>
    git commit -m "<MSG COMMIT>"
    git checkout <MAIN>
    git merge <DEV-BRANCH>

<br>

## Stash

Store last change in memory

    git stash

List of stash and id

    git stash list

Apply last stash

    git stash apply

Apply stash by ID

    git stash apply stash@{<ID>}