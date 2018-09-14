import requests
import re
import bs4

def open_url(url):
    headers = {"User-Agent":"Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
    res = requests.get(url,headers=headers)
    return res

def get_one_file_detail(a_url):
    res = open_url(a_url)
    # ~ decode('gbk','ignore')非常重要%%%%%%%
    bsobj = bs4.BeautifulSoup(res.content.decode('gbk','ignore'),"html.parser")
    name = bsobj.find('h1')
    name = re.findall(r'[^《》]+',name.text)[1]
    td = bsobj.find('td',attrs={'style':"WORD-WRAP: break-word"})
    url_a = td.find('a')
    return name,url_a.text


def get_one_page_urls(url):
    res = open_url(url)
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
    names = []
    detail_urls = []
    f = open("dytt.txt","w",encoding="utf-8")
    for i in range(2,10):
        url = "http://www.dy2018.com/2/index_%s.html"%i
        urls = []
        urls = get_one_page_urls(url)
        for a_url in urls:
            name,detail_url=get_one_file_detail(a_url)
            f.write("%s:%s\n\n" % (name, detail_url))
    

if __name__ =="__main__":
    main()
