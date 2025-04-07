# Process Management

## -show_z

Show all the zombie processes belonging to the current user.

- **Default**: `False`
- **Usage**: Use this option to list all zombie processes for the current user.

## -kill_z

Kill all the zombie processes belonging to the current user.

- **Default**: `False`
- **Usage**: Use this option to terminate all zombie processes for the current user.

## -show_grep

Show processes matching a specific pattern using `grep`.

- **Type**: `string`
- **Default**: Empty string
- **Usage**: Specify a pattern to filter processes. Example: `-show_grep=xxx`.

## -kill_grep

Kill processes matching a specific pattern using `grep`.

- **Type**: `string`
- **Default**: Empty string
- **Usage**: Specify a pattern to terminate processes. Example: `-kill_grep=xxx`.