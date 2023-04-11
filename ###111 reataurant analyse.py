###111 reataurant analyse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

df = pd.read_csv('restaurant_comments.csv')

df.drop(['restaurant_name', 'location'], axis=1, inplace=True)
df.dropna(inplace=True)

def preprocess_text(text):
    # Remove special characters
    text = re.sub('[^a-zA-Z0-9\s]', '', text)

    # Convert to lowercase
    text = text.lower()

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if not token in stop_words]
    text = ' '.join(tokens)

    return text

df['comment'] = df['comment'].apply(preprocess_text)

X_train, X_test, y_train, y_test = train_test_split(df['comment'], df['rating'], test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_bow = vectorizer.fit_transform(X_train)
X_test_bow = vectorizer.transform(X_test)

classifier = MultinomialNB()
classifier.fit(X_train_bow, y_train)

y_pred = classifier.predict(X_test_bow)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nAccuracy Score: {:.2f}%".format(accuracy_score(y_test, y_pred) * 100))
