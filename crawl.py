from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import csv

properties = []

for m in range(1,150):
    url = 'https://alonhadat.com.vn/can-ban-nha-ho-chi-minh-t2/trang-{}.htm'.format(m)
    page_content = urllib.request.urlopen(url)
    rawdata = page_content.read()
    webpage_text = rawdata.decode('utf-8')

    soup = BeautifulSoup(webpage_text, 'lxml')
    items = soup.find_all('div', 'content-item')

# Get the name, area of the property

    for i in items:
        t = i.findChildren('div', class_='ct_title')
        title = t[0].a.string
        o = i.find_all('div', class_='ct_date')        
        date = o[0].next_element
        a = i.find_all('div','ct_dt')
        size = a[0].label.next_element.next_element.string
        try:
            b = i.find_all('div', class_='characteristics')
            bedroom = b[0].find('span','bedroom').string
            f = i.find_all('div', class_='characteristics')
            floors = f[0].find('span','floors').string
            r = i.find_all('div', class_='characteristics')
            roadwidth = r[0].find('span','road-width').string
        except:
            pass
        p = i.find_all('div','ct_price')
        price = p[0].label.next_element.next_element.string
        d = i.find_all('div','ct_dis')
        district = d[0].a.next_element.next_element.next_element.next_element.next_element.next_element.string
        street = d[0].a.string
        area = d[0].a.next_element.next_element.next_element.string
           
        property ={
            'name': title,
            'month_2020': date, 
            'square_meter': size,
            'bedroom_no': bedroom,
            'road-width': roadwidth,
            'floors': floors,
            'price': price,
            'street': street,
            'area': area,
            'district': district,            
        }
        properties.append(property)


try:
    with open('alonhadat.csv', 'w') as output_file:

        keys = properties[0].keys()
        writer = csv.DictWriter(output_file, fieldnames=keys)
        writer.writeheader()
        for property in properties:
            writer.writerow(property)        
    print('Success')
except:
    print('Error')