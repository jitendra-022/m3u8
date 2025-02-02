import requests
from bs4 import BeautifulSoup

def get_hls_link(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Searching for the HLS link, adjust this according to the website structure
    hls_links = soup.find_all('a', href=lambda x: x and '.m3u8' in x)
    
    if hls_links:
        return hls_links[0]['href']
    else:
        return None
