#加入list的概念 Time:6.29, 15:58
import urllib.request as req
import pandas as pd


url="http://61.60.10.87/Device/latest/VD/VDLive.xml"
with req.urlopen(url) as response:
    data = response.read().decode("utf-8")

import bs4 #爬蟲套件
root = bs4.BeautifulSoup(data, "xml") #解析xml資料
titles=root.find_all("LinkFlow") #抓關鍵字
time=root.find("UpdateTime")
vehiclevolun=root.find_all("Vehicle")
A=[]
B=[]
C=[]
for LinkFlow in titles:
    if LinkFlow.text != None:
        A.append(LinkFlow.LinkID.text) #
        B.append(LinkFlow.Lanes.Lane.Speed.text)
        C.append(LinkFlow.Lanes.Lane.Vehicles.contents[3].Volume.text)
A.append(time.text)
af = pd.DataFrame.from_dict(A).transpose()  # 直的,transpose轉置
bf = pd.DataFrame.from_dict(B).transpose()
cf = pd.DataFrame.from_dict(C).transpose()
af.to_csv("filetest7.csv", index=False,header=0,mode="a")  # 也可以將csv改成xlsx
bf.to_csv("filetest7.csv", index=False,header=0,mode="a")  # 也可以將csv改成xlsx
cf.to_csv("filetest7.csv", index=False,header=0,mode="a")  # 也可以將csv改成xlsx


