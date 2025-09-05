# Python File Downloader CLI Tool

A simple **Command Line Interface (CLI) tool** written in Python to download files from a given URL.

---

## 🚀 Features
- Download files directly from a URL.
- Optionally specify a custom output filename (`-o` or `--output`).
- Streams file in chunks for efficient downloading (supports large files).
- User-friendly command-line interface built with `argparse`.

---

## 💻 Usage

```bash
# Basic usage
python downloader.py "https://example.com/file.pdf"

# With custom output filename
python downloader.py "https://example.com/file.pdf" -o myfile.pdf
