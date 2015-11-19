import tweepy, os, sys, time

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

c = tweepy.Cursor(api.followers,scren_name=content).items()

while True:
    try:
        user = c.next()
        print user.screen_name
        content = "%s\n" % user.screen_name
        fo.write(content);
    except tweepy.TweepError:
        print "Tweepy Rate Limit exceeded, waiting for 15 min..."
        time.sleep(60 * 15)
        continue
    except StopIteration:
        break

fo.close()
