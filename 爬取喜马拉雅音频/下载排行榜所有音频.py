import requests
import json
import re
import os

def get_id():
    base_url = "https://www.ximalaya.com/revision/getRankList?code=yinyue"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    res = requests.get(base_url,headers=headers)
    result = json.loads(res.content.decode())
    all_author = []
    for i in result['data']['albums']:
        author={}
        author['id'] = (i['id'])
        author['name'] = (i['albumTitle'])
        all_author.append(author)
    return all_author

def get_info(mus_id,mus_name):
    if not os.path.exists(mus_name):
        os.mkdir(mus_name)
    start_url = "https://www.ximalaya.com/revision/play/album?albumId="+str(mus_id)+"&pageNum={}&sort=-1&pageSize=30"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    for i in range(5):
        url = start_url.format(i+1)
        res = requests.get(url,headers=headers)
        result = json.loads(res.content.decode())['data']['tracksAudioPlay']
        for i in result:
            scr = i["src"]    
            name = i["trackName"]    
            #去掉文件中的?"| 的字符用空字符代替
            name = re.sub(r'\?|"|\|',"",name)
            # 既然能够获取每个音频url，我们就可以直接访问这个url来得到二进制数据，并保存
            mus = requests.get(scr,headers=headers)
            with open("./"+mus_name+"/{}.m4a".format(name),'ab') as f:
                f.write(mus.content)
                print(name)
if __name__ =="__main__":
    all_author = get_id()
    for i in all_author:
        get_info(i['id'],i['name'])

