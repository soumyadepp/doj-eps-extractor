# Documentation Index

Welcome to the Epstein DOJ Multimedia Search CLI documentation.

## Quick Links

### New Users

Start here if you're new to this tool:

1. **[OVERVIEW.md](OVERVIEW.md)** - Learn why this tool was created and what problems it solves
2. **[INSTALLATION.md](INSTALLATION.md)** - Get the tool installed and running
3. **[USAGE.md](USAGE.md)** - See practical examples and command reference

### Experienced Users

For developers and advanced usage:

1. **[API.md](API.md)** - Use the tool as a Python library in your projects
2. **[FAQ.md](FAQ.md)** - Common questions and troubleshooting
3. **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute to the project
4. **[CHANGELOG.md](CHANGELOG.md)** - What's new and what's planned

---

## Documentation Overview

### [OVERVIEW.md](OVERVIEW.md)

**The "Why" Document**

- Explains the purpose of this CLI tool
- Describes problems it solves
- Lists key features
- Suitable for: Decision makers, new users, researchers

### [INSTALLATION.md](INSTALLATION.md)

**Getting Started**

- Installation methods (pip, uv, source)
- Verification steps
- Troubleshooting common issues
- Suitable for: First-time installers

### [USAGE.md](USAGE.md)

**How to Use**

- Command syntax and options
- Practical examples for common tasks
- Output format documentation
- Tips, tricks, and performance notes
- Suitable for: Command-line users

### [API.md](API.md)

**Python Library Reference**

- Complete API documentation
- Import and usage examples
- Advanced examples (filtering, batch processing, etc.)
- Error handling and troubleshooting
- Suitable for: Python developers

### [FAQ.md](FAQ.md)

**Questions & Answers**

- General questions
- Technical troubleshooting
- Data and search questions
- Output and file handling
- Performance and limitations
- Suitable for: Users with specific problems

### [CONTRIBUTING.md](CONTRIBUTING.md)

**Developer Guide**

- Development setup
- Code style and conventions
- Making changes and testing
- Documentation updates
- Commit and PR process
- Suitable for: Contributors and maintainers

### [CHANGELOG.md](CHANGELOG.md)

**Version History**

- What's new in each version
- Future roadmap
- Technical details
- Suitable for: Understanding changes and planned features

---

## Common Tasks

### "How do I install this?"

→ See [INSTALLATION.md](INSTALLATION.md)

### "How do I search for documents?"

→ See [USAGE.md](USAGE.md) - Quick Start section

### "Can I use this in my Python project?"

→ See [API.md](API.md)

### "I have a question..."

→ Check [FAQ.md](FAQ.md) first

### "I found a bug / have a feature idea"

→ See [CONTRIBUTING.md](CONTRIBUTING.md) - Reporting section

### "What's new in the latest version?"

→ See [CHANGELOG.md](CHANGELOG.md)

---

## Document Types

Each documentation file has a specific purpose:

| File            | Type       | For Whom                   | Length       |
| --------------- | ---------- | -------------------------- | ------------ |
| OVERVIEW.md     | Conceptual | New users, decision makers | ~3 min read  |
| INSTALLATION.md | How-to     | Installers                 | ~5 min read  |
| USAGE.md        | Reference  | CLI users                  | ~10 min read |
| API.md          | Technical  | Python developers          | ~15 min read |
| FAQ.md          | Reference  | Users with questions       | ~10 min read |
| CONTRIBUTING.md | Guide      | Contributors               | ~10 min read |
| CHANGELOG.md    | Reference  | Version watchers           | ~2 min read  |

---

## Quick Command Reference

```bash
# Show help
epstein --help

# Basic search
epstein --search "query"

# Search and save to files
epstein --search "query" --limit 100

# Preview without saving
epstein --search "query" --no-save

# See all options
epstein --help
```

For more, see [USAGE.md](USAGE.md).

---

## Quick Python Reference

```python
from epstein import DOJMultimediaSearchClient

# Create client
client = DOJMultimediaSearchClient()

# Search
documents = client.search_all(query="query", max_results=100)

# Save results
client.save_results(documents, prefix="my_results")

# Get single page
docs, has_next = client.search(query="query", page=0)
```

For more, see [API.md](API.md).

---

## Need Help?

1. **Check relevant doc** - Most questions are answered in the appropriate file above
2. **Search the FAQ** - [FAQ.md](FAQ.md) covers common issues
3. **Review examples** - Check [USAGE.md](USAGE.md) for CLI or [API.md](API.md) for Python
4. **Read source code** - Check `epstein/client.py` and `epstein/cli.py` for implementation details

---

## File Locations

All documentation is in the `docs/` folder:

```
docs/
├── README.md          ← You are here
├── OVERVIEW.md        ← Why this tool exists
├── INSTALLATION.md    ← How to install
├── USAGE.md           ← How to use (CLI)
├── API.md             ← How to use (Python)
├── FAQ.md             ← Questions & answers
├── CONTRIBUTING.md    ← How to contribute
└── CHANGELOG.md       ← What's new
```

---

Last updated: February 8, 2026
