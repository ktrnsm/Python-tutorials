#115 matplotlib Figure
import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
location=fig.add_axes([0.1,0.1,0.8,0.6])
year=["2018","2019","2020","2021"]
price=[10,15,20,25]
location.plot(year,price)
location.set_xlabel("year")
location.set_ylabel("Price Value")
location.set_title("price vc year")
#grafik alanın tamamı

#plt.show()

x=np.linspace(-10,9,20)
y=x**2
z=x**3
fig2=plt.figure()
chart1st=fig2.add_axes([0.1,0.1,0.8,0.8])
chart1st.plot(x,y,c="red")
chart1st.set_xlabel("X Value")
chart1st.set_ylabel("Y Value")
chart1st.set_title("Sample Chart")

chart2nd=fig2.add_axes([0.3,0.6,0.2,0.2])
chart2nd.plot(x,z,c="blue")
chart2nd.set_xlabel("X Value")
chart2nd.set_ylabel("Y Value")
#plt.show()

fig3,chart=plt.subplots(nrows=2,ncols=1)
chart[0].plot(x,y,c="blue")
chart[0].set_title("1st Chart")
chart[1].plot(x,z,c="red")
chart[1].set_title("2nd Chart")
plt.tight_layout() # alanların birbiri üzerine kaymasını engelliyor.
plt.show()
fig3.savefig("c:/....".png)