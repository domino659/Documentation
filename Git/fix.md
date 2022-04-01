## [Sommaire](README.md)

# Fix

## Rebase
Use when branch main has advanced and impossible to merge

    git checkout -b <COPY MAIN> <MAIN>
    git add <FILE>
    git commit -m "<MSG COMMIT>"

    git checkout <MAIN>
    git add <FILE>
    git commit -m "<MSG COMMIT>"

    git log --oneline # Get last id commit

    git checkout <COPY MAIN>
    git rebase <ID COMMIT>

    git checkout <MAIN>
    git merge <COPY MAIN>
    git branch -d <COPY MAIN>

<br>

## Ammend
Combine the change staged in the ancient cmomit with the actual one
    
    git commit --amend
    
Can also allow you to change the commit message

    git commit --amend -m "an updated commit message"
    
If you just want to add a file that was forgotten

    git commit --amend --no-edit
 
<br>
   
## Go back to a precise commit
    git log --online # Get the commit id
    gti checkout <ID COMMIT>
    gut checkout -b <NEW-BRANCH>

<br>

## Get a precise file from a commit
    git checkout <ID COMMIT> <FILE NAME>
