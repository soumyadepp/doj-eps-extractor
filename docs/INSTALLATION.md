# Installation Guide

## Prerequisites

- Python 3.9 or higher
- pip or uv package manager

## Installation Methods

### Option 1: Using pip (Recommended)

```bash
pip install doj-multimedia-search
```

Then use the `epstein` command directly:

```bash
epstein --search "query"
```

### Option 2: Using uv (Development)

If you have the source code and want to use `uv`:

```bash
git clone <repository-url>
cd scrape-doj
uv sync
```

Then run:

```bash
python3 -m epstein.cli --search "query"
# or
python3 main.py --search "query"
```

### Option 3: Install from Source with pip

```bash
git clone <repository-url>
cd scrape-doj
pip install -e .
```

## Verify Installation

```bash
# Show the ASCII art banner
epstein

# Or check the help
epstein --help
```

## Troubleshooting

### Command not found: epstein

If you get "command not found", make sure:

1. Python 3.9+ is installed: `python3 --version`
2. The package is installed in your Python environment
3. Your Python bin directory is in PATH

Try running with full path:

```bash
python3 -m epstein.cli --search "query"
```

### SSL Certificate Errors

If you get SSL certificate errors, try:

```bash
python3 -m pip install --upgrade certifi
```

### Connection Timeout

If requests time out, the DOJ servers may be temporarily unavailable or your internet connection is slow. The CLI will retry after a delay. You can adjust the delay:

```bash
epstein --search "query" --delay 1.0  # 1 second delay between requests
```

## Next Steps

- See [USAGE.md](USAGE.md) for command examples
- Check [API.md](API.md) for Python API documentation
- Review [FAQ.md](FAQ.md) for common questions
