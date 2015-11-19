import tweepy, os, sys

#Twitter API credentials

access_key = "1366884128-bimgAM9nBQMalVXnwRBJn3J06xyRSdhOa9zZSlD"
access_secret = "XDL6kiLcZSePRMSqaEs8gJTS8T0bt4YMvX6xZesdPuzNB"
consumer_key = "55KFXSirWyaqXSDnxYVbS9S2B"
consumer_secret = "Wycg3x5vibEXK2ZQhO08dGIcAATeGIMXZnWApswzDUx11Unghk"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
fo = open('FollowerList.txt', "a+")
txt = "list.txt"

with open(txt) as f:
    content = f.readlines()

for user in tweepy.Cursor(api.followers, screen_name=content).items():

    print user.screen_name
    content = "%s\n" % user.screen_name
    fo.write(content);

fo.close()