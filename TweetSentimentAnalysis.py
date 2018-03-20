import json
import csv
from textblob import TextBlob


#set the input and outputing file
input_file= "tweets.json"
output_file= "results.csv"

#store all json data
tweets_novartis = []

with open (input_file) as input_novartis:
    for line in input_novartis:
        tweets_novartis.append(json.loads(line))

#open output file to store the results
with open(output_file, "w") as output_novartis:
    writer = csv.writer(output_novartis)

    #iterate through all the tweets
    for tweets_novartis in tweets_novartis:
        tweet = tweets_novartis["full_text"]

        #TextBlob to calculate sentiment
        sentiment = [[TextBlob(tweet).sentiment.polarity]]
        writer.writerows(sentiment)

