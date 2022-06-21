import csv
import pprint
import emoji
import advertools as adv
from emosent import get_emoji_sentiment_rank
import re
import pickle
import emoji
from emot.emo_unicode import UNICODE_EMOJI
from emot.emo_unicode import EMOTICONS_EMO
import pandas as pd

emojis=dict()
result=dict()
emoticons=dict()
taxonomia=dict()
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

with open('Emoticon_Dict.p', 'rb') as fp:
    Emoticon_Dict = pickle.load(fp)

def find_emoticons(text):
    emoticon_pattern = re.findall(u'(' + u'|'.join(k for k in Emoticon_Dict) + u')',text)
    aux=[]
    for elem in emoticon_pattern:
      elem = elem.replace('-','')
      if elem != ')':
        aux.append(str(elem))
    return aux

def extract_emojis(s):
  return ''.join(c for c in s if c in emoji.UNICODE_EMOJI['pt'])

def convert_text_to_emojis(text):
  return emoji.emojize(text,language='pt')

def convert_emojis_to_text(text):
  return emoji.demojize(text, language='pt')

def convert_emoticons_to_emoji(text):
  words = text.split(" ")
  outcome = " "
  for word in words:
    outcome += rawEmojis.get(word, word) + " "
  return(outcome)

def convert_emoticons_to_text(text):
  return emoji.demojize(convert_emoticons_to_emoji(text))

def find_taxonomia(text):
  result=dict()
  aux=extract_emojis(text)
  for emoj in aux:
    taxonomia[emoj]= adv.emoji_search(emoj)['group'][0]
  return result

with open('Tweets_pt_pt.csv', 'r',encoding="utf-8") as file:
  tweets = csv.DictReader(file, skipinitialspace=True)
  aux=0
  for tweet in tweets:
    aux+=1
    mojis = extract_emojis(convert_emoticons_to_emoji(tweet["tweet_text"]))
    for elem in mojis:
      emojis[elem] = [{'taxonomia': adv.emoji_search(elem)['group'][0]},
        {'emoji em texto': convert_emojis_to_text(elem)}]
      try:
        a=get_emoji_sentiment_rank(elem)
        emojis[elem].append({'sentimento': a['sentiment_score'],'positividade': a['positive'], 'neutral': a['neutral'], 'negatividade': a['negative']})
      except:
        emojis[elem].append(('sentimento', 'NA'))
df = pd.DataFrame(data=emojis)
df = df.fillna(' ').T
with open('output.html', 'w') as f:
    f.write(df.to_html())

    #if(find_emoticons(tweets['tweet_text'])!=[]):
      #emoticons[str(l['id'])]=find_emoticons(l['tweet_text'])
    #has_emoji = bool(emoji.get_emoji_regexp().search(l['tweet_text']))
    #if(has_emoji):
    #  emojis[str(l['id'])]=str(l['tweet_text'])
    if(aux==3000):
      pprint.pprint(emojis)
      break 

#for key, value in emojis.items():
#  result[str(key)]=extract_emojis(value)
#  for emoj in result[str(key)]:
#    taxonomia[emoj]= adv.emoji_search(emoj)['group'][0]

#for k,v in emoticons.items():
#  for elem in v:
#    elem=convert_emoticons_to_emoji(elem)