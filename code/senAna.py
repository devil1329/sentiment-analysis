import tweepy as tp
import re
from textblob import TextBlob as tb
import pandas as pd
import matplotlib.pyplot as plt

#for clean text
def cleanText(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'RT[\s]+', '', text)
    text = re.sub(r'https?:\/\/\S+', '', text)
    text = re.sub(r': ','',text)
    return text

#subjectivity and polarity of the tweets
def getSubjectivity(text):
    return tb(text).sentiment.subjectivity

def getPolarity(text):
    return tb(text).sentiment.polarity

#it get  the analysis for the positive, negative and neutral tweets
def getAnalysis(score):
    if score < 0:
        return '-ve'
    elif score > 0:
        return '+ve'
    else:
        return '0'

def setData(a,b,c,d):
    apiKey = a
    apiKeySecret = b
    accessToken = c
    accessTokenSecret = d

    #api handler
    authHandler = tp.OAuthHandler(consumer_key=apiKey,consumer_secret=apiKeySecret)
    authHandler.set_access_token(accessToken,accessTokenSecret)

    api = tp.API(authHandler)

    #extract tweets from user
    posts = api.user_timeline(screen_name = "Vishnu",count = 100, lang = "en", tweet_modes = "extended")

    #create dataframe
    df = pd.DataFrame([tweet.text for tweet in posts], columns=['Tweets'])
    df['Tweets'] = df['Tweets'].apply(cleanText)

    df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
    df['Polarity'] = df['Tweets'].apply(getPolarity)

    #plot polarity and subjectivity
    plt.figure(figsize=(8,6))
    for i in range(0, df.shape[0]):
        plt.scatter(df['Polarity'][i],df['Subjectivity'][i], color='Blue')

    plt.title("SENTIMENT ANALYSIS")
    plt.xlabel('Polarity')
    plt.ylabel('Subjectivity')
    plt.show()

    df['Analysis'] = df['Polarity'].apply(getAnalysis)

    #plot and visalize the content
    df['Analysis'].value_counts()

    plt.title("SENTIMENT ANALYSIS")
    plt.xlabel('Sentiment')
    plt.ylabel('Polarity')
    df['Analysis'].value_counts().plot(kind='bar')
    plt.show()
    polarity = 0

    for i in df['Polarity']:
        polarity += i

    return df, polarity