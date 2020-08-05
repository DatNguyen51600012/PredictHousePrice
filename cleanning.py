import pandas as pd
import csv
import re

properties = pd.read_csv('alonhadat.csv')
properties.head()
re_express = re.compile(',')
print(properties.dtypes)
properties['price'].unique()
properties['square_meter'] = properties['square_meter'].apply(lambda x: x.split()[0])
properties['bedroom_no'] = properties['bedroom_no'].apply(lambda z: z.split()[0] )
properties['price'] = properties['price'].apply(lambda y: y.split()[0])
properties['floors'] = properties['floors'].apply(lambda f: f.split()[0] )
properties['road-width'] = properties['road-width'].apply(lambda t: t.split()[0] )
#properties['price'] = properties['price'].apply(lambda y: y.replace(re_express,r'.'))
#properties['price'] = properties['price'].astype(str)
#int(float(x[:4]))
a = properties['price'].count()
phone = "" 

date1 =""

i= 0
while i < a:

    phone = properties['price'][i]
    phone = phone.replace(r',',r'.')
    phone = phone.replace('Thỏa thuận','4.95')
    phone = phone.replace('Thỏa','5')
    properties['price'][i] = properties['price'][i].replace(properties['price'][i],phone)
    phone = "" 
    
    date1 = properties['month_2020'][i]
    date1 = date1.replace('Hôm nay','13/7/2020')
    date1 = date1.replace('Hôm qua','12/7/2020')
    properties['month_2020'][i] = properties['month_2020'][i].replace(properties['month_2020'][i],date1)
    i+=1

phone1 = "" 
j= 0
while j < a:

    phone1 = properties['road-width'][j]
    phone1 = phone1.replace('Trêm','6')
    phone1 = phone1.replace('H?','6')
    phone1 = phone1.replace('m','')
    phone1 = phone1.replace(r',',r'.')
    phone1 = phone1.replace(r'-',r'.')
    properties['road-width'][j] = properties['road-width'][j].replace(properties['road-width'][j],phone1)
    phone1 = "" 
    j+=1

phone2 = ""
k = 0
while k < a:

    phone2 = properties['square_meter'][k]
    phone2 = phone2.replace('KXĐ',"100")
    phone2 = phone2.replace('m','')
    phone2 = phone2.replace(r'\w','')
    phone2 = phone2.replace(r'-',r'.')
    properties['square_meter'][k] = properties['square_meter'][k].replace(properties['square_meter'][k],phone2)
    phone2 = "" 
    k+=1

#properties['price'][1] = phone
properties['square_meter'] = properties['square_meter'].astype(float)
b = properties['square_meter'].count()
n = 0


#properties.astype(str)['price'].map(lambda x:  type(x))
#print(properties.dtypes)
#properties['price'] = properties['price'].replace(to_replace = r'\s', value='new', regex=True)

#properties['price'] = re.sub(r',',r'.',properties['price'])

#properties['price'] = pd.to_numeric(properties['price'], errors = 'coerce')




#for i in properties:
#   if (((properties['price'][i])<1000)&((properties['price'][i])>300)):
#       properties['price'][i] = properties['price'][i]*0.001



properties.to_csv('alonhadat.csv',columns=['name','month_2020','square_meter','road-width','price','bedroom_no','floors','street','area','district'])
