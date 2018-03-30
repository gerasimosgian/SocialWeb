# SocialWeb 

Social Web(X_405086) - Group 13

# Project : Applying Sentiment Analysis to Investigate the Relation Between Public Opinion and Stock Market Performance

In this project we apply sentiment analysis to extracted tweets containing hashtags('#Novartis', '#Novartis_Gate') related to Novartis and the bribal scandals the company is being accused of. Then we visualize the sentiment score for the given period(the same as the extracted tweets) and compare it to the price of Novartis' stock for the same time. 

*Important Note: This is a university project. By no means we accuse Novartis or any other business of being guilty. This is clearly out of our scope. All related data was collected from social-media and press, and thus it is an opinion expressed by users of social media and press(and not our personal opinion)*

# Extracting Tweets

For tweet Extraction we used two methods : twarc(https://github.com/DocNow/twarc) and the script "TweetsExtraction.py".

# Performing Sentiment Analysis

For performing the sentiment analysis, we used the "TweetSentimentAnalysis.py" script.

# Visualization

We used python's library matplotlib (scripts : "plotsentiment.py", "plotstockprices.py")

# Limitations

Language - All tweets were used, were written in english language. In order to have a more sophisticated view, tweets written in other language should also be taken into consideration

Twitter API - Twitter API sets users restriction(in terms of time) to extracting tweets

Stockmarket - The stockmarket is being characterised by a different attitude, and using just Twitter's data could be a bias
