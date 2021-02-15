#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from tqdm import tqdm
securities = pd.read_csv('optionable securities.csv')
securities = securities['Symbol'].tolist()


# In[111]:


comments_df = pd.read_csv('reddit_data.csv').set_index('Time & Date').drop(columns=['Unnamed: 0']).sort_values(by='Time & Date', ascending=False)
comments = comments_df['body'].tolist()
tickers= []
for x in tqdm(range(0, len(comments))):
    words = comments[x].split()
    for word in words:
        if word.isupper():
            for i in range(0, len(securities)):
                if securities[i] == word:
                    tickers.append(word)


# In[112]:


pd.Series(tickers).value_counts().drop(['DD','A','USD', 'YOLO', 'ITM','CEO'])#[0:25]






