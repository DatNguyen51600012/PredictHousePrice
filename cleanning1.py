import pandas as pd
import csv
import re
from sklearn import preprocessing
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing


properties = pd.read_csv('alonhadat.csv')
#properties.head()

print(properties.dtypes)
properties['price'].unique()
properties['square_meter'] = properties['square_meter'].astype(float)
properties['bedroom_no'] = properties['bedroom_no'].astype(float)
properties['price'] = properties['price'].astype(float)
properties['floors'] = properties['floors'].astype(float)
properties['road-width'] = properties['road-width'].astype(float)

#print(properties.dtypes)

a = properties['price'].count()
i = 0
while i < a:
    if ((properties['price'][i] < 1000)&(properties['price'][i] > 300)):
        properties['price'][i] =  properties['price'][i]*0.001

    if (properties['price'][i] > 200):
        properties['price'][i] = 200
        properties = properties.drop([i])

    i+=1







properties.to_csv('alonhadat.csv',columns=['name','month_2020','square_meter','road-width','price','bedroom_no','floors','street','area','district'])
