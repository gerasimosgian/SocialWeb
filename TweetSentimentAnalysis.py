#-*- coding: utf-8 -*-
import json
import csv
from textblob import TextBlob
import itertools 
import simplejson

#Input and output files
input_file= "nov.json"
output_file="results.csv"

tweets_novartis = []

#Append the json file
with open (input_file) as input_novartis:
	for line in input_novartis:
		tweets_novartis.append(json.loads(line))

#parsing the text and date data 
with open(output_file, 'w', newline = '') as output_novartis:
	writer = csv.writer(output_novartis)

	for tweets_novartis in tweets_novartis:
		
		tweet = tweets_novartis["full_text"]
		lan = tweets_novartis["created_at"]
		
		#Sentiment Analysis
		tweet=TextBlob(tweet)
		
		tweet = tweet.replace("\n", " ")
		tweet = tweet.replace("\r", " ")
		def set_date(self, lan):
			date = time.striptime(lan, '%b %d %Y ')
			
			self.date = datetime.fromtimestamp(time.mktime(date))
		#Sentiment score
		sentiment=[tweet.sentiment.polarity]
		
		writer.writerows(zip(sentiment, [lan[4:10], lan[26:]]))
		
		
		
