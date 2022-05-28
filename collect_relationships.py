import requests
import json
import bs4
from pathlib import Path
import sys, getopt, os
import os.path as osp
import hashlib

BASE_URL = "https://www.whosdatedwho.com/dating/"

def get_path():
    opts,args = getopt.getopt(sys.argv, "c:o:", [])
    return args[2],args[4]

def create_dir(path):
    try:
        parentdir = os.path.abspath(Path(__file__).resolve().parents[1])
        new_dir = os.path.join(parentdir, path)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
    except:
        pass
    return

def main():
    conf_file,outfile = get_path()
    with open(conf_file,'r') as f:
        js = json.load(f)
    f.close()
    cache_dir = js['cache_dir']
    celebrities = js['target_people']
    create_dir(str(cache_dir))
    cache_list = []
    for name in celebrities:
        hash = hashlib.sha1(str(name).encode("UTF-8")).hexdigest()
        cache_file = "../"+cache_dir+"/"+hash+".html"
        cache_list.append(cache_file)
        if not osp.exists(cache_file):
            html_content = requests.get(BASE_URL + str(name), 'html.parser')
            with open(cache_file,'w') as f:
                f.write(html_content.text)
            f.close()

    relation_list = []
    for file in cache_list:
        soup = bs4.BeautifulSoup(open(file, 'r'), 'html.parser')
        Relationships = soup.find('h4', 'ff-auto-relationships')
        p_tags = Relationships.findNextSiblings('p')
        names = []
        for p_tag in p_tags:
            a_tags = p_tag.find_all('a')
            for a_tag in a_tags:
                name = a_tag.string
                names.append(name)
        relation_list.append(names)

    # dic = {}
    # for i in range(len(celebrities)):
    #     dic[celebrities[i]] = relation_list[i]

    key_str = ''
    for i in range(len(celebrities)):
        names_str = ''
        for name in relation_list[i]:
            names_str += '"'+str(name)+'", '
        total_names = '[' + names_str[:-2] + ']'
        key_str += '\n\t'+'"'+str(celebrities[i])+'": '+ total_names + ','
    total_str = '{' + key_str[:-1] + '\n}'

    with open(outfile, 'w') as f:
        f.write(total_str)
    f.close()

    return


if __name__ == '__main__':
    main()