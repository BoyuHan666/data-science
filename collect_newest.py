import requests
import json
import sys, getopt
import os
from pathlib import Path

def get_path():
    opts, args = getopt.getopt(sys.argv, "o:s:", [])
    return args[2], args[4]


def main():
    output, subreddit = get_path()
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
    url = "https://oauth.reddit.com" + str(subreddit) + "/new.json?limit=100"
    res = requests.get(url, headers=headers)
    try:
        index = 0
        for i in range(len(output)):
            if output[i] == '/':
                index = i
        path = output[0:index]
        parentdir = os.path.abspath(Path(__file__).resolve().parents[1])
        new_dir = os.path.join(parentdir, path)
        if output[0] == '/':
            new_dir = path
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
    except:
        pass
    with open(str(output),'w') as f:
        for post in res.json()['data']['children']:
            d = json.dumps(post)
            f.write(d)
            f.write('\n')
    f.close()
    return


if __name__ == '__main__':
    main()
