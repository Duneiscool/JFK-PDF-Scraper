# JFK Archives PDF Scraper

This script downloads all PDF files from the JFK Archives website (https://www.archives.gov/research/jfk/release-2025).

## Requirements

- Python 3.6 or higher
- Required packages listed in `requirements.txt`

## Installation

1. Clone or download this repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Simply run the script:
```bash
python jfk_pdf_scraper.py
```

The script will:
1. Create a new directory with a timestamp (e.g., `jfk_pdfs_20240321_143022`)
2. Download all PDF files found on the webpage
3. Save them in the created directory
4. Show progress and results in the console

## Features

- Creates timestamped directories for each run
- Handles both relative and absolute URLs
- Includes error handling and progress reporting
- Respects server load with delays between downloads
- Streams large files to handle memory efficiently

## Notes

- The script includes a 1-second delay between downloads to be respectful to the server
- If a PDF download fails, the script will continue with the remaining files
- The script will create a new directory for each run to prevent overwriting previous downloads 