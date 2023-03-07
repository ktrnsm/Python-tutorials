#98 Pandas-3rd
#data frame yapısı bir'den fazla serinin data yapııs içinde toplanması

import pandas as pd
serial1st=[1,3,5,7,9]
serial2nd=[0,2,4,6,8]
#y=pd.Series(serial1st)
#print(y)

headerserial=dict(product1=serial1st,product2=serial2nd)
datas=pd.DataFrame(headerserial)
print(datas)
