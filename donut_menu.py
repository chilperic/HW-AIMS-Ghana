#!/usr/bin/env python
import json
'''
To load data from the donuts.json and combination of donuts, batters, and (single) toppings

'''

#open donuts.json

with  open("donuts.json") as donutsData:
	donutsData = json.load(donutsData)

#reading file content
for i in range(len(donutsData)):
  # Looping through batter and toppings for each donut
   for n in range(len(donutsData[i]['batters']['batter'])):
	print '\n#',n+1,' Available Toppings for ', donutsData[i]['batters']['batter'][n]['type'],donutsData[i]['name'],'Donut\n' 

        for k in range(len(donutsData[i]['topping'])):
   		print k+1,': ',donutsData[i]['topping'][k]['type']



