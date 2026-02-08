# Frequently Asked Questions

## General

### What is this tool for?

The Epstein DOJ Multimedia Search CLI provides programmatic access to the Department of Justice's public documents related to the Epstein case. Instead of clicking through a website, you can search and download metadata for thousands of documents instantly.

### Is this legal?

Yes. All documents are publicly available through official DOJ channels. This tool simply provides a more convenient way to access public records.

### Can I download the actual PDFs?

The tool provides URLs to all documents. You can then:

- Open URLs directly in your browser
- Use `curl` or `wget` to download
- Use Python's `urllib` library in a script

The tool focuses on metadata to keep it lightweight and fast.

### How many documents are available?

As of February 2026, there are thousands of documents in the DOJ Multimedia Search database. Exact count varies as documents may be added or removed.

### Do I need to register or authenticate?

No. The API is public and requires no login or API key.

## Technical Questions

### What Python version do I need?

Python 3.9 or higher. Check your version:

```bash
python3 --version
```

### Why am I getting "command not found: epstein"?

The `epstein` command is only available after installation with pip. If you cloned the repo, use:

```bash
python3 -m epstein.cli --search "query"
```

Or install from source:

```bash
pip install -e .
```

### How do I use this in my own Python code?

Import the client:

```python
from epstein import DOJMultimediaSearchClient

client = DOJMultimediaSearchClient()
documents = client.search_all(query="your_search", max_results=100)
```

See [API.md](API.md) for full documentation.

### Can I change the default delay between requests?

Yes, via the `--delay` option:

```bash
epstein --search "query" --delay 1.0  # 1 second
```

Or in Python:

```python
client.search_all(query="query", delay=1.0)
```

### What output formats are supported?

Three formats when you save:

1. **JSON** - Full metadata, easily parseable
2. **CSV** - Open in Excel, Google Sheets, etc.
3. **TXT** - Just the URLs, one per line

## Data & Search

### Can I search for multiple terms at once?

No, but you can run multiple searches:

```bash
epstein --search "trump" --prefix trump_results
epstein --search "clinton" --prefix clinton_results
```

Then combine the CSV files in Excel or a script.

### What happens if I search for a very common term?

Large searches take longer. For example, searching for "the" might return thousands of results. Use `--limit` to cap results:

```bash
epstein --search "the" --limit 100
```

### Can I get ALL documents?

Yes, use an empty search term:

```bash
epstein --search "" --limit 50000
```

This will take a while depending on your limit and delay settings.

### Are search results sorted?

The API returns results in its default order (usually by relevance). The CLI maintains the API's ordering.

### Can I filter results by date?

Not directly in the CLI. But you can:

1. Export to CSV
2. Open in Excel
3. Use Excel's filter on the `indexed_at` column

Or filter in Python:

```python
from epstein import DOJMultimediaSearchClient
import json

client = DOJMultimediaSearchClient()
docs = client.search_all(query="query")

# Filter to documents indexed in January 2026
january_docs = [d for d in docs if d['indexed_at'].startswith('2026-01')]
```

## Output & Files

### Where do my files go?

They're saved to the `lib_data/` folder in your current directory:

```
lib_data/
├── epstein_library_20260208_120000.json
├── epstein_library_20260208_120000.csv
└── epstein_library_20260208_120000_urls.txt
```

### Can I change the output location?

Not directly, but you can:

1. Move the files after generation
2. Customize the prefix with `--prefix` to organize by topic
3. Use Python API and save manually

### What's in the JSON file?

Complete metadata for each document:

- Title, filename, URL
- Document ID, file size, word count
- Page ranges
- Indexing timestamp
- And more (see [API.md](API.md))

### Can I open CSV files in Excel?

Yes! The CSV is formatted for spreadsheet software:

```bash
epstein --search "query" --limit 1000
open lib_data/epstein_library_*.csv  # macOS
# or on Windows: start lib_data\epstein_library_*.csv
```

### How do I download all the PDFs?

Extract URLs from the text file:

```bash
epstein --search "query" --limit 100 --prefix "my_search"

# Download all URLs (requires curl)
cat lib_data/my_search_*_urls.txt | xargs -I {} curl -O {}
```

Or use Python (see [API.md](API.md) for examples).

## Performance & Limitations

### Why is my search slow?

The API returns ~10 documents per request, so:

- 100 documents = 10 API calls = ~5 seconds (with 0.5s delay)
- 1000 documents = 100 API calls = ~50 seconds

You can speed up with `--delay 0.1` but don't overload the servers.

### Can I reduce the delay below 0.1 seconds?

Technically yes, but not recommended:

```bash
epstein --search "query" --delay 0.01
```

If you hit rate limits, increase the delay back.

### What if I get a timeout?

Network issues or the DOJ servers being slow. Try:

1. Increase delay: `--delay 1.0`
2. Reduce limit: `--limit 50`
3. Try again later

### Can I cancel a search?

Press `Ctrl+C` to stop. Your partial results won't be saved unless you run with `--head` to display only (not save).

### How much disk space do files take?

Roughly:

- JSON: 20-50 KB per 100 documents
- CSV: 10-30 KB per 100 documents
- TXT: 1-5 KB per 100 documents

1000 documents ≈ 200-300 KB total

## Troubleshooting

### I get SSL certificate errors

Update your certificates:

```bash
python3 -m pip install --upgrade certifi
```

Or disable verification (not recommended):

```bash
# In Python code
import urllib3
urllib3.disable_warnings()
```

### Some URLs are broken

The DOJ sometimes reorganizes files or links expire. This is rare but possible. Check if the link works in a browser first.

### My search returned 0 results

Possible reasons:

1. **Typo in search term** - Try a simpler term
2. **Very specific search** - The term might not exist in documents
3. **API issue** - Try searching without a term: `epstein --search ""`

### How do I report a bug?

Open an issue on GitHub with:

1. Command you ran
2. Error message
3. Python version
4. OS (macOS, Linux, Windows)

## Legal & Ethics

### Is there anything illegal about this tool?

No. The documents are public and the tool simply accesses publicly available APIs.

### Should I be concerned about my searches?

Your searches go to the official DOJ API. The tool doesn't use any tracking or logging beyond what the DOJ's normal servers do.

### Can I use this commercially?

Check the license file. Typically yes, for data analysis, research, or journalism.

### Is the tool affiliated with the DOJ?

No. This is an independent tool created to provide better access to public records.

## Still Have Questions?

- **For usage**: See [USAGE.md](USAGE.md)
- **For API details**: See [API.md](API.md)
- **For installation help**: See [INSTALLATION.md](INSTALLATION.md)
- **For project info**: See [OVERVIEW.md](OVERVIEW.md)
