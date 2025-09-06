# Python Command-Line File Downloader  

A simple Python script that downloads files from the internet using a URL.  
It supports custom filenames, adds headers to avoid errors, and automatically creates a `DownloadedFiles` folder to store files.  

## 🚀 Features  
- Download any file from a given URL  
- Optional custom filename (otherwise extracted from URL)  
- Creates a `DownloadedFiles` folder automatically  
- Adds headers to prevent request blocking (403 errors)  
- Opens the folder automatically after download (Windows only)  
- Efficient chunked downloading to handle large files  

## 🛠️ Technologies Used  
- **Python 3**  
- **os** → File and folder management  
- **requests** → Handling HTTP requests  
- **argparse** → Command-line interface  

## 📂 Project Structure  
├── downloader.py      # Main script  
├── DownloadedFiles/   # Folder where files will be saved (auto-created)  


## ⚡ Usage  

```bash
# 1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# 2. Install requirements
pip install requests

# 3. Run the script with a URL
python downloader.py <URL> -o <optional_filename>

# Example
python downloader.py https://example.com/sample.jpg -o myimage.jpg



