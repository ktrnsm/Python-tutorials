###6 Separation of training and test data
import pandas as pd
import pandas as pd
from sklearn.model_selection import train_test_split
data=pd.read_excel("C:/Users/Şebnem/Desktop/tutorials/###6.xlsx")
#print(data)

#bağımlı ve bağımsız değişkenler ayrılır

y=data["Y"]
X=data[["X1","X2"]]

#4 veri verir ikisi bağımsız ikisi bağımlı
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)


print(X_train)
print(X_test)
