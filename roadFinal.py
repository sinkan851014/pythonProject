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
    road = road[2]
    A = []
    # A.append(road)

    for i in range(1, 4319, 3):
        A.append(data[road][i])
    af = pd.DataFrame.from_dict(A)  # .transpose()  # 直的,transpose轉置
    bf = pd.to_numeric(af[0])  # 將string轉為數字
    C = []
    C.append(road)  # 編號路段
    for i in range(24):
        print(bf.iloc[0 + 60 * i:60 + 60 * i].sum())
        bfrange = bf.iloc[0 + 60 * i:60 + 60 * i]  # 設立range物件
        filter = (bfrange >= 0) & (bfrange < 255)  # 篩選，避免掉原始資料-99的data
        filteredData = bfrange[filter]  # 替換為過濾後的資料茲
        print(filteredData.sum())
        print("=====")  # 分隔線，利於比較
        C.append(filteredData.sum())  # 把資料加入陣列
    cf = pd.DataFrame.from_dict(C)  # 轉換資料為pandas資料
    cf.to_csv("allroad_hoursvolume.csv", index=False, header=0, mode="a")  # 輸出csv
