#!/bin/env python

import urllib2, json, time, re

dataLoc = "/home/ric/dev/stocks/python/data/"

def getPrice(lastTime = ""):
    """Function to get price"""

    url = "http://finance.google.com/finance/info?client=ig&q=LON:BA"
    txt = urllib2.urlopen(url).read()
    js = json.loads(txt[3:])[0]
#    print(js)
#    for x in js.keys():
#        print(str(x))
    changeTime = str(js["lt_dts"])
    if lastTime != changeTime:
        price = float(js["l"])
        return (changeTime, price)
    else:
        print("No change in price")

def toFile(results):
    with open(dataLoc + "data.csv", "a") as f:
        time, price = results
        time = re.sub(r"[A-Z]", " ", time).strip()
        f.write("{0},{1}\n".format(time, price))
    f.close

t, p = getPrice()
toFile((t, p))
print((t, p))

while time.localtime().tm_hour < 18:
    tup = getPrice(t)
    if tup:
        print(tup)
        toFile(tup)
        t = tup[0]
    time.sleep(30)
