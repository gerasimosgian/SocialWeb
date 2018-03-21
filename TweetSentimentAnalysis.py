#-*- coding: utf-8 -*-
import json
import csv
from textblob import TextBlob
from textblob.translate import Translator
import itertools 
import simplejson

input_file= "nov.json"
output_file="results.csv"

tweets_novartis = []

with open (input_file) as input_novartis:
	for line in input_novartis:
		tweets_novartis.append(json.loads(line))

with open(output_file, 'w', newline = '') as output_novartis:
	writer = csv.writer(output_novartis)

	for tweets_novartis in tweets_novartis:
		
		tweet = tweets_novartis["full_text"]
		lan = tweets_novartis["created_at"]
		
		tweet=TextBlob(tweet)
		
		tweet = tweet.replace("\n", " ")
		tweet = tweet.replace("\r", " ")
		def set_date(self, lan):
			date = time.striptime(lan, '%b %d %Y ')
			
			self.date = datetime.fromtimestamp(time.mktime(date))
		sentiment=[tweet.sentiment.polarity]
		
		writer.writerows(zip(sentiment, [lan[4:10], lan[26:]]))
		
		
		
