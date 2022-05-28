#!/usr/bin/python
import csv
import json
import sys, getopt

opts,args = getopt.getopt(sys.argv, "hi:o:", [])
inputfile=args[3]
outputfile=args[2]

count_twilight_sparkle = 0
count_applejack = 0
count_rarity = 0
count_pinkie_pie = 0
count_rainbow_dash = 0
count_fluttershy = 0
num_of_Pony = -1
# abs_path = "/Users/alain/Desktop/hw3/submission_template/"+inputfile
with open(inputfile, 'r', encoding='utf-8') as f:
    csvreader = csv.reader(f)
    for line in csvreader:
        if line[2].lower() == "twilight sparkle":
            count_twilight_sparkle += 1
        if line[2].lower() == "applejack":
            count_applejack += 1
        if line[2].lower() == "rarity":
            count_rarity += 1
        if line[2].lower() == "pinkie pie":
            count_pinkie_pie += 1
        if line[2].lower() == "rainbow dash":
            count_rainbow_dash += 1
        if line[2].lower() == "fluttershy":
            count_fluttershy += 1
        num_of_Pony += 1;
f.close()

verbosity_twilight_sparkle = count_twilight_sparkle/num_of_Pony
verbosity_applejack = count_applejack/num_of_Pony
verbosity_rarity = count_rarity/num_of_Pony
verbosity_pinkie_pie = count_pinkie_pie/num_of_Pony
verbosity_rainbow_dash = count_rainbow_dash/num_of_Pony
verbosity_fluttershy = count_fluttershy/num_of_Pony

data={}
data["count"] = {
    "twilight sparkle" : count_twilight_sparkle,
    "applejack" : count_applejack,
    "rarity" : count_rarity,
    "pinkie pie" : count_pinkie_pie,
    "rainbow dash" : count_rainbow_dash,
    "fluttershy" : count_fluttershy}
data["verbosity"] = {
    "twilight sparkle" : verbosity_twilight_sparkle,
    "applejack" : verbosity_applejack,
    "rarity" : verbosity_rarity,
    "pinkie pie" : verbosity_pinkie_pie,
    "rainbow dash" : verbosity_rainbow_dash,
    "fluttershy" : verbosity_fluttershy
}

with open(outputfile, 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, indent=4)
outfile.close()

# The code below is just for verification
# sum=0
# fractions=0
# for i in data["count"]:
#     for j in i:
#         sum += i[j]
# for i in data["verbosity"]:
#     for j in i:
#         fractions += i[j]
# print(sum/num_of_Pony)
# print(fractions)