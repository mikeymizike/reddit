import praw
from tqdm import tqdm
from datetime import datetime
import pandas as pd

#### Reddit login and API connection ####

# Your login details
username = 'USERNAME'
password = 'PASSWORD'

# Your app details
user_agent = 'bot'
client_id = 'CLIENT_ID'
client_secret = 'CLIENT_SECRET'

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password)

# create a loop to scrape and store data from reddit continuously
i = 0
reddit_df = pd.DataFrame(columns=['Time & Date', 'URL', 'body'])
reddit_df.to_csv('reddit_data.csv')
for comment in tqdm(reddit.subreddit("wallstreetbets").stream.comments()):
    if i%500==0:
        reddit_df.loc[i] = [datetime.fromtimestamp(comment.created_utc),comment.permalink,comment.body]
        reddit_df.to_csv('reddit_data.csv', mode='a', header=False)
        reddit_df = pd.DataFrame(columns=['Time & Date', 'URL', 'body'])
    else:
        reddit_df.loc[i] = [datetime.fromtimestamp(comment.created_utc),comment.permalink,comment.body]
    i+=1
