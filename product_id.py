import requests
import time
import random
import pandas as pd
import os  
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://tiki.vn/?src=header_tiki',
    'x-guest-token': 'k2QERlHIBzdrmhW4yYcPtaMDn5Sv9qCj',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params_mobile = {
    'limit': '48',
    'include': 'sale-attrs,badges,product_links,brand,category,stock_item,advertisement',
    'aggregations': '1',
    'trackity_id': '70e316b0-96f2-dbe1-a2ed-43ff60419991',
    'category': '1795',
    'page': '1',
    'src': 'c1795',
    'urlKey':  'dien-thoai-smartphone',
}

params_laptop = {
    'limit': '48',
    'include': 'sale-attrs,badges,product_links,brand,category,stock_item,advertisement',
    'aggregations': '1',
    'trackity_id': '70e316b0-96f2-dbe1-a2ed-43ff60419991',
    'category': '8095',
    'page': '1',
    'src': 'c8095',
    'urlKey':  'laptop',
}

mobile_id = []
page = 1
while True:
    params_mobile['page'] = page
    response = requests.get('https://tiki.vn/api/v2/products', headers=headers, params=params_mobile)#, cookies=cookies)
    if response.status_code == 200:
        print(f'request success page {page} - smartphone!!!')
        data = response.json().get('data')
        if not data:  # Nếu không có dữ liệu nữa thì dừng vòng lặp
            break
        for record in data:
            mobile_id.append({'id': record.get('id')})
        page += 1
    else:
        print('request failed!!!')
directory = 'raw_data'
df = pd.DataFrame(mobile_id)
df.to_csv('./raw_data/mobile_id_ncds.csv', index=False)

laptop_id = []
page = 1
while True:
    params_laptop['page'] = page
    response = requests.get('https://tiki.vn/api/v2/products', headers=headers, params=params_laptop)#, cookies=cookies)
    if response.status_code == 200:
        print(f'request success page {page} !!!')
        data = response.json().get('data')
        if not data:  # Nếu không có dữ liệu nữa thì dừng vòng lặp
            break
        for record in data:
            laptop_id.append({'id': record.get('id')})
        page += 1
    else:
        print('request failed!!!')

df = pd.DataFrame(laptop_id)
df.to_csv('./raw_data/laptop_id_ncds.csv', index=False)