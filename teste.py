import csv
import emoji
import advertools as adv
from emosent import get_emoji_sentiment_rank
import re
import pickle
import emoji
from emot.emo_unicode import UNICODE_EMOJI
from emot.emo_unicode import EMOTICONS_EMO 

emojis=dict()
result=dict()
emoticons=dict()
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

def convert_emoticons_to_emoji(text):
  words = text.split(" ")
  outcome = " "
  for word in words:
    outcome += rawEmojis.get(word, word) + " "
  return(outcome)

def convert_emoticons_to_text(text):
  return emoji.demojize(convert_emoticons_to_emoji(text))

with open('Tweets_pt_pt.csv', 'r',encoding="utf-8") as file:
  reader = csv.DictReader(file, skipinitialspace=True)
  aux=0
  for l in reader:
    aux+=1
    if(find_emoticons(l['tweet_text'])!=[]):
      emoticons[str(l['id'])]=find_emoticons(l['tweet_text'])
    has_emoji = bool(emoji.get_emoji_regexp().search(l['tweet_text']))
    if(has_emoji):
      emojis[str(l['id'])]=str(l['tweet_text'])
    if(aux==10000):
       break 

for key, value in emojis.items():
  result[str(key)]=extract_emojis(value)

for k,v in emoticons.items():
  for elem in v:
    elem=convert_emoticons_to_emoji(elem)
    print(elem)
