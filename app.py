from flask import Flask, redirect, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_hls_link(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Searching for the HLS link, adjust this according to the website structure
    hls_links = soup.find_all('a', href=lambda x: x and '.m3u8' in x)
    
    if hls_links:
        return hls_links[0]['href']
    else:
        return None

@app.route('/')
def index():
    target_url = request.args.get('url')
    
    if target_url:
        hls_link = get_hls_link(target_url)
        
        if hls_link:
            return redirect(hls_link)
        else:
            return "No HLS link found!", 404
    else:
        return "Please provide a valid URL.", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8070)
