###103
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
lema=WordNetLemmatizer()
from wordcloud import WordCloud
import numpy as np
from PIL import Image
from sklearn.feature_extraction.text import CountVectorizer

original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/spam.csv",encoding="Windows-1252")
data=original_data.copy()
#print(data)

data=data.drop(columns=["Unnamed: 2","Unnamed: 3","Unnamed: 4"],axis=1)
data=data.rename(columns={"v1":"Tag","v2":"SMS"})
#print(data)

data2nd=data["SMS"].str.replace("[^\w\s]","",regex=True)
#data3rd=re.sub('[^a-zA-Z]'," ",data["SMS"][0])
data3rd=data2nd.str.lower()
data4th=data3rd.str.replace("[\d]","",regex=True) # wil remove digits

stop_words=stopwords.words("english")
stop_words.extend(" n ")
data5th=data4th.apply(lambda x:" ".join(x for x in x.split() if x not in stop_words or x==" n "))
#print(original_data["v2"][0])
#print(data4th.iloc[0])
#print(data5th.iloc[0])

ps=PorterStemmer()

cleared_data=[]
for i in range(len(data)):
    sort=re.sub('[^a-zA-Z]',' ',data["SMS"][i])
    sort=sort.lower()
    sort=sort.split()
    sort=[lema.lemmatize(word) for word in sort if not word in set(stopwords.words("english"))]
    sort=' '.join(sort)
    cleared_data.append(sort)
cv=CountVectorizer(max_features=500)
matrix=cv.fit_transform(cleared_data).toarray()
matrix_df=pd.DataFrame(matrix,columns=cv.get_feature_names_out())
print(matrix_df)

"""
df=pd.DataFrame(list(zip(data["SMS"],cleared_data)),columns=["Original Data","Cleared Data"])
#print(df.iloc[0])

frequency=(df["Cleared Data"]).apply(lambda x:pd.value_counts(x.split(" "))).sum(axis=0).reset_index()
frequency.columns=["Words","Frequency"]
words=dict(frequency.values)
#print(frequency)
#print(frequency.info())
#print(frequency.nunique())

picture=np.array(Image.open("C:/Users/Şebnem/Desktop/tutorials/Abe.jpg"))
#filter=frequency[frequency["Frequency"]>250]
#filter.plot.bar(x="Words",y="Frequency")
#plt.show()
plt.figure(figsize=(5,5))
cloud=WordCloud(background_color="White",mask=picture,colormap="rainbow",max_words=250).generate_from_frequencies(words)
plt.imshow(cloud)
plt.axis("off")
plt.show()
"""