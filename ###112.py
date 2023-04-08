###112

import pandas as pd
import re
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
nltk.download("wordnet")
lema=nltk.WordNetLemmatizer()
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier

original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/Restaurant_Reviews.tsv",delimiter="\t")
data=original_data.copy()
#print(data)

cleared_data=[]
for i in range(len(data)):
    arrange=re.sub('[^a-zA-Z]',' ',data["Review"][i])
    arrange=arrange.lower()
    arrange=arrange.split()
    arrange=[lema.lemmatize(word) for word in arrange if not word in set(stopwords.words("english"))]
    arrange=' '.join(arrange)
    cleared_data.append(arrange)

cv=CountVectorizer(max_features=1500)
matrix=cv.fit_transform(cleared_data).toarray()
y=data.iloc[:,1].values
X_train,X_test,y_train,y_test=train_test_split(matrix,y,test_size=0.2,random_state=42)
model=GaussianNB()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)

model2nd=RandomForestClassifier(random_state=42)
model2nd.fit(X_train,y_train)
y_pred2nd=model.predict(X_test)

score=accuracy_score(y_test,y_pred)
print(score*100)

martixdf=pd.DataFrame(matrix,columns=cv.get_feature_names_out())
#print(martixdf)

df=pd.DataFrame(list(zip(data["Review"],cleared_data)),columns=["Orinial","Processed"])
#print(df)

freq=(df["Processed"]).apply(lambda x:pd.value_counts(x.split(" "))).sum(axis=0).reset_index()
freq.columns=["Words","Frequency"]
#print(freq)

filt=freq[freq["Frequency"]>10]
filt.plot.bar(x="Words",y="Frequency")
#plt.show()
