import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series({16976: 2, 1: 39, 2: 49, 3: 187, 4: 159,
               5: 158, 16947: 14, 16977: 1, 16948: 7, 16978: 1, 16980: 1},
               name='article_id')
print (s)

#Name: article_id, dtype: int64
s.plot.bar()
plt.show()