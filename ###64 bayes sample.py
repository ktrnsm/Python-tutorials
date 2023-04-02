###64 bayes sample
#import chardet
#with open(r"C:\Users\Şebnem\Desktop\tutorials\spam.csv", "rb") as f:
#    result = chardet.detect(f.read())

#print(result)


import pandas as pd
import matplotlib.pylab as plt
import re
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import numpy as np

original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/spam.csv",encoding="Windows-1252")
data=original_data.copy()
#print(data)
data=data.drop(columns=["Unnamed: 2","Unnamed: 3","Unnamed: 4"],axis=1)
data=data.rename(columns={"v1":"Tag","v2":"SMS"})
#print(data)
#print(data.groupby("Tag").count())

data=data.drop_duplicates()
#print(data.describe())
#print(data.isnull().sum())

data["number of characters"]=data["SMS"].apply(len)
#print(data)
#data.hist(column="number of characters",by="Tag",bins=50)
#plt.show()

data.Tag=[1 if code=="spam" else 0 for code in data.Tag]
#print(data)

message=re.sub("[^a-zA-Z]"," ",data["SMS"][0])
#print(data["SMS"][0])
#print(message)

def letters(sentence):
    location=re.compile("[^a-zA-Z]")
    return re.sub(location," ",sentence)

#print(letters("tuy,,?RTF11"))
stopping=stopwords.words("english")
#print(stopping)

spam=[]
ham=[]
all_sentences=[]

for i in range(len(data["SMS"].values)):
    r1=data["SMS"].values[i]
    r2=data["Tag"].values[i]

    clean_sentence=[]
    sentences=letters(r1)
    sentences=sentences.lower()

    for words in sentences.split():
        clean_sentence.append(words)

        if r2==1:
            spam.append(sentences)
        else:
            ham.append(sentences)
    
    all_sentences.append(" ".join(clean_sentence))

data["New SMS"]=all_sentences
data=data.drop(columns=["SMS","number of characters"],axis=1)
#print(data)

cv=CountVectorizer()
x=cv.fit_transform(data["New SMS"]).toarray()

y=data["Tag"]
X=x

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=MultinomialNB(alpha=0.1)
model.fit(X_train,y_train)
prediction=model.predict(X_test)

acs=accuracy_score(y_test,prediction)

for i in np.arange(0.0,1.1,0.1):
    model=MultinomialNB(alpha=i)
    model.fit(X_train,y_train)
    prediction=model.predict(X_test)
    score=accuracy_score(y_test,prediction)
    print("Alfa Value:{} Score:{}".format(round(i,1),round(score*100,2)))
