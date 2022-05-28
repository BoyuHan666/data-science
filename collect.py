import requests
import json

def sample1():
    id = "Al-OEI5e_WioPFUvQBfPxg"
    key = "NvDE01YZUVaClmrbuH8JsePe-FCnRA"

    user = requests.auth.HTTPBasicAuth(id, key)
    access_dic = {
        'grant_type': 'password',
        'username': 'Alainhby',
        'password': 'kuailexingqiu'
    }
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=user, data=access_dic, headers=headers)
    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
    res1 = requests.get("https://oauth.reddit.com/r/funny/new.json?limit=100", headers=headers)
    res2 = requests.get("https://oauth.reddit.com/r/AskReddit/new.json?limit=100", headers=headers)
    res3 = requests.get("https://oauth.reddit.com/r/gaming/new.json?limit=100", headers=headers)
    res4 = requests.get("https://oauth.reddit.com/r/aww/new.json?limit=100", headers=headers)
    res5 = requests.get("https://oauth.reddit.com/r/pics/new.json?limit=100", headers=headers)
    res6 = requests.get("https://oauth.reddit.com/r/Music/new.json?limit=100", headers=headers)
    res7 = requests.get("https://oauth.reddit.com/r/science/new.json?limit=100", headers=headers)
    res8 = requests.get("https://oauth.reddit.com/r/worldnews/new.json?limit=100", headers=headers)
    res9 = requests.get("https://oauth.reddit.com/r/videos/new.json?limit=100", headers=headers)
    res10 = requests.get("https://oauth.reddit.com/r/todayilearned/new.json?limit=100", headers=headers)
    res_list = [res1,res2,res3,res4,res5,res6,res7,res8,res9,res10]
    with open('../sample1.json','w') as f:
        for res in res_list:
            for post in res.json()['data']['children']:
                d = json.dumps(post)
                f.write(d)
                f.write('\n')
    f.close()
    return

def sample2():
    id = "Al-OEI5e_WioPFUvQBfPxg"
    key = "NvDE01YZUVaClmrbuH8JsePe-FCnRA"

    user = requests.auth.HTTPBasicAuth(id, key)
    access_dic = {
        'grant_type': 'password',
        'username': 'Alainhby',
        'password': 'kuailexingqiu'
    }
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=user, data=access_dic, headers=headers)
    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
    res1 = requests.get("https://oauth.reddit.com/r/AskReddit/new.json?limit=100", headers=headers)
    res2 = requests.get("https://oauth.reddit.com/r/memes/new.json?limit=100", headers=headers)
    res3 = requests.get("https://oauth.reddit.com/r/politics/new.json?limit=100", headers=headers)
    res4 = requests.get("https://oauth.reddit.com/r/nfl/new.json?limit=100", headers=headers)
    res5 = requests.get("https://oauth.reddit.com/r/nba/new.json?limit=100", headers=headers)
    res6 = requests.get("https://oauth.reddit.com/r/wallstreetbets/new.json?limit=100", headers=headers)
    res7 = requests.get("https://oauth.reddit.com/r/teenagers/new.json?limit=100", headers=headers)
    res8 = requests.get("https://oauth.reddit.com/r/PublicFreakout/new.json?limit=100", headers=headers)
    res9 = requests.get("https://oauth.reddit.com/r/leagueoflegends/new.json?limit=100", headers=headers)
    res10 = requests.get("https://oauth.reddit.com/r/unpopularopinion/new.json?limit=100", headers=headers)
    res_list = [res1,res2,res3,res4,res5,res6,res7,res8,res9,res10]
    with open('../sample2.json','w') as f:
        for res in res_list:
            for post in res.json()['data']['children']:
                d = json.dumps(post)
                f.write(d)
                f.write('\n')
    f.close()
    return

def main():
    sample1()
    sample2()

if __name__ == '__main__':
    main()