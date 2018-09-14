import requests
import json
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
    print(all_author)
if __name__=="__main__":
    get_id()
