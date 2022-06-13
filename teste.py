import csv
import emoji
import advertools as adv
from emosent import get_emoji_sentiment_rank
import re

emojis=dict()
result=dict()

def extract_emojis(s):
  return ''.join(c for c in s if c in emoji.UNICODE_EMOJI['pt'])

def convert_emojis(text):
    for emot in emoji.UNICODE_EMOJI['pt']:
        text = re.sub(r'('+emot+')', "_".join(emoji.UNICODE_EMOJI['pt'][emot].replace(",","").replace(":","").split()), text)
    return text


with open('Tweets_pt_pt.csv', 'r',encoding="utf-8") as file:
   reader = csv.DictReader(file, skipinitialspace=True)
   aux=0
   for l in reader:
     aux+=1
     has_emoji = bool(emoji.get_emoji_regexp().search(l['tweet_text']))
     if(has_emoji):
       emojis[str(l['id'])]=str(l['tweet_text'])
     if(aux==10000):
       break 

for key, value in emojis.items():
  result[str(key)]=extract_emojis(value)
  convert_emojis(result[str(key)])
  break

#print(result)

print(get_emoji_sentiment_rank(result['1031627864658071552']))
for k in get_emoji_sentiment_rank(result['1031627864658071552']):
  print(k)
#print(emojis['1031565375429861377'])