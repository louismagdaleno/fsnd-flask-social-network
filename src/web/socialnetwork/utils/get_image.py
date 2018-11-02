from bs4 import BeautifulSoup
import urllib.request
import shutil
import requests
from urllib.parse import urljoin
import sys
import time


def make_soup(url):
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
    html = urllib.request.urlopen(req)
    return BeautifulSoup(html, 'html.parser')


def get_images(url):
    soup = make_soup(url)
    images = [img for img in soup.findAll('img')]
    print (str(len(images)) + " images found.")
    print('Downloading images to current working directory.')
    image_links = [each.get('src') for each in images]
    for each in image_links:
        try:
            filename = each.strip().split('/')[-1].strip()
            src = urljoin(url, each)
            print('Getting: ' + filename)
            response = requests.get(src, stream=True)
            # delay to avoid corrupted previews
            time.sleep(1)
            with open(filename, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
        except:
            print('  An error occured. Continuing.')
    print('Done.')