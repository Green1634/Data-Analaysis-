#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas


# In[3]:


filepath = 'C:/dataset/'
filename = 'iris.csv'


# In[4]:


df = pandas.read_csv(filepath + filename)


# In[5]:


df


# In[6]:


df.info()


# In[10]:


df.iloc[0:1, 1:3]


# In[12]:


feature1 = df['SepalLength']


# In[13]:


feature1


# In[14]:


featurelist = feature1.values.tolist()
print(featurelist)


# In[29]:


feature2 = df.iloc[10:50, 2:4]


# In[30]:


feature2


# In[36]:


feature3 = df.loc[10:60, ['SepalLength', 'Name']]


# In[37]:


feature3


# In[41]:


mySet = ()


# In[ ]:




