import csv
path1 = "/Users/alain/Desktop/hw4/further_new_dataset.csv"
path2 = "/Users/alain/Desktop/hw4/allzipcode.csv"
csv_data = []
with open(path1, 'r', encoding='utf-8') as f:
    csvreader = csv.reader(f)
    for line in csvreader:
        if line[3] == "83":
            line[3] = "00083"
        if [line[3]] not in csv_data:
            csv_data.append([line[3]])
f.close()
print(csv_data)
with open(path2, 'w', encoding='utf-8') as wf:
     writer = csv.writer(wf)
     writer.writerows(csv_data)
wf.close()