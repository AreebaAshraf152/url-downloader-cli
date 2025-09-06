import argparse
import requests
import os

# Create a folder inside your project to store downloads
download_folder = "DownloadedFiles"
if not os.path.exists(download_folder):
    os.makedirs(download_folder)


def download_file(url, local_filename=None):
    # If no filename is provided, use the last part of the URL
    if local_filename is None:
        local_filename = url.split('/')[-1]

    # Save inside the DownloadedFiles folder
    local_filename = os.path.join(download_folder, local_filename)

    headers = {"User-Agent": "Mozilla/5.0"}  # Helps avoid 403 errors
    with requests.get(url, stream=True, headers=headers) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    return local_filename

# Setup command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("url", help="URL of the file to download")
parser.add_argument("-o", "--output", type=str,
                    help="Filename to save as",default=None)
args = parser.parse_args()

# Run the downloader
saved_file = download_file(args.url, args.output)
print(f"File downloaded successfully and saved as: {saved_file}")

# Automatically open the folder where the file is saved
folder_path = os.path.abspath(download_folder)
os.startfile(folder_path)  # This opens the folder in File Explorer
