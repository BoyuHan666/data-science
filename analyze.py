import json
import sys, getopt
import os
from pathlib import Path
def get_path():
    opts, args = getopt.getopt(sys.argv, "i:o:", [])
    input = args[2]
    output = ''
    if len(args) == 5:
        output = args[4]
    return input,output
def main():
    input,output = get_path()

    with open(str(input),'r') as f:
        data = f.readlines()
    f.close()

    code_dic = {"course-related":0, "food-related":0,
                "residence-related":0, "other":0}
    for l in data[1:]:
        if l[-2] == 'c':
            code_dic["course-related"] += 1
        if l[-2] == 'f':
            code_dic["food-related"] += 1
        if l[-2] == 'r':
            code_dic["residence-related"] += 1
        if l[-2] == 'o':
            code_dic["other"] += 1

    summary_table = {"course-related":str(code_dic["course-related"]),
                     "food-related":str(code_dic["food-related"]),
                     "residence-related":str(code_dic["residence-related"]),
                     "other":str(code_dic["other"])}
    if output == '':
        print(json.dumps(code_dic,indent=0))
    else:
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
        with open(str(output), 'w') as fp:
            json.dump(code_dic, indent=0, fp=fp)
        fp.close()

    return

if __name__ == '__main__':
    main()