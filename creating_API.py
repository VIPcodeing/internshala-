#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


shoplist=pd.DataFrame(columns=['FruitsID','NAME','PRICE','DESCRIPTION','IMAGE'])
print(shoplist)


# In[3]:


A= [1,2,3,4,5,]
B= ['Apple', 'Banana', 'Grapes','Orange','Avacado']
C= [200,60,120,130,1200]
D= ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident.','Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?','At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga.']
E= ['https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1548&q=80','https://cdn.pixabay.com/photo/2018/09/24/20/12/bananas-3700718_1280.jpg','https://images.pexels.com/photos/708777/pexels-photo-708777.jpeg?auto=compress&cs=tinysrgb&w=800','https://images.unsplash.com/photo-1611080626919-7cf5a9dbab5b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80','https://images.unsplash.com/photo-1601039641847-7857b994d704?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1740&q=80']
shoplist['FruitsID']= pd.Series(A)
shoplist['NAME']= pd.Series(B)
shoplist['PRICE']= pd.Series(C)
shoplist['DESCRIPTION']= pd.Series(D)
shoplist['IMAGE']= pd.Series(E)
print(shoplist)


# In[4]:


shoplist['NAME']


# In[5]:


shoplist['NAME'].describe()


# In[6]:


print(shoplist.head(2))


# In[7]:


for column in shoplist.columns:
    print(column + ":", shoplist.loc[1, column])


# In[8]:


for index, row in shoplist.iterrows():
    print("Row", index + 1)
    for column in shoplist.columns:
        print(column + ":", row[column])
    print()


# In[9]:


import json

# Assume you have a dataset named 'data'
output = []

for index, row in shoplist.iterrows():
    row_data = {}
    for column in shoplist.columns:
        row_data[column] = row[column]
    output.append(row_data)

json_output = json.dumps(output)
print(json_output)


# In[24]:


from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/api/endpoint")
async def send_data():
    
    
    # Define the API endpoint URL
    url = "https://example.com/api/endpoint"

    # Send a POST request to the API endpoint with the JSON payload
    response = requests.post(url, json=json_output)

    # Check the response status code
    if response.status_code == 200:
        return {"message": "Data sent successfully!"}
    else:
        return {"error": "Failed to send data."}


# In[16]:


#!pip install fastapi==0.65.2 pydantic==1.8.2


# In[ ]:




