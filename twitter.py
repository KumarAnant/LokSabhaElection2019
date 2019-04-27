import nltk, pprint
from nltk.twitter import Twitter
from nltk.twitter import Query, Streamer, Twitter, TweetViewer, TweetWriter, credsfromfile
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import seaborn as sns

#Rest API
from nltk.twitter import Twitter
tw = Twitter()
# tw.tweets(keywords='LokSabhaElection2019', limit=2)
tw.tweets(keywords='LokSabhaElection2019', stream=False, limit=20)


## Read tweets
totaltweets = 0
oauth = credsfromfile()
client = Query(**oauth)
f = open('E:/temp/twitter.txt', 'w')
tweets = client.search_tweets(keywords='LokSabhaElection2019', limit=10000)
for tweet in tweets:
    print(tweet['text'])
    try:
        f.write(tweet['text'])
        totaltweets += 1
    except Exception: 
        pass
f.close()

f = open('E:/temp/twitter.txt', 'a')
oauth = credsfromfile()
client = Query(**oauth)
tweets = client.search_tweets(keywords='Elections2019', limit=10000)
for tweet in tweets:
    print(tweet['text'])
    try:
        f.write(tweet['text'])
        totaltweets += 1
    except Exception: 
        pass
f.close()

f = open('E:/temp/twitter.txt', 'a')
oauth = credsfromfile()
client = Query(**oauth)
tweets = client.search_tweets(keywords='FestivalOfDemocracy', limit=10000)
for tweet in tweets:
    #print(tweet['text'])
    try:
        f.write(tweet['text'])
        totaltweets += 1
    except Exception: 
        pass
f.close()




## Read tweets and analyze
f = open('E:/temp/twitter.txt', 'r')
stopwords = set(nltk.corpus.stopwords.words('english'))
lines = f.readlines()
data_nostop = ''
## Line tokenize for sentiment analysis
for line in lines:
    lines_list += nltk.sent_tokenize(line)

comp_score = []
neg_score = []
neu_score = []
pos_score = []

sid = nltk.sentiment.vader.SentimentIntensityAnalyzer()
for sentence in lines_list:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        #print('{0}: {1}, '.format(k, ss[k]), end='')
        comp_score.append(ss['compound'])
        neg_score.append(ss['neg'])
        neu_score.append(ss['neu'])
        pos_score.append(ss['pos'])
len(neu_score)

# fig, ax = plt.subplots()
## Neutral snetiment plot
plt.figure(figsize = (30, 20), linewidth = 1)
sns.set(font_scale = 2)
g = sns.distplot(neu_score, rug = True, bins = 5, kde = False)
g.set(xlim = (-0.01, 1))
plt.xlabel('Neutral Sentiment score')
plt.ylabel('Count')
plt.title('Election 2019 Neutral Sentiments\t(Tweets Sample = {})\n'.format(totaltweets))
plt.xticks([0.1, 0.3, 0.5, 0.7, 0.9])
plt.show()

## Positive snetiment plot
plt.figure(figsize = (30, 20), linewidth = 20)
sns.set(font_scale = 2)
g = sns.distplot(pos_score, rug = True, bins = 5, color='g', kde = False)
g.set(xlim = (-0.01, 1))
plt.xlabel('Positive Sentiment score')
plt.ylabel('Count')
plt.title('Election 2019 Positive Sentiments\t(Tweets Sample = {})\n'.format(totaltweets))
plt.xticks([0.1, 0.3, 0.5, 0.7, 0.9])
plt.show()

## Negative snetiment plot
plt.figure(figsize = (30, 20), linewidth = 20)
sns.set(font_scale = 2)
g = sns.distplot(neg_score, rug = True, bins = 5, color='r', kde = False)
g.set(xlim = (-0.01, 1))
plt.xlabel('Negative Sentiment score')
plt.ylabel('Count')
plt.title('Election 2019 Negative Sentiments\t(Tweets Sample = {})\n'.format(totaltweets))
plt.xticks([0.1, 0.3, 0.5, 0.7, 0.9])
plt.show()


## Word tokenize and processing
for line in lines:
    #print(line)
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
