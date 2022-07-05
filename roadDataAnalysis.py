import pandas as pd
#路段
road="6360370300090H"
data=pd.read_csv("車輛動態偵測器24-24時資料.csv")
A=[]
#A.append(road)

for i in range(1,4319,3):
    A.append(data[road][i])
        #data=data.append(data[road][i])
#data[road]=pd.to_numeric(data[road])
#print(data)
    #print(i, end=" ")
       #A.append(data[road][i])
print(A)
af = pd.DataFrame.from_dict(A)#.transpose()  # 直的,transpose轉置
print(af)
af.to_csv(road+"af_test.csv", index=False,header=0,mode="a")
bf=pd.to_numeric(af[0])
bf.to_csv(road+"bf_test.csv", index=False,header=0,mode="a")
#for i in range(24)
C=[]
C.append(road)
for i in range(24):
    print(bf.iloc[0+60*i:60+60*i])
    print(bf.iloc[0+60*i:60+60*i].sum())
    C.append(bf.iloc[0+60*i:60+60*i].sum())
cf = pd.DataFrame.from_dict(C)
cf.to_csv(road+"_hoursvolume.csv", index=False,header=0,mode="a")  # 也可以將csv改成xlsx
#print(af[""].nlargest(10).sum())
#af[] = pd.to_numeric()
#print(af.sum())
