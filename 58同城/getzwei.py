import bs4,requests
import pickle

zhiwei={}
def open_url(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
    res=requests.get(url,headers=headers)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    return soup
def get_zw():
    soup=open_url('http://hg.58.com/')
    tag=soup.find('div',class_='colWrap')
    tag2=tag.find_all('a')
    for each in tag2:
        zhiwei[each.text]=each['href']
    zhiweilist=open(r'D:\python\python_work\项目\58同城\my_zhiweilist.pkl','wb')
    pickle.dump(zhiwei,zhiweilist)
    zhiweilist.close()
