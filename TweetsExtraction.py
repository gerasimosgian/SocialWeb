#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contain the user credentials to access Twitter API 
access_token = "969164812310794242-uV56fg4mJfUAQlQkUx2vhOPDbhGzZ6V"
access_token_secret = "4QJxalTQOg66ZLtKaNGpXFOcXEocAWi7gFh1KlYxqRDpz" 
consumer_key = "bU3fiwthsZU1FtudNsAN6uiGn"
consumer_secret = "NNTG3iUTEGySOr8qP8Ya5OjalyYrJx84tQfycHyaefKoKxiWRR"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    #def on_error(self, status):
        #print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
   

    #This line filter Twitter Streams to capture data by the keyword'Novartis'
    stream.filter(track=['Novartis'], languages=["en"])
