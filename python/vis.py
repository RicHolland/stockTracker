import csv
from datetime import datetime
from bokeh.plotting import figure, output_file, show

x = []
y = []

with open("/home/ric/dev/stocks/python/data.csv") as data:
    dd = csv.reader(data, delimiter=",")
    for row in dd:
        t, p = row
        print "{0}\t{1}".format(t, p)
        x.append(datetime.strptime(t, "%Y-%m-%d %H:%M:%S"))
        y.append(p)

plot = figure(title = "BAE", x_axis_type = "datetime")
plot.line(x, y)

show(plot)

for z in x:
    print(z)
