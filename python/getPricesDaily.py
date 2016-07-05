#!/bin/env python

import urllib2, json, time, re

dataLoc = "/home/ric/dev/stocks/python/data/"
lastTimeDict = {}

def getPrice(ltDict, *codes):
    """Function to get price"""

    res = []
    tmp = ""
    for code in codes:
        tmp = tmp + "," + str(code)
    tmp = tmp[1:]
    url = "http://finance.google.com/finance/info?client=ig&q=" + tmp
    txt = urllib2.urlopen(url).read()
    jsArr = json.loads(txt[3:])
    for js in jsArr:
        changeTime = str(js["lt_dts"])
        stockId = str(js["e"]) + ":" + str(js["t"])
        if stockId not in ltDict or ltDict[stockId] != changeTime:
            price = float(js["l"])
            res.append((stockId, changeTime, price))
        else:
            print("No change in price")
    if res:
        return res

def toFile(results, stock):
    with open(dataLoc + stock + "_data.csv", "a") as f:
        time, price = results
        time = re.sub(r"[A-Z]", " ", time).strip()
        f.write("{0},{1}\n".format(time, price))
    f.close

for line in getPrice(lastTimeDict, "LON:BA", "LON:FDM"):
    sid, t, p = line
    toFile((t, p), sid)
    print((sid, t, p))
    lastTimeDict[sid] = t

while time.localtime().tm_hour < 18:
    lst = getPrice(lastTimeDict, "LON:BA", "LON:FDM")
    if lst:
        for tup in lst:
            print(tup)
            sid, t, p = tup
            toFile((t, p), sid)
            lastTimeDict[sid] = t
    time.sleep(30)
