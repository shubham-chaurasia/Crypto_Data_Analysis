#!/usr/bin/env python
# coding: utf-8

# In[63]:


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'10',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'a848abf4-8175-49f2-86b9-24a4261b1626',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


# In[2]:


type(data)


# In[74]:


import pandas as pd
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)


# In[75]:


pd.json_normalize(data['status'])


# In[76]:


pd.json_normalize(data['data'])


# In[85]:


import pandas as pd

def api_runner():
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'10',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'a848abf4-8175-49f2-86b9-24a4261b1626',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    
    
    df = pd.json_normalize(data['data'])
    df['timestamp'] = pd.to_datetime('now')
    df
    
    if not os.path.isfile(r'C:\Users\lenovo\Downloads\Data Analysis Projects\API.csv'):
        df.to_csv(r'C:\Users\lenovo\Downloads\Data Analysis Projects\API.csv', header='column_name')
    else:
        df.to_csv(r'C:\Users\lenovo\Downloads\Data Analysis Projects\API.csv',mode='a',header=False)
    


# In[78]:


import os 
from time import time
from time import sleep

for i in range(333):
    api_runner()
    print("API runner completed Successfully")
#     sleep(60)
exit()


# In[89]:


df32 = pd.read_csv(r'C:\Users\lenovo\Downloads\Data Analysis Projects\Book.csv')
df32


# In[90]:


df


# In[93]:


pd.set_option('display.float_format', lambda x: '%.5f' % x)


# In[94]:


df


# In[100]:


df3 = df.groupby('name', sort=False)[['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d']].mean()
df3


# In[101]:


df4 = df3.stack()
df4


# In[103]:


type(df3)


# In[105]:


df5 = df4.to_frame(name='values')
df5


# In[114]:


index = pd.Index(range(60))

df6 = df5.set_index(index)
df6


# In[113]:


df5.count()


# In[116]:


df6 = df5.reset_index()
df6.head()


# In[123]:


df7 = df6.rename(columns={'level_1':'percent_change'})
df7.head()


# In[131]:


df7['percent_change']=df7['percent_change'].replace(['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d'],['1h','24h','7d','30d','60d','90d'])
df7


# In[127]:


import seaborn as sns
import matplotlib.pyplot as plt 

sns.catplot(x='percent_change',y='values',hue='name',data=df7,kind='point')
# In[ ]:




