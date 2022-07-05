import pandas as pd
data=pd.read_csv("test1033.csv")
print(data.shape)
data=pd.to_numeric(data["case"])
for i in range(24)
    print(data.nlargest(60i).sum())
