import pandas as pd
import csv
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

properties = pd.read_csv('alonhadat.csv')

#print(properties['price'].describe())
#print(properties['price'].median())

fig,ax = plt.subplots(figsize=(8,6))
sns.distplot(properties['price'],kde=False,ax=ax)
plt.title('Sale Price Distribution')
plt.xlabel('Sale Price')
plt.ylabel('Freq')
plt.show()


sale_price = properties['price'].values
properties['district'] = properties['district'].fillna('0')

d = properties.groupby('district')['price'].median()
f = properties.groupby('month_2020')['price'].median()

y = []
for o in f:
    y.append(o)

#print(f)
#print(o)

g = d.count()
i=1
u = []

ht = y[10:]
hx = y[:10]
hg = ht + hx
print(hg)

for l in d:
    u.append(l)

#print(u)

date2 = ['15/6','19/6','20/6','21/6','23/6','24/6','27/6','29/6','3/7','4/7','6/7','7/7','8/7','9/7','10/7','11/7','12/7','13/7']
dist = ['0','Bình Chánh','Cần Giờ','Củ Chi','Hóc Môn','Nhà Bè','Quận 1','Quận 10','Quận 11','Quận 12','Quận 2','Quận 3','Quận 4','Quận 5','Quận 6','Quận 7','Quận 8','Quận 9','Bình Thạnh','Bình Tân','Gò Vấp','Phú nhuận','Thủ Đức','Tân Bình','Tân Phú']

plt.bar(date2,hg)
plt.title('Median Price by Date')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

plt.bar(dist,u)
plt.title('Median Price by District')
plt.xlabel('District')
plt.ylabel('Price')
plt.show()

plt.scatter(properties['floors'],properties['price'])
plt.title('Correlation Floors vs Price')
plt.xlabel('Floors')
plt.ylabel('Price')
plt.show()
plt.scatter(properties['bedroom_no'],properties['price'])
plt.title('Correlation Bedroom vs Price')
plt.xlabel('Bedroom')
plt.ylabel('Price')
plt.show()
plt.scatter(properties['road-width'],properties['price'])
plt.title('Correlation Roadwidth vs Price')
plt.xlabel('Roadwidth')
plt.ylabel('Price')
plt.show()
plt.scatter(properties['square_meter'],properties['price'])
plt.title('Correlation SquareMeter vs Price')
plt.xlabel('Square meter')
plt.ylabel('Price')
plt.show()