# GitHub Trending Repository CLI

A lightweight Python command-line tool that fetches and displays the most popular GitHub repositories created within a selected time period (day, week, month, or year), ranked by number of stars.

This tool uses the official GitHub Search API to help developers quickly discover trending or recently popular open-source projects without manually browsing GitHub.

## Features

- Fetch top repositories based on creation date
- Sorts results by star count (most popular first)
- Supports multiple time filters:
  - Past day
  - Past week
  - Past month
  - Past year
- Displays key repository details:
  - Name
  - Description
  - Primary language
  - Star count
  - GitHub URL
- Simple CLI interface using argparse
- Basic error handling for API and network issues

## Tech Stack

- Python 3
- Requests (GitHub REST API v3)
- Argparse (CLI handling)
- Datetime (time-based filtering)

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone or download this repository
2. Install required dependencies:
   ```bash
   pip install requests
   ```

## How It Works

The tool calculates a date based on the selected duration, then queries the GitHub Search API using:
```
created:>YYYY-MM-DD
```

It then sorts repositories by stars in descending order and displays the top results in a formatted output.

## Usage

```bash
python main.py --duration week --limit 20
```

## Options

| Argument | Description |
|----------|-------------|
| `--duration` | Time range: `day`, `week`, `month`, `year` (default: `week`) |
| `--limit` | Number of repositories to display (default: `20`) |

## Example Output

```
========================================
Top Repositories:
========================================
Name: example-repo
Description: A cool project
Language: Python
Stars: 12000
URL: https://github.com/user/example-repo
----------------------------------------
```

## Testing

Unit tests are provided to validate the functionality of the application. Tests are written using `pytest` and include mocking for API calls to avoid external dependencies.

### Install Testing Dependencies

```bash
pip install pytest
```

### Run Tests

```bash
python3 -m pytest
```

Or with verbose output:

```bash
python3 -m pytest -v
```

### Test Coverage

The test suite covers:
- Date calculation for different durations
- API parameter construction
- Error handling for invalid inputs
- Repository data display formatting