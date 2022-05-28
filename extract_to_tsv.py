import json
import sys, getopt
import pandas as pd
import os
from pathlib import Path

def get_path():
    opts, args = getopt.getopt(sys.argv, "o:", [])
    return args[2], args[3], args[4]

def main():
    output,jf,npto = get_path()
    npto = int(npto)
    with open(jf, 'r') as f:
        data = f.readlines()
    f.close()
    new_data_list = []
    for line in data:
        try:
            new_line = json.loads(line)
            new_data_list.append(new_line)
        except:
            pass
    if npto > len(new_data_list):
        npto = len(new_data_list)

    col1,col2,col3= [],[],[]
    for l in new_data_list:
        col1.append(l['data']['name'])
        col2.append(l['data']['title'])
        col3.append('')
    df_data = {'Name':col1, 'title':col2, 'coding':col3}
    df = pd.DataFrame(df_data).sample(npto)
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
    df.to_csv(str(output), sep="\t", index=False)

if __name__ == '__main__':
    main()