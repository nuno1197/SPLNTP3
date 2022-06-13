import re
import pickle
import emoji
from emot.emo_unicode import UNICODE_EMOJI
from emot.emo_unicode import EMOTICONS_EMO 

with open('Emoticon_Dict.p', 'rb') as fp:
    Emoticon_Dict = pickle.load(fp)

def find_emoticons(text):
    emoticon_pattern = re.findall(u'(' + u'|'.join(k for k in Emoticon_Dict) + u')',text)

    return emoticon_pattern

text = "I won 🥇 in 🏏  :) :("
print(str(find_emoticons(text)))
