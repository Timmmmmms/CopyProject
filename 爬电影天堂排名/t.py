# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
import sys



def get_bs(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36'}
    text = requests.post(url, headers=headers).text
    return BeautifulSoup(text)

def download(url):
    fn = re.search(r'.*/(.*)', url).group(1)
    content = requests.get(url).content
    with open(fn, 'wb') as f:
        f.write(content)

if __name__ == '__main__':
    url = 'http://jandan.net/ooxx'
    bs = get_bs(url)
    for code in bs('li', id=re.compile(r'comment-\d+')):
        url = code.find('img')['src']
        download(url)
