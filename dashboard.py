import pandas as pd
import datetime as dt
df = pd.read_csv("/Users/alain/Desktop/hw4/further_new_dataset.csv")
i=0
data_hours = []
while i<1000:
    d1 = df.loc[i][1]
    d2 = df.loc[i][2]
    m1 = int(d1[0:2])
    day1 = int(d1[3:5])
    h1 = int(d1[11:13])
    min1 = int(d1[14:16])
    s1 = int(d1[17:19])
    m2 = int(d2[0:2])
    day2 = int(d2[3:5])
    h2 = int(d2[11:13])
    min2 = int(d2[14:16])
    s2 = int(d2[17:19])
    res1 = d1[20:22]
    res2 = d2[20:22]
    if res1=="PM" and h1<12:
        h1 += 12
    if res2=="PM" and h2<12:
        h2 += 12
    if res1=="AM" and h1>=12:
        h1 -= 12
    if res2=="AM" and h2>=12:
        h2 -= 12
    create_date = dt.datetime(2020,m1,day1,h1,min1,s1)
    close_date = dt.datetime(2020,m2,day2,h2,min2,s2)
    hours = (close_date-create_date).total_seconds()/3600
    if hours<0:
        print(i+1)
    data_hours.append(hours)
    i += 1
print(len(data_hours))

