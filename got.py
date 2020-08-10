import pandas as pd
import GetOldTweets3 as got

def tweets1(username, top_only, start_date, end_date, max_tweets):
   
    # specifying tweet search criteria 
    tweetCriteria = got.manager.TweetCriteria().setUsername(username).setTopTweets(top_only).setSince(start_date).setUntil(end_date) \
        .setMaxTweets(max_tweets)
    
    # scraping tweets based on criteria
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    
    # creating list of tweets with the tweet attributes 
    text_tweets = [[tweet.username,
                tweet.text,
                tweet.date,
                tweet.retweets,
                tweet.favorites,
                tweet.mentions,
                tweet.hashtags] for tweet in tweets]
    
    # creating dataframe, assigning column names to list of
    # tweets corresponding to tweet attributes
    news_df = pd.DataFrame(text_tweets, 
                            columns = ['User', 'Text','Date', 'Favorites', 'Retweets', 'Mentions', 'HashTags'])
    
    return news_df

news = tweets1(['nytimes', 'bbcbreaking', 'bbcnews', 'bbcworld', 'theeconomist', 'reuters','HindustanTimes', 'financialtimes', 'guardian'], 
                     top_only = True,
                     start_date = "2020-06-07", 
                     end_date = "2020-07-1",
                    max_tweets = 100).sort_values('Date')





