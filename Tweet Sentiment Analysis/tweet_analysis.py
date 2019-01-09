import pandas as pd
import matplotlib.pyplot as polt
from textblob import TextBlob

# Reading tweets from csv file
df = pd.read_csv("gold.csv", encoding="ISO-8859-1")
# df = pd.read_csv("C:\\Users\\noopur\\Downloads\\keralaflood.csv",encoding = "ISO-8859-1")
raw_tweets = df.text
#print(raw_tweets)

tweets = []

for tweet in raw_tweets:
    # empty dictionary to store required params of a tweet
    structured_tweet = {}
    # saving text of tweet
    structured_tweet['text'] = tweet
#    print(structured_tweet)
    # saving sentiment of tweet
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        structured_tweet['sentiment'] = 'positive'
        structured_tweet['polarity'] = analysis.sentiment.polarity
    elif analysis.sentiment.polarity == 0:
        structured_tweet['sentiment'] = 'neutral'
        structured_tweet['polarity'] = analysis.sentiment.polarity
    else:
        structured_tweet['sentiment'] = 'negative'
        structured_tweet['polarity'] = analysis.sentiment.polarity
    tweets.append(structured_tweet)
 #   print(structured_tweet)
#print(tweets)
# Separating positive tweets from tweets
pos_tweets = [x for x in tweets if x['sentiment'] == 'positive']
#print(pos_tweets)
# % of positive tweets
print("Positive tweet {} %".format(100 * len(pos_tweets) / len(tweets)))
# Separating negative tweets from tweets
neg_tweets = [x for x in tweets if x['sentiment'] == 'negative']
# % of negative tweets
print("Negative tweets {} %".format(100 * len(neg_tweets) / len(tweets)))
# % of neutral tweets
print("Neutral tweets {} % ".format(100 * (len(tweets) - len(neg_tweets) - len(pos_tweets)) / len(tweets)))

ptext = []
ntext = []

for x in tweets:
    if x['polarity'] > 0.8:
        ptext.append(x['text'])

for x in tweets:
    if x['polarity'] < -0.7:
        ntext.append(x['text'])

# printing tweets
print("\n Positive tweets:")
print(ptext[:5])

print("\n Negative tweets:")
print(ntext[:5])


def print_worldcloud(words):
    from wordcloud import WordCloud
    word_cloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110).generate(words)
    polt.figure(figsize=(10, 7))
    polt.imshow(word_cloud, interpolation="bilinear")
    polt.axis('off')
    polt.show()


all_words = ' '.join([text for text in ptext])
print_worldcloud(all_words)

all_words = ' '.join([text for text in ntext])
print_worldcloud(all_words)