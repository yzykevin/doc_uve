# Preparation Guide before using

- [Preparation Guide before using](#preparation-guide-before-using)
  - [General Options](#general-options)
    - [Supported Shells for `-env_setup`](#supported-shells-for--env_setup)
  - [Notes](#notes)

This document provides instructions and options for running a single simulation. Ensure that the run is executed in the root folder of the cloned repository.

## General Options

Below is a list of available command-line options for the simulation:

| Option         | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `-h/--help`    | Show help message and descriptions of the options.                         |
| `-env_setup`   | Automatically set up the required environment variables based on your shell type. |
| `-env_unset`   | Unset all environment variables related to `uve_tools`.                    |

### Supported Shells for `-env_setup`

- `bash/zsh`
- `tcsh/csh`

## Notes

- Ensure that your shell is supported before using the `-env_setup` option.
- Use `-env_unset` to clean up the environment variables after completing your tasks.
