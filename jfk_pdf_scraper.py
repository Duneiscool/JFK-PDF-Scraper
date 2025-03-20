import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
from datetime import datetime

def create_download_directory():
    """Create a directory to store downloaded PDFs with timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    directory = f"jfk_pdfs_{timestamp}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def is_pdf(url):
    """Check if the URL points to a PDF file."""
    return url.lower().endswith('.pdf')

def download_pdf(url, directory):
    """Download a PDF file from the given URL."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Extract filename from URL
        filename = os.path.basename(urlparse(url).path)
        if not filename:
            filename = 'document.pdf'
        
        # Create full file path
        filepath = os.path.join(directory, filename)
        
        # Download the file
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        print(f"Successfully downloaded: {filename}")
        return True
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")
        return False

def scrape_pdfs(url):
    """Scrape PDFs from the given URL."""
    # Create download directory
    download_dir = create_download_directory()
    print(f"Created directory: {download_dir}")
    
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all links
        links = soup.find_all('a')
        
        # Filter and download PDFs
        pdf_count = 0
        for link in links:
            href = link.get('href')
            if href:
                # Convert relative URL to absolute URL
                full_url = urljoin(url, href)
                
                if is_pdf(full_url):
                    print(f"Found PDF: {full_url}")
                    if download_pdf(full_url, download_dir):
                        pdf_count += 1
                    # Add a small delay to be respectful to the server
                    time.sleep(1)
        
        print(f"\nScraping completed!")
        print(f"Total PDFs downloaded: {pdf_count}")
        print(f"PDFs are saved in: {os.path.abspath(download_dir)}")
        
    except Exception as e:
        print(f"Error scraping the website: {str(e)}")

if __name__ == "__main__":
    target_url = "https://www.archives.gov/research/jfk/release-2025"
    print("Starting PDF scraper...")
    scrape_pdfs(target_url) 