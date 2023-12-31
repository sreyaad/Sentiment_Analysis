# -*- coding: utf-8 -*-
"""Sentiment_Analysis.ipynb"""

import pandas as pd
data=pd.read_csv("/content/IMDB Dataset.csv")

data.head()

data['sentiment'].value_counts()

"""Importing Libraries Necessary"""

import seaborn as sns
import matplotlib.pyplot as plt
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelBinarizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from wordcloud import WordCloud, STOPWORDS
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize,sent_tokenize

import spacy
import re,string,unicodedata
from nltk.stem import WordNetLemmatizer,LancasterStemmer
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from textblob import TextBlob
from textblob import Word
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score
from bs4 import BeautifulSoup

import nltk
nltk.download("stopwords")

#Tokenizing text
from nltk.tokenize.toktok import ToktokTokenizer

tokenizers=ToktokTokenizer()
stopwords=nltk.corpus.stopwords.words('english')

#Remove noisy text
def noiseremoval(text):
  soup=BeautifulSoup(text,"html.parser")
  text=soup.get_text()
  text=re.sub('\[[^]]*\]','',text)
  return text

data['review']=data['review'].apply(noiseremoval)

"""**Stemming**"""

def stemmer(text):
  ps=nltk.porter.PorterStemmer()
  text=' '.join([ps.stem(word) for word in text.split()])
  return text

data['review']=data['review'].apply(stemmer)

data.head()

"""Stopwords Removal"""

def stoprem(text,is_lower_case=False):
  tokenizers=ToktokTokenizer()
  tokens=tokenizers.tokenize(text)
  tokens=[i.strip() for i in tokens]
  if is_lower_case:
    filtokens=[i for i in tokens if token not in stopwords]
  else:
    filtokens=[i for i in tokens if i.lower() not in stopwords]
  filtered_texts=' '.join(filtokens)
  return filtered_texts

data['review']=data['review'].apply(stoprem)

data.head()

"""Bag of Words"""

norm_train_reviews=data.review[:40000]
norm_train_reviews[0]

norm_test_reviews=data.review[40000:]
norm_test_reviews[45005]

cv=CountVectorizer(min_df=0,max_df=1,binary=False,ngram_range=(1,3))
cv_train=cv.fit_transform(norm_train_reviews)

cv_test=cv.transform(norm_test_reviews)
print("BOW_Train",cv_train.shape)
print("BOW_Test",cv_test.shape)

"""TF-IDF"""

tf=TfidfVectorizer(min_df=0,max_df=1,use_idf=True,ngram_range=(1,3))
tf_train=tf.fit_transform(norm_train_reviews)

tf_test=tf.transform(norm_test_reviews)
print("TF_Train",tf_train.shape)
print("TF_Test",tf_test.shape)

"""Label Encoding"""

label=LabelBinarizer()
sentiment_data=label.fit_transform(data['sentiment'])
print(sentiment_data.shape)

train_data=data.sentiment[:40000]

test_data=data.sentiment[40000:]

"""Training the Model"""

logistic=LogisticRegression(penalty='l2',max_iter=500,C=1,random_state=42)
lr_bow=logistic.fit(cv_train,train_data)

print(lr_bow)

lr_tfidf=logistic.fit(tf_train,train_data)
print(lr_tfidf)

bow_predict=logistic.predict(cv_test)
print(bow_predict)
tfidf_predict=logistic.predict(tf_test)
print(tfidf_predict)

"""Predicting Accuracy of both Models"""

lr_bow_score=accuracy_score(test_data,bow_predict)

print(lr_bow_score)

tfidf_score=accuracy_score(test_data,tfidf_predict)

print(tfidf_score)
