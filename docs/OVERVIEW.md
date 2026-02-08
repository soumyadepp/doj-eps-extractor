# Epstein DOJ Multimedia Search CLI

## Why This CLI Was Created

The DOJ released a large archive of documents related to the Epstein case. These documents are publicly available through the Justice Department's multimedia search portal, but accessing and downloading them at scale was difficult:

1. **No Built-in Bulk Download**: The web interface only allows searching and viewing one document at a time
2. **Manual Data Extraction**: Researchers, journalists, and the public had no programmatic way to access document metadata and links
3. **Poor Accessibility**: Finding specific documents across thousands of files was time-consuming
4. **No Data Export**: The search interface didn't provide CSV/JSON exports for further analysis

### The Solution

**Epstein CLI** provides:

- **Programmatic Access**: Query the DOJ Multimedia Search API directly from the command line
- **Bulk Export**: Download metadata for hundreds or thousands of documents at once
- **Multiple Formats**: Export results as JSON, CSV, or plain text URL lists
- **Fast & Efficient**: Configurable delays to respect server resources
- **Easy Integration**: Use as a CLI tool or import the Python client in your own projects

## Use Cases

- **Academic Research**: Analyze document patterns and metadata at scale
- **Investigative Journalism**: Find documents related to specific topics or names
- **Data Analysis**: Export to spreadsheets for filtering and analysis
- **Archival**: Create local backups of document metadata and URLs
- **Public Access**: Make public records more accessible to the general public

## Key Features

- ✅ Search millions of documents by keyword
- ✅ Pagination support for large result sets
- ✅ Export to JSON, CSV, and TXT formats
- ✅ Properly URL-encoded document links
- ✅ Configurable request delays
- ✅ Clean, structured metadata output
- ✅ Both CLI and Python API access

## Technical Details

The CLI queries the official DOJ Multimedia Search API at `https://www.justice.gov/multimedia-search` and parses Elasticsearch JSON responses to extract document metadata including:

- Document filename and ID
- Direct download URLs
- File size and word count
- Page ranges
- Index timestamp

All data remains public and is sourced directly from official government servers.
