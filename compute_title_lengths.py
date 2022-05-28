import os,sys
import json

def main():
    input_file = sys.argv[1]
    with open(input_file,'r') as f:
        data = f.readlines()
    f.close()

    new_data_list = []
    for line in data:
        try:
            new_line = json.loads(line)
            new_data_list.append(new_line)
        except:
            pass

    total_length = 0
    for post in new_data_list:
        title = post['data']['title']
        total_length += len(title)
    avg_length = total_length/len(new_data_list)
    avg_length = "{:.2f}".format(avg_length)
    print(avg_length)
    return avg_length

if __name__ == '__main__':
    main()