#111 matplotlib 
import matplotlib.pyplot as plt
Serial1st=[1,2,3,4,5]
#plt.plot(Serial1st)
#plt.show()
Serial2nd=[6,7,8,9,10]
#plt.plot(Serial1st,Serial2nd) # ilk parametre x, ikinci parametre y
#plt.show()


s3rd=[2017,2018,2019,2020,2021,2022,2023]
s4th=[100,200,300,400,500,600,700]
plt.plot(s3rd,s4th,color="gray",linewidth=2)
plt.axis([2017,2025,0,1000]) # kkordinat cetvelini ayarlayabiliyoruz.
plt.title("2015-2023 Price Values")
plt.xlabel("Year")
plt.ylabel("Prices")
plt.show()