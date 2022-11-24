import pandas as pd
import matplotlib as plt
import numpy as np 
data = {'A1' : [1, 3, 4, 3, 5],
'A2' : [2, 4, 5, 2, 4],
'A3' : [3, 2, 3, 1, 3]}
df = pd.DataFrame(data)
df.plot(kind='bar')
plt.show()