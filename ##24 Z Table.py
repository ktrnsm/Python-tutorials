##24 Z Table
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(0)
data=np.random.normal(35,2,5) #ortalama 35, standart sapma=2, 5 elemanlı bir veri seti oluşturur.
#her seferinde yeni küme oluşturur. bunu egnellemek için seed kullanırız.
print(data)