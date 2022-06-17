import gensim
import csv
from gensim.models.doc2vec import TaggedDocument, Doc2Vec 

def train_model():
    with open('Tweets_pt_pt.csv', 'r',encoding="utf-8") as file:
        tweets = csv.DictReader(file, skipinitialspace=True)  
        documents = [TaggedDocument(text['tweet_text'].split(), [text['id']])  for text in tweets]
    model = Doc2Vec(documents, vector_size=100, window=8, min_count=2, workers=7)
    model.distance('😀','😄')
    return model


