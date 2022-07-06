import pandas as pd
#路段
data=pd.read_csv("車輛動態偵測器24-24時資料.csv")#讀取資料,格式為 0:路段編號 1:車速 2:偵測車流量
F=[]
F.append(data.iloc[2])
F=pd.DataFrame.from_dict(F).transpose()
F.reset_index(inplace = True, drop = True)


for i in range(393):
    road=(F.iloc[i])
    road = road.astype("string")
    road=road[2]
    print(road)

#for i in range(393)
#寫得很爛的程式，目的是為了抓取編號，作為for loop中代入的參數（事實上已經有內建index），