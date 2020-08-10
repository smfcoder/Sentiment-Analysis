import string
from collections import Counter
import GetOldTweets3 as got
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sia
import matplotlib.pyplot as plt

def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('DonaldTrump') \
        .setSince("2020-01-01") \
        .setUntil("2020-08-8") \
        .setMaxTweets(700)
    # Creation of list that contains all tweets
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    # Creating list of chosen tweet data
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets



# reading text file
text = ""
text_tweets = get_tweets()
length = len(text_tweets)

for i in range(0, length):
    text = text_tweets[i][0] + " " + text

# converting to lowercase
lower_case = text.lower()

# Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# splitting text into words
tokenized_words = word_tokenize(cleaned_text, "english")

# Removing stop words from the tokenized words list
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

# Get emotions text
emotions = []
with open('emotion.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotions.append(emotion)

count = Counter(emotions)
print(count)

#visualising
fig, ax1 = plt.subplots()
ax1.bar(count.keys(), count.values())
fig.autofmt_xdate()
plt.show()


#PolarityScore:
def sentiment_analyze(cleaned_text1):
    score = sia().polarity_scores(cleaned_text1)
    if score['neg'] > score['pos']:
        print("Negative Sentiment")
    if score['neg'] < score['pos']:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")
    
    
sentiment_analyze(cleaned_text)


