import gensim
import emoji
import csv
import re
from gensim.models import Word2Vec 


def convert_emoticons_to_emoji(text):
  words = text.split(" ")
  outcome = " "
  for word in words:
    outcome += rawEmojis.get(word, word) + " "
  return(outcome)

rawEmojis = {
  ":)" : "😀",
  "=)" : "😀",
  ":(" : "😞",
  ":D" : "😄",
  ":/" : "😕",
  ":'(": "😢",
  ":P" : "😛",
  "XD" : "😆",
  ":3" : "🐱",
  "DX" : "😫",
  "d:" : "😦",
  "XP" : "😝",
  "D8" : "😱",
  ":o" : "😯"
}

f2=open("tweets.txt",'w')

with open('Tweets_pt_pt.csv', 'r',encoding="utf-8") as file:
    aux=0
    tweets = csv.DictReader(file, skipinitialspace=True)  
    for tweet in tweets:
        aux+=1
        #tweet["tweet_text"]=re.sub('[)]{2,}',')',tweet["tweet_text"])
        #tweet["tweet_text"]=re.sub('[(]{2,}',')',tweet["tweet_text"])
        #tweet["tweet_text"]=re.sub('@(.)*\s','',tweet["tweet_text"])
        #tweet["tweet_text"]=re.sub('https:(.)*(\s|/\n/)?','',tweet["tweet_text"])
        t = emoji.demojize(convert_emoticons_to_emoji(tweet["tweet_text"]),language='pt')
        f2.write(t+'\n')
f2.close()

file=open("tweets.txt",encoding="utf-8")

frases=[]
for line in file:
    frases.append(list(gensim.utils.tokenize(line, lower=True)))

model = Word2Vec(sentences=frases,sg=0, workers=5, epochs=20, vector_size=100)

def semelhantes(emo):
  aux=[]
  a = emoji.demojize(emo, language='pt')
  b = re.sub(':','',a)
  res=model.wv.most_similar(b)
  for (a,c) in res:
    a = ":" + a + ":"
    a=emoji.emojize(a,language='pt')
    a=re.sub(':','',a)
    aux.append((a,c))
  return aux

print(semelhantes('😀'))