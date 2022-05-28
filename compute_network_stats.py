import json
import networkx as nx
import sys, getopt
import pandas as pd
import os
import pathlib

def get_path():
    opts, args = getopt.getopt(sys.argv, "i:o:", [])
    outputfile = args[4]
    inputfile = args[2]
    return outputfile, inputfile

def get_data(inputfile):
    with open(inputfile, 'r') as f:
        data = json.load(f)
    f.close()
    return data

def dic_to_js_str(output,n):
    output_str = '{'
    count = 0
    for pony in output.keys():
        total_word_str = ''
        count += 1
        index = 0
        for word in output[pony]:
            if index == 0:
                total_word_str += '"' + word + '"'
                index += 1
            else:
                total_word_str += ', "' + word + '"'
        if count == n:
            output_str += '\n\t"' + pony + '": [' + total_word_str + ']'
        else:
            output_str += '\n\t"' + pony + '": [' + total_word_str + '],'
    output_str += '\n}'
    return output_str

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

    outstring = dic_to_js_str(summary_dic,3)
    with open(output, 'w') as f:
        f.write(outstring)
    f.close()
    return

def main():
    outputfile, inputfile = get_path()
    data = get_data(inputfile)
    dic = {}
    dic['most_connected_by_num'] = []
    dic['most_connected_by_weight'] = []
    dic['most_central_by_betweenness'] = []
    graph = nx.Graph()
    for node1 in data.keys():
        for node2 in data[node1].keys():
            graph.add_edge(node1, node2, weight=data[node1][node2])
    lst1 = []

    for i in graph.degree:
        tmp = []
        tmp.append(i[1])
        tmp.append(i[0])
        lst1.append(tmp)
    c11 = sorted(lst1, reverse=True)[0][1]
    c21 = sorted(lst1, reverse=True)[1][1]
    c31 = sorted(lst1, reverse=True)[2][1]
    # print(sorted(lst1, reverse=True))
    dic['most_connected_by_num'] = [c11,c21,c31]

    weight_dic = {}
    for edge in graph.edges:
        node1 = edge[0]
        node2 = edge[1]
        weight = graph.get_edge_data(node1, node2)['weight']
        if node1 not in weight_dic.keys():
            weight_dic[node1] = weight
        else:
            weight_dic[node1] += weight
        if node2 not in weight_dic.keys():
            weight_dic[node2] = weight
        else:
            weight_dic[node2] += weight
    sorted_weight_dic = dict(sorted(weight_dic.items(), key=lambda item: item[1], reverse=True))
    count = 0
    for key in sorted_weight_dic.keys():
        if count < 3:
            count += 1
            dic['most_connected_by_weight'].append(key)

    betweenness_dic = nx.betweenness_centrality(graph)
    sorted_betweenness_dic = dict(sorted(betweenness_dic.items(), key=lambda item: item[1], reverse=True))
    count2 = 0
    for key in sorted_betweenness_dic.keys():
        if count2 < 3:
            count2 += 1
            dic['most_central_by_betweenness'].append(key)

    # with open('weight.json', 'w') as f:
    #     json.dump(sorted_weight_dic,f, indent=4)
    #     f.close()
    # with open('betweenness.json', 'w') as f:
    #     json.dump(sorted_betweenness_dic, f, indent=4)
    #     f.close()

    generate_file(outputfile,dic)

if __name__ == '__main__':
    main()