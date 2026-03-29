# Repository Symlink Management

repo_link enables linking project directories across multiple repositories. This is useful for team setups where design files, verification environments, configurations, and documentation live in separate git repositories but need to be accessible under a unified project structure. It supports both creating and cleaning up these links.

## Use Cases

- Share a common verification IP or design block across multiple projects without duplicating files
- Link a standalone configuration repository into a project's config directory
- Connect separate design and verification repositories into a single simulation workspace
- Clean up symlinks when a linked repository is no longer needed

## Supported Operations

### Create Links
Creates symlinks from a source repository directory into a target project directory, covering design, verification, config, and doc subdirectories.

### Clean Up Links
Removes symlinks from the target directory that point back into the source repository, leaving non-symlinked files untouched.
