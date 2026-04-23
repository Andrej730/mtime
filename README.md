# mtime

Measure time - a simple command timing utility.

## Usage

```bash
mtime python -c "from time import sleep; sleep(5)"
# real 5.044s
```

## Installation

```bash
# With pip
pip install git+https://github.com/Andrej730/mtime.git

# Or with uv
uv tool install git+https://github.com/Andrej730/mtime.git
```

Then use it as a command:

```bash
mtime <command>
```

## Note

This tool is mainly useful on Windows where the Unix `time` command is not available. On macOS and Linux, you can use the built-in `time` command instead.
