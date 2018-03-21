from matplotlib import style
from matplotlib import pylab as plt
import numpy as np
import pandas as pd
import dateutil
import datetime
import csv
import matplotlib.dates as mdates

date1=[]
op=[]
cl=[]

with open('novstocks.csv', 'r') as prices:
	csvreader = csv.reader(prices)
	for row in csvreader:
		if len(row) ==3:
			date1.append(row[0])
			op.append(row[1])
			cl.append(row[2])

headers = ['Dates', 'Open', 'Close']
df1 = pd.read_csv('novstocks.csv', names = headers)
df1['Dates']=pd.to_datetime(df1['Dates'], format='%b-%d') #Convert the strings in the second column to datetime 
			
op=np.array(op)
cl=np.array(cl)			
		
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.plot(df1['Dates'], cl)
plt.plot(df1['Dates'], op)
plt.gcf().autofmt_xdate()

plt.xlabel('Date')
plt.title('Stock Prices')
plt.ylabel('Price is US Dollars')
			
plt.show()