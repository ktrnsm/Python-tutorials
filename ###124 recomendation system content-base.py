###124 recomendation system content-based
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/movies_metadata.csv")
data=original_data.copy()

df=data[["id","title","overview"]]
#print(df)

tdidf=TfidfVectorizer(stop_words="english")
df["overview"]=df["overview"].fillna(" ")
tdidf_matrix=tdidf.fit_transform(df["overview"])
#print(tdidf_matrix.shape)

similarity_matrix=linear_kernel(tdidf_matrix,tdidf_matrix)
indexes=pd.Series(df.index,index=df["title"]).drop_duplicates()
movie_index=indexes["Toy Story"]
movie_similar=list(enumerate(similarity_matrix[movie_index]))
sort=sorted(movie_similar,key=lambda x: x[1],reverse=True)
sort_score=sort[1:11]
sort_index=[i[0] for i in sort_score]
output=df["title"].iloc[sort_index]
print(output)

