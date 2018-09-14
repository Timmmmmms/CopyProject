import requests
import json

def main():
    url = "https://www.ximalaya.com/revision/play/album?albumId=11873814&pageNum=1&sort=-1&pageSize=30"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    res = requests.get(url,headers=headers)
    # ~ print(json.loads(res.text)['data']['tracksAudioPlay'])
    result = json.loads(res.content.decode())['data']['tracksAudioPlay']
    for i in result:
        scr = i["src"]    
        name = i["trackName"]    
        # 既然能够获取每个音频url，我们就可以直接访问这个url来得到二进制数据，并保存
        mus = requests.get(scr,headers=headers)
        with open("./music/{}.m4a".format(name),'ab') as f:
            f.write(mus.content)
            print(name)
if __name__ =="__main__":
    main()
