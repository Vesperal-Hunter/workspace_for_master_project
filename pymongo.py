#! /usr/bin/env python
import numpy as np
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 62345)
#get the right timepointfirst
db = client['roslog']
monitordata =db['monitored_nav_events']
timepoints =[]

for data in monitordata.find():
    data['event_start_time']['secs']
    timepoints.append(data['event_start_time']['secs'])

#the function to got the fist struck timepoits
def del_interval(l):
    index_record=[0]

    for ind in xrange(len(l)-1):
        if l[ind+1]-l[ind]>1:
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
for data in costmap.find():
    for i in arrage(len(rtps))
        if data['header']['stamp']['secs'] - rtps[i] < 60:






    maplist = np.array(data['data'])
    costmapdata.append(maplist.reshape((80, 80)))


# cmexap = costmap.find_one()
# costmapdata = cmexap['data']
# costmapdata_m = np.array(costmapdata)
# shape = (80,80)
# costmapdata_m.reshape(shape)


