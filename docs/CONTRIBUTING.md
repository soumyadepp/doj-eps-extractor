# Contributing Guide

## Getting Started

### Development Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/scrape-doj.git
cd scrape-doj
```

2. Install with development dependencies:

```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -e ".[dev]"
```

3. Verify installation:

```bash
python3 -m epstein.cli --help
```

## Project Structure

```
scrape-doj/
├── epstein/                 # Main package
│   ├── __init__.py         # Package initialization
│   ├── client.py           # DOJMultimediaSearchClient class
│   └── cli.py              # CLI interface
├── docs/                    # Documentation
│   ├── OVERVIEW.md         # Project overview
│   ├── INSTALLATION.md     # Setup guide
│   ├── USAGE.md            # Usage examples
│   ├── API.md              # API documentation
│   ├── FAQ.md              # Frequently asked questions
│   └── CONTRIBUTING.md     # This file
├── main.py                  # Legacy entry point
├── README.md                # Main readme
├── pyproject.toml           # Project configuration
├── requirements.txt         # Dependencies
├── .gitignore              # Git ignore rules
└── lib_data/               # Output data folder (not tracked)
```

## Making Changes

### Code Style

- Follow PEP 8 conventions
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep lines under 100 characters

### Adding a New Feature

1. Create a new branch:

```bash
git checkout -b feature/my-feature
```

2. Make your changes
3. Test thoroughly
4. Commit with clear messages
5. Push and create a Pull Request

### Modifying the Client

The main API client is in `epstein/client.py`:

```python
class DOJMultimediaSearchClient:
    def __init__(self, base_url="..."):
        # Initialization

    def search(self, query="", page=0):
        # Single page search

    def search_all(self, query="", max_results=None, ...):
        # Paginated search

    def save_results(self, documents, prefix="..."):
        # Save to files
```

If adding methods, ensure they:

- Have clear docstrings
- Return documented types
- Handle errors gracefully
- Don't break existing API

### Modifying the CLI

The CLI interface is in `epstein/cli.py`:

```python
def main():
    # Parse arguments
    parser = argparse.ArgumentParser(...)

    # Use client to fetch data
    client = DOJMultimediaSearchClient(...)

    # Display results
    # Print formatted output
```

When adding CLI options:

- Use clear flag names
- Add help text
- Update [USAGE.md](USAGE.md)
- Test with `python3 -m epstein.cli --help`

## Testing

### Manual Testing

```bash
# Basic functionality
python3 -m epstein.cli --search "test" --limit 2 --no-save

# With file output
python3 -m epstein.cli --search "test" --limit 5

# Check output
ls -la lib_data/
cat lib_data/epstein_library_*.json | head -20
```

### Python API Testing

```python
from epstein import DOJMultimediaSearchClient

client = DOJMultimediaSearchClient()

# Test single page
docs, has_next = client.search(query="test", page=0)
assert len(docs) > 0, "No documents found"
assert has_next == True, "Should have more pages"

# Test search_all
all_docs = client.search_all(query="test", max_results=20)
assert len(all_docs) >= 10, "Should fetch at least one page"

# Test save_results
json_file, csv_file, txt_file = client.save_results(all_docs)
assert json_file.startswith("lib_data/"), "Should save to lib_data/"
```

## Documentation

When adding features, update relevant documentation:

- **New CLI option?** → Update [USAGE.md](USAGE.md)
- **New method?** → Update [API.md](API.md)
- **New behavior?** → Update [OVERVIEW.md](OVERVIEW.md)
- **Common issue?** → Add to [FAQ.md](FAQ.md)

Documentation uses Markdown. Keep it:

- Clear and concise
- Well-formatted with headers
- Includes code examples
- Links to related docs

## Dependencies

Current dependencies in `pyproject.toml`:

- `requests>=2.32.5` - HTTP requests
- `beautifulsoup4>=4.12.0` - HTML/XML parsing

Before adding new dependencies:

1. Check if you can use existing ones
2. Justify the addition
3. Update `pyproject.toml`
4. Update `requirements.txt`
5. Document in README

## Commits & Pull Requests

### Commit Messages

Use clear, descriptive messages:

```
Good:
- "Add support for custom base URLs"
- "Fix URL encoding for spaces"
- "Update documentation for API"

Avoid:
- "fix stuff"
- "update"
- "asdf"
```

### Pull Request Process

1. Update documentation
2. Include clear description of changes
3. Reference any related issues
4. Be responsive to feedback
5. Keep commits clean and squashed

## Reporting Issues

Found a bug? Create an issue with:

1. **Description** - What happened?
2. **Steps to reproduce** - How to trigger it?
3. **Expected behavior** - What should happen?
4. **Actual behavior** - What actually happened?
5. **Environment**:
   - Python version: `python3 --version`
   - OS: macOS/Linux/Windows
   - Installation method: pip/uv/source
6. **Logs or output** - Copy error messages

## Feature Requests

Have an idea? Open an issue with:

1. **Description** - What feature do you want?
2. **Use case** - Why do you need it?
3. **Example usage** - How would users use it?
4. **Alternatives** - Any workarounds?

## Release Process

Maintainers only:

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md` (if exists)
3. Create git tag: `git tag v0.2.0`
4. Push changes and tags
5. Build distribution: `python3 -m build`
6. Upload to PyPI: `python3 -m twine upload dist/*`

## Questions?

- Check the [FAQ.md](FAQ.md)
- Review [API.md](API.md)
- Look at existing code for patterns

Thanks for contributing! 🎉
