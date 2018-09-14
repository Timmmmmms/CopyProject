import re
import requests
import bs4

def open_url(url):
    headers = {"User-Agent":"Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
    res = requests.get(url,headers=headers)
    return res

def get_one_file_detail(res):
    bsobj = bs4.BeautifulSoup(res.content.decode('gbk','ignore'),"html.parser")
    name = bsobj.find('h1')
    name = re.findall(r'[^《》]+',name.text)[1]
    td = bsobj.find('td',attrs={'style':"WORD-WRAP: break-word"})
    url_a = td.find('a')
    return name,url_a.text


def main():
    url = "https://www.dy2018.com/i/99133.html"
    res = open_url(url)
    name,url = get_one_file_detail(res)
    print("电影名称："+name+"\n"+"下载地址："+url)
if __name__ == "__main__":
    main()
