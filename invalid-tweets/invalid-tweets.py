import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets_where_content_length_is_greater_than_15 = tweets[tweets["content"].str.len() > 15]
    ans = tweets_where_content_length_is_greater_than_15[['tweet_id']]
    return ans
