# Preparation

- [Preparation](#preparation)
  - [-h/--help](#-h--help)
  - [-env\_setup](#-env_setup)
  - [-env\_unset](#-env_unset)
  - [-check\_testlist](#-check_testlist)

This document provides instructions for running a single simulation. Ensure the command is executed in the root folder of the cloned repository.

> The `run` command must be executed in the project's root folder.

## -h/--help

Displays a help message with descriptions of all options.

## -env_setup

Sets up the required environment variables based on your shell type.

Supported shells:

- bash/zsh
- tcsh/csh

## -env_unset

Unsets all environment variables related to `uve_tools`.

## -check_testlist

Checks the testlist before simulation or regression to identify errors early.

Example: `-check_testlist=./verif/test/ip/testlist_ip`
