from bokeh.layouts import column, row
from bokeh.plotting import figure
from bokeh.io import show
from bokeh.models import CustomJS, Dropdown
import csv

from bokeh.plotting import figure,show
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
p = figure(title="Simple line example", x_axis_label='x', y_axis_label='y')
p.line(x, y, legend_label="Temp.", line_width=2)

path = "/Users/alain/Desktop/hw4/allzipcode.csv"
unique_list = []
with open(path, 'r', encoding='utf-8') as f:
    csvreader = csv.reader(f)
    for line in csvreader:
        unique_list.append(line[0])
f.close()

menu = unique_list

dropdown1 = Dropdown(label="zipcode1", button_type="warning", menu=menu)
dropdown1.js_on_event("menu_item_click", CustomJS(code="console.log('dropdown: ' + this.item, this.toString())"))
dropdown2 = Dropdown(label="zipcode2", button_type="warning", menu=menu)
dropdown2.js_on_event("menu_item_click", CustomJS(code="console.log('dropdown: ' + this.item, this.toString())"))
def click(e):
    print(e.item)
dropdown1.on_click(click)
show(row(p,dropdown1,dropdown2))


