#!/usr/bin/env python3
"""
DOJ Multimedia Search API Client
Query the DOJ Multimedia Search endpoint and export document metadata

This module is kept for backward compatibility.
For CLI usage, run: python3 -m epstein.cli or use 'epstein' command

Requirements:
    uv sync

Usage:
    python3 main.py --search "search term" --limit 100
    python3 -m epstein.cli --search "search term" --limit 100
    epstein --search "search term" --limit 100
"""

# Import from the new package structure for backward compatibility
from epstein import DOJMultimediaSearchClient
from epstein.cli import main

if __name__ == "__main__":
    main()
