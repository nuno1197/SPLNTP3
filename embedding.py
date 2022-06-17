import gensim
import csv
from gensim.models import Word2Vec 

f2=open("tweets.txt",'w')

with open('Tweets_pt_pt.csv', 'r',encoding="utf-8") as file:
    tweets = csv.DictReader(file, skipinitialspace=True)  
    for tweet in tweets:
        f2.write(tweet['tweet_text']+'\n')
f2.close()

file=open("tweets.txt",encoding="utf-8")

frases=[]
for line in file:
    frases.append(list(gensim.utils.tokenize(line, lower=True)))

model = Word2Vec(sentences=frases,sg=0, workers=5, epochs=20, vector_size=100)

print(model.wv.most_similar("like"))