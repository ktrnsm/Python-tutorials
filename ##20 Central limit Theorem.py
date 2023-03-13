##20 Central limit Theorem // 1st
import numpy as np
import matplotlib.pyplot as plt
import random
#customer age Study
Age=np.random.uniform(low=18,high=75,size=40000)
#plt.hist(Age)
#plt.show()
#sampling=random.choices(Age,k=10)
sampling=[np.mean(random.choices(Age,k=30)) for _ in range(1000)]
plt.hist(sampling)
plt.show()
