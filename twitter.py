import nltk, pprint
from nltk.twitter import Twitter
from nltk.twitter import Query, Streamer, Twitter, TweetViewer, TweetWriter, credsfromfile
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Rest API
from nltk.twitter import Twitter
tw = Twitter()
# tw.tweets(keywords='LokSabhaElection2019', limit=2)
tw.tweets(keywords='LokSabhaElection2019', stream=False, limit=20)


## Read tweets
oauth = credsfromfile()
f = open('E:/temp/twitter.txt', 'w')
client = Query(**oauth)
tweets = client.search_tweets(keywords='LokSabhaElection2019', limit=10000)
# tweet = next(tweets)
# pprint(tweet['text'], depth=1)

for tweet in tweets:
    print(tweet['text'])
    try:
        f.write(tweet['text'])
    except:
        print(' could not be printed', tweet['text'])
f.close()



## Read tweets and analyze
f = open('E:/temp/twitter.txt', 'r')
stopwords = set(nltk.corpus.stopwords.words('english'))
lines = f.readlines()
data_nostop = ''
for line in lines:
    print(line)
    for word in line.split():
        if word.lower() not in stopwords and word.isalpha():
            data_nostop += ' ' + word

word_toekn = nltk.word_tokenize(data_nostop)
fdist = nltk.FreqDist(word_toekn)
# Print word freq
fdist.plot(15, cumulative = True)

# plot the WordCloud image
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                min_font_size = 10).generate(data_nostop)


plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0)  
plt.show()
