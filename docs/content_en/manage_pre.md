# Debug

## -debug

Enable debug mode to print additional debug information.

## -check_testlist

Checks the testlist before simulation or regression to identify errors early.

Example: `-check_testlist=./verif/test/ip/testlist_ip`

## -clean

Clean the root folder with interactive actions.

## -git_update

Update the repository and submodules.

## -check_git_clean

Check all the folders in the repo, analyze folders/files within specified level layer.
check_git_clean_check will be created to store the information for reviewing. This will be git ignored and need to be deleted manually.

review information:

- newly added folder
- should not contain in xxx
