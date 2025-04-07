# Preparation

## -h/--help

Displays a help message with descriptions of all options.

## -env_setup

Sets up the required environment variables based on your shell type.

Supported shells:

- bash/zsh
- tcsh/csh

## -env_unset

Unsets all environment variables related to `uve_tools`.

## -json

The json/json_extra files are located: `config/json/project/`

Specifies the configuration for a project using a JSON file. This file manages options for EDA and all processes of simulation or emulation. The default file is `uve.json`.

To use a specific JSON file for simulation, pass it as an argument:

Example: `-json=xxx.json`

## -json_extra

Specifies additional configuration for a project using an extra JSON file. This file includes sections for compilation, elaboration, and execution. The default file is `uve_extra.json`.

To use a specific extra JSON file for simulation, pass it as an argument:

Example: `-json_extra=xxx_extra.json`
