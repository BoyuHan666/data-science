import json
import pytz
import datetime
import sys, getopt

def get_path():
    opts,args = getopt.getopt(sys.argv, "hi:o:", [])
    return args[2],args[4]

# path1 = '/Users/alain/Desktop/hw5/submission_template/data/example.json'
# path2 = '/Users/alain/Desktop/hw5/submission_template/data/output.txt'
def trim_data(path1):
  with open(path1, 'r', encoding='utf-8') as f:
    data = f.readlines()
  f.close()
  return data

# part 1 and 2 for title
def check_title(new_data_list):
    final_data1 = []
    for line in new_data_list:
        keys = list(line.keys())
        if 'title' in keys:
            final_data1.append(line)
        elif 'title_text' in keys:
            v = line.pop('title_text')
            new_line = {}
            new_line['title'] = v
            new_line.update(line)
            final_data1.append(new_line)
    return final_data1

# part 3 and 4 for datetime
def check_createdAt(final_data1):
    final_data2 = []
    for line in final_data1:
        if 'createdAt' not in list(line.keys()):
            final_data2.append(line)
        else:
            try:
                iso_time = datetime.datetime.strptime(line['createdAt'], "%Y-%m-%dT%H:%M:%S%z")
                utc_time = iso_time.astimezone(pytz.utc)
                s = str(utc_time)
                new_utc = s[0:10] + 'T' + s[11:22] + s[23:25]
                line['createdAt'] = str(new_utc)
                final_data2.append(line)
            except:
                pass
    return final_data2

# part 5 for invalid json
def check_json(data):
    new_data_list = []
    for line in data:
        try:
            new_line = json.loads(line)
            new_data_list.append(new_line)
        except:
            pass
    return new_data_list

# part 6 for author
def check_author(final_data2):
    final_data3 = []
    for line in final_data2:
        if 'author' not in list(line.keys()):
            final_data3.append(line)
        else:
            try:
                if line['author'] == None or line['author'] == 'N/A' or line['author'] == 'null':
                    pass
                else:
                    final_data3.append(line)
            except:
                pass
    return final_data3

# part 7 and 8 for total_count
def check_total_count(final_data3):
    final_data4 = []
    for line in final_data3:
        if 'total_count' not in list(line.keys()):
            final_data4.append(line)
        else:
            try:
                t = type(line['total_count'])
                if t == int or t == float or t == str:
                    line['total_count'] = int(line['total_count'])
                    final_data4.append(line)
            except:
                pass
    return final_data4

# part 9 for tags
def check_tags(final_data4):
    final_data5 = []
    for line in final_data4:
        if 'tags' not in list(line.keys()):
            final_data5.append(line)
        else:
            try:
                new_l = []
                for s in line['tags']:
                    for ele in s.split(' '):
                        if ele == '':
                            pass
                        else:
                            new_l.append(ele)
                line['tags'] = new_l
                final_data5.append(line)
            except:
                pass
    return final_data5

#
def generate_output(path2,final_data5):
    with open(path2, 'w', encoding='utf-8') as f:
        for line in final_data5:
            d = json.dumps(line)
            f.write(d)
            f.write('\n')
    f.close()

def main():
    # path1 = '/Users/alain/Desktop/hw5/submission_template/data/example.json'
    # path2 = '/Users/alain/Desktop/hw5/submission_template/data/output.json'
    path1,path2 = get_path()
    data = trim_data(path1)
    new_data_list = check_json(data)
    final_data1 = check_title(new_data_list)
    final_data2 = check_createdAt(final_data1)
    final_data3 = check_author(final_data2)
    final_data4 = check_total_count(final_data3)
    final_data5 = check_tags(final_data4)
    generate_output(path2,final_data5)

if __name__ == '__main__':
    main()





