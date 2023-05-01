###122 recomendation systems sample
import pandas as pd
from sklearn.metrics import pairwise_distances

movies=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/ml-latest-small/movies.csv")
ratings=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/ml-latest-small/ratings.csv")

df=pd.merge(movies,ratings,on="movieId")
df=df[["userId","title","rating"]]
#print(df)

pivot=df.pivot_table(index="title",columns="userId",values="rating",fill_value=0)
#print(pivot)

similarity_matrix=pairwise_distances(pivot,metric="correlation")
indexes=list(pivot.index)
movie_index=indexes.index("Godfather, The (1972)")
similar_indexes=(similarity_matrix[movie_index].argsort()[1:11])
for i in similar_indexes:
    print(indexes[i])