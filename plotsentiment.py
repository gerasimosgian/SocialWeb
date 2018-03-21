from matplotlib import style
from matplotlib import pylab as plt
import numpy as np
import pandas as pd
import dateutil
import datetime
import csv
import matplotlib.dates as mdates

filename='results.csv'
value=[]
date=[]


with open(filename, 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	for row in csvreader:
		if len(row) ==2:
			value.append(row[0])
			date.append(row[1])

value=np.array(value)

headers = ['Value', 'Date']
df = pd.read_csv('results.csv', names = headers)

#Processing results.csv 
df['Date']=pd.to_datetime(df['Date'], format='%b %d') #Convert the strings in the second column to datetime 
date=df.set_index('Date').groupby(pd.TimeGrouper('d')).mean() #Calculate the mean of polarity for each day


plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.plot(date)
plt.gcf().autofmt_xdate()

plt.xlabel('Date')
plt.title('User Sentiment')
plt.ylabel('Sentiment Score')

plt.show()