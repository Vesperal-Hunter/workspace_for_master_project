#! /usr/bin/env python
import numpy as np
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 62345)
#get the right timepointfirst
db = client['message_store']
monitordata =db['monitored_nav_events']
timepoints =[]

for data in monitordata.find():
    timepoints.append(data['event_start_time']['secs'])

#the function to got the fist struck timepoits
def del_interval(l):
    index_record=[0]
    for ind in xrange(len(l)-1):
        if l[ind+1]-l[ind]>60:
            index_record.append(ind+1)
    l2=[]
    for ind in index_record:
        l2.append(l[ind])
    return l2

rtps = del_interval(timepoints)

#get the maps which were stored 1m before the first struck timepoints
logdata =  client['roslog']
costmap = logdata['move_base_local_costmap_costmap']
costmapdata = []

for singletime in rtps:
    for data in costmap.find():
        if 0 < singletime - data['header']['stamp']['secs'] <60:
            costmapdata.append(data['data'])

#save the costmapda in csvfile
import csv
with open('costmapdata1to10.csv', 'wb') as csvfile:
    wb = csv.writer(csvfile, delimiter=',')
    wb.writerow(costmapdata1to10)


with open('costmapdata.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        testdata =  row
count = 0
c=[[]]
for i in testdata:
    for j in i:
        if j != '[' and j != ',' and j != ' ':
            if j == ']':
                count +=1
                c.append([])
            else:
                c[count].append(int(j))

del (c[len(c) - 1])


    maplist = np.array(data['data'])
    costmapdata.append(maplist.reshape((80, 80)))