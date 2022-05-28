import datetime
import csv

from bokeh.layouts import row
from bokeh.models import CustomJS, ColumnDataSource, Select, Column, Row
from bokeh.plotting import figure, show, curdoc, output_file

path = "/Users/alain/Desktop/hw4/further_new_dataset.csv"
path2 = "/Users/alain/Desktop/hw4/allzipcode.csv"

d = {}
hourlist = []
unique_list = []

data = {}
trim_data = {}
final_data = {}
t_list = [[],[],[],[],[],[],[],[],[],[],[],[]]
trim_t = []
with open(path2, 'r', encoding='utf-8') as f:
    csvreader = csv.reader(f)
    for line in csvreader:
        unique_list.append(line[0])
        data[line[0]] = [[],[],[],[],[],[],[],[],[],[],[],[]]
        trim_data[line[0]] = []
        final_data[line[0]] = {}
f.close()

def gethours(m1,m2,d1,d2,h1,h2,mm1,mm2,s1,s2,res1,res2):
    if res1 == "PM" and h1 < 12:
        h1 += 12
    if res2 == "PM" and h2 < 12:
        h2 += 12
    if res1 == "AM" and h1 >= 12:
        h1 -= 12
    if res2 == "AM" and h2 >= 12:
        h2 -= 12
    create_date = datetime.datetime(2020,m1,d1,h1,mm1,s1)
    close_date = datetime.datetime(2020,m2,d2,h2,mm2,s2)
    delta = close_date - create_date
    hours = delta.total_seconds() / 3600
    return hours

######## double trim data ############
with open(path, 'r', encoding='utf-8') as f:
    csvreader = csv.reader(f)
    for line in csvreader:
        hours = gethours(int(line[1][0:2]),int(line[2][0:2]),int(line[1][3:5]),int(line[2][3:5]),
                         int(line[1][11:13]),int(line[2][11:13]),int(line[1][14:16]),int(line[2][14:16]),
                         int(line[1][17:19]),int(line[2][17:19]),line[1][20:22],line[2][20:22])
        month = line[2][0:2]
        if month == "01":
            data[line[3]][0].append(hours)
            t_list[0].append(hours)
        if month == "02":
            data[line[3]][1].append(hours)
            t_list[1].append(hours)
        if month == "03":
            data[line[3]][2].append(hours)
            t_list[2].append(hours)
        if month == "04":
            data[line[3]][3].append(hours)
            t_list[3].append(hours)
        if month == "05":
            data[line[3]][4].append(hours)
            t_list[4].append(hours)
        if month == "06":
            data[line[3]][5].append(hours)
            t_list[5].append(hours)
        if month == "07":
            data[line[3]][6].append(hours)
            t_list[6].append(hours)
        if month == "08":
            data[line[3]][7].append(hours)
            t_list[7].append(hours)
        if month == "09":
            data[line[3]][8].append(hours)
            t_list[8].append(hours)
        if month == "010":
            data[line[3]][9].append(hours)
            t_list[9].append(hours)
        if month == "011":
            data[line[3]][10].append(hours)
            t_list[10].append(hours)
        if month == "012":
            data[line[3]][11].append(hours)
            t_list[11].append(hours)
for key in data.keys():
    value = data[key]
    for i in range(len(value)):
        if len(value[i]) != 0:
            avg = sum(value[i])/len(value[i])
            trim_data[key].append(avg)
        else:
            trim_data[key].append(0)

for i in range(len(t_list)):
    if len(t_list[i]) != 0:
        avg = sum(t_list[i])/len(t_list[i])
        trim_t.append(avg)
    else:
        trim_t.append(0)

######## create data_source #########
x = [1,2,3,4,5,6,7,8,9,10,11,12]
for key in final_data.keys():
    final_data[key]['x'] = x
    final_data[key]['y'] = trim_data[key]
final_data['all'] = {}
final_data['all']['x'] = x
final_data['all']['y'] = trim_t
data = final_data

myPlot = figure(title="2020 monthly monthly average incident create-to-closed time",
                x_axis_label="month",
                y_axis_label="monthly average incident create-to-closed time (in hours)")
source = ColumnDataSource(data['all'])
source1 = ColumnDataSource(data['11234'])
source2 = ColumnDataSource(data['11210'])
# myPlot.line(x, trim_t, Legend_label="all 2020 data", line_width = 2, color="green")
myPlot.line('x', 'y', line_width = 2, source = source, color = "blue", legend_label="all 2020 data")
myPlot.line('x', 'y', line_width = 2, source = source1, color = "red", legend_label="2020 data in zipcode 1")
myPlot.line('x', 'y', line_width = 2, source = source2, color = "green", legend_label="2020 data in zipcode 2")

callback1 = CustomJS(args = {'source': source1, 'data': data},
code = """source.data = data[cb_obj.value]; """)

callback2 = CustomJS(args = {'source': source2, 'data': data},
code = """source.data = data[cb_obj.value]; """)

select1 = Select(title = 'zipcode1', value = '11234', options = unique_list)
select1.js_on_change('value', callback1)
select2 = Select(title = 'zipcode2', value = '11210', options = unique_list)
select2.js_on_change('value', callback2)

layout = Row(select1,select2,myPlot)
# show(layout)
curdoc().add_root(row(select1,select2,myPlot))