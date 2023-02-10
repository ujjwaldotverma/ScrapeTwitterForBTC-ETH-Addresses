#dependency import
import snscrape.modules.twitter as sntwitter
import pandas as pd
import re

#the actual query/account from which you need to take the tweets from
query = "(from:anciliainc)"
tweets = []

#limit of tweets taken at a time from the top
limit = 10

#RE for ETH address
re1 = "0x[a-fA-F0-9]{40}"

#RE for BTC address
re2 = "[13][a-km-zA-HJ-NP-Z1-9]{25,34}"
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets)==limit:
        break
    else:
        x=[]
        row = str(tweet.content)
        all_match = re.compile("(%s|%s)" % (re1, re2)).findall(row) 
        for match in all_match:
            #print(match)
            x.append(match)
        print(x)
        tweets.append([tweet.date, tweet.username, tweet.content, all_match])
   

df = pd.DataFrame(tweets, columns=['Date','User','Tweet','Address'])

#if you need to transfer the output to a .csv file.
#df.to_csv("Addresses.csv")


print(df)
