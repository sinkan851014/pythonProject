import pandas as pd
import matplotlib.pyplot as plt

#路段
data=pd.read_csv("allroad_hoursvolume.csv")#讀取資料,格式為 0:路段編號 1:車速 2:偵測車流量
A=[]
for i in range(9824):
    A.append(data.iloc[i])
af = pd.DataFrame.from_dict(A)
for k in range(393):
    bfrange = af.iloc[0 + 25 * k:24 + 25 * k]  # 設立range物件
    bfrange.plot.bar()
    plt.show()

        #picture=A.append(data.iloc[i])
#    af = pd.DataFrame.from_dict(A)
#    print(af)
#    af.drop(data.index,inplace=True)

