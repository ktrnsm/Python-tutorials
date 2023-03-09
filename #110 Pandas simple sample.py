#110 Pandas simple sample
import pandas as pd
serial1st=pd.DataFrame({"Name":["ktrn","sm","smh"],
                        "Lastname":["a","b","c"]})
serial2nd=pd.DataFrame({"City":["ist","ank","izm"],"Heat":[10,19,25]})
#print(serial1st)
#print(serial2nd)
#folder=serial1st.to_excel("C:/Users/Şebnem/Desktop/tutorials/inf.xlsx",sheet_name="Names",index=False)
#index değerini getirmiyor
#folder=serial2nd.to_excel("C:/Users/Şebnem/Desktop/tutorials/inf.xlsx",sheet_name="weather",index=False)
#ayrı ayrı ikisini yazma durumunda ilkini silip ikincisini oluşturuyour

with pd.ExcelWriter("C:/Users/Şebnem/Desktop/tutorials/inf.xlsx") as writer:
    serial1st.to_excel(writer,sheet_name="Names",index=False)
    serial2nd.to_excel(writer,sheet_name="Weather",index=False)
#with metodu ile silmeden yeni sayfa ekler.


