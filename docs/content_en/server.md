# Report Server

The report server provides a web-based dashboard for viewing regression results across multiple users and projects.

After starting the server, the dashboard is accessible from a web browser.

## Features

- Aggregates regression results from configured work directories
- Displays pass/fail/error/skip counts with color coding
- Auto-refreshes periodically
- Supports filtering by user or status

## Configuration

User directories and server settings are configured via a JSON configuration file in the report server's `config/` folder.

## Starting the Server

```terminal
python3 serve.py
```

## Options

### --port / -p

TCP port to listen on. Default: `8765`.

### --host

Bind address. Default: `0.0.0.0`.

### --config / -c

Path to an alternate configuration file.

### --debug

Enable debug mode with hot-reload.
