# Project Startup

`uve_startup` is a project scaffolding tool that generates a new UVE project directory structure with all required folders, configuration files, and entry points pre-configured.

## What it creates

- Standard project directory layout (`bin`, `config`, `design`, `verif`, `doc`, `work`)
- Default configuration files
- `run` and `run_cocotb` entry point symlinks
- `.gitignore` and related project files

## Key Options

### project_name

The name of the project to create (required).

### -o / --output-dir

Specify the output directory. Default: current directory.

### --submodule-add

Add submodules defined in `.gitmodules` after project creation.

### -r / --remote

Set the git remote origin URL for the newly created project.

## Example

```terminal
python3 uve_startup project_name -o /path/to/projects
```
