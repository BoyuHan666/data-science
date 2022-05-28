import json
import csv
import sys, getopt
import os
import pathlib

def get_path():
    opts, args = getopt.getopt(sys.argv, "i:o:", [])
    outputfile = args[4]
    inputfile = args[2]
    return outputfile, inputfile


def get_top101_character(csvreader):
    dic = {}
    c_list = []
    seq = []
    episode_list = []
    drop_words = ['others', 'ponies', 'and', 'all']
    for line in csvreader:
        character = line[2]
        episode = line[0]
        seq.append(character)
        episode_list.append(episode)
        flag = True
        for char in character.split(' '):
            if char.lower() in drop_words:
                flag = False
        if flag:
            character = character.lower()
            if character not in c_list:
                dic[character] = 1
                c_list.append(character)
            else:
                dic[character] += 1

    summary_dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    top_101 = []
    top_101_dic = {}
    count = 0
    for character in summary_dic.keys():
        if count < 101:
            top_101.append(character)
            top_101_dic[character] = summary_dic[character]
            count += 1
        else:
            break
    for i in range(len(top_101)):
        top_101[i] = top_101[i].lower()
    for i in range(len(seq)):
        seq[i] = seq[i].lower()
    return top_101, seq, episode_list

def generate_file(output,summary_dic):
    try:
        index = 0
        for i in range(len(output)):
            if output[i] == '/':
                index = i
        path = output[0:index]
        parentdir = os.path.abspath(pathlib.Path(__file__).resolve().parents[1])
        new_dir = os.path.join(parentdir, path)
        if output[0] == '/':
            new_dir = path
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
    except:
        pass
    with open(output, 'w') as f:
        json.dump(summary_dic, f, indent=4)
    f.close()
    return

def main():
    outputfile, inputfile = get_path()
    with open(inputfile, 'r') as f:
        csvreader = csv.reader(f)
        top_101,seq,epl = get_top101_character(csvreader)
    f.close()
    dic_101 = {}
    for char in top_101:
        dic_101[char] = {}
    for i in range(len(seq)-1):
        char1 = seq[i]
        char2 = seq[i+1]
        ep1 = epl[i]
        ep2 = epl[i+1]
        if ep1 != ep2:
            continue
        if (char1 in top_101) and (char1 != char2):
            if char2 in top_101:
                if char2 in dic_101[char1].keys():
                    dic_101[char1][char2] += 1
                else:
                    dic_101[char1][char2] = 1
                if char1 in dic_101[char2].keys():
                    dic_101[char2][char1] += 1
                else:
                    dic_101[char2][char1] = 1

    network = {}
    for key in dic_101.keys():
        if dic_101[key] != {}:
            network[key] = dic_101[key]

    new_dic = {}
    for pony in network.keys():
        new_dic[pony] = dict(sorted(network[pony].items(), key=lambda item: item[1], reverse=True))
    generate_file(outputfile, new_dic)

if __name__ == '__main__':
    main()
