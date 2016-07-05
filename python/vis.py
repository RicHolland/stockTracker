import csv
from datetime import datetime, date
from bokeh.plotting import figure, output_file, show

x = []
y = []

stock = "LON:BA"

with open("/home/ric/dev/stocks/python/data/" + stock + "_data.csv") as data:
    dd = csv.reader(data, delimiter=",")
    for row in dd:
        t, p = row
        #print "{0}\t{1}".format(t, p)
        x.append(datetime.strptime(t, "%Y-%m-%d %H:%M:%S"))
        y.append(p)
    # Add current time with last known price
    x.append(datetime.now())
    y.append(p)

today = date.today()
x_f = datetime(today.year, today.month, today.day, 8, 30)
x_l = datetime(today.year, today.month, today.day, 18)

plot = figure(title = stock, x_axis_type = "datetime", x_range = [x_f, x_l])
plot.line(x, y)

show(plot)

#for z in x:
    #print(z)
