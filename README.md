# Sentiment_Analysis
This is a Natural Language Processing Project based on IMDB Dataset.
- This project identifies negative and positive sentiments among viewers .
- First, we cleaned the data by performing tokenization, removal of html tags and noise texts, text stemming, and removal of stopwords.
- We used Bag of Words model to convert text documents to numerical vectors of Bag of Words.
- Then We used Term Frequency-Inverse Document Frequency model (TFIDF) to convert text documents to matrix of tfidf features.
- Finally We did Label Encoding using LabelBinarizer before training the model.

## Model Used-
We used Logistic Regression to train our model.
- We split the data in the ratio of 4:1 where we used 40000 data for training and 10000 data for testing the model.

## Accuracy-
Both Bag of Words and Tf-idf showed almost similar accuracy of 75% using Logistic Regression.

## Future Works-
We can still improve the accuracy of the models by preprocessing data and by using lexicon models like Textblob.
