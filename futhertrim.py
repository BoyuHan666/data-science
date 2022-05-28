import csv
import datetime
path = "/Users/alain/Desktop/hw4/过程/filtered.csv"
path2 = "/Users/alain/Desktop/hw4/further_new_dataset.csv"
count = 0
csv_data=[]
with open(path, 'r', encoding='utf-8') as f:
    csvreader = csv.reader(f)
    for line in csvreader:
        if count != 0:
            csv_data.append(line)
        count += 1
print(len(csv_data))
with open(path2, 'w', encoding='utf-8') as wf:
    writer = csv.writer(wf)
    writer.writerows(csv_data)
wf.close()
