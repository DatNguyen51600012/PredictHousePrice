import pandas as pd
import csv
import re
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing

properties = pd.read_csv('alonhadat.csv')

num = preprocessing.LabelEncoder()

properties['district'] = num.fit_transform(properties['district'].astype('str'))
properties['area'] = num.fit_transform(properties['area'].astype('str'))
properties['street'] = num.fit_transform(properties['street'].astype('str'))
properties['month_2020'] = num.fit_transform(properties['month_2020'].astype('str'))

properties['district'] = properties['district'].astype(float)
properties['area'] = properties['area'].astype(float)
properties['street'] = properties['street'].astype(float)
properties['month_2020'] = properties['month_2020'].astype(float)


properties.to_csv('alonhadat.csv',columns=['name','month_2020','square_meter','road-width','price','bedroom_no','floors','street','area','district'])