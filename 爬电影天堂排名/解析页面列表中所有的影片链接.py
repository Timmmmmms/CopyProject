import requests
import re
import bs4

def open_url(url):
    headers = {"User-Agent":"Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
    res = requests.get(url,headers=headers)
    return res

def get_one_page_urls(res):
    urls = []
    base_url = "https://www.dy2018.com"
    soup = bs4.BeautifulSoup(res.content,"html.parser")
    url_all = soup.find_all('a',attrs={"class":"ulink","title":re.compile('.*')})
    for url in url_all:
        a_url = url.get("href")
        url = base_url + a_url
        urls.append(url)
    return urls
        
def main():
    url = "http://www.dy2018.com/2/index_3.html"
    res = open_url(url)
    urls = []
    urls = get_one_page_urls(res)
    print(urls)
    

if __name__ =="__main__":
    main()
