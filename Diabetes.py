#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd


# In[ ]:





# In[36]:


Age = [12, 34, 45, 34, 23, 45, 12, 12, 13, None]
Gender = ['m', 'f', 'm', 'm', None, 'f', 'm', 'f', 'm', 'f']
monthsick = [1, 2, 3, 4, 5, 4, 2, 4, 2, 1]
MalariaParasiteDensity = [1, 2, 1, 1, 2, 3, 1, 2, None, 1]
Community = [1, 2, 3, 4, 5, 8, 5, 5, 1, 9]
infectionWindow = [4, 6, 6, 8, 9, None, 4, 6, 8, 1000]
Genotype = ['AA', 'AS', 'AC', 'SC', 'SS', 'AA', 'AS', 'AS', 'AC', 'SS']


# In[37]:


patientData = [Age, Gender, monthsick, MalariaParasiteDensity, Community, infectionWindow, Genotype]


# In[38]:


df = pd.DataFrame()


# In[40]:


df['Age'] = Age
df['Gender'] = Gender
df['monthsick'] = monthsick
df['MalariaParasiteDensity'] = MalariaParasiteDensity
df['Community'] = Community
df['infectionWindow'] = infectionWindow
df['Genotype'] = Genotype


# In[41]:


df


# In[43]:


filepath = 'C:/dataset/'
filename = 'diabetes.csv'


# In[44]:


dataset = pd.read_csv(filepath + filename)


# In[45]:


dataset


# In[46]:


dataset.size


# In[47]:


dataset.info()


# In[48]:


dataset.describe()


# In[51]:


import matplotlib.pyplot as plt


# In[52]:


dataset['AGE'].plot(kind='density')


# In[55]:


plt.hist(dataset.AGE)


# In[57]:


dataset['BMI'].plot(kind='density')


# In[58]:


plt.hist(dataset.BMI)


# In[59]:


dataset['HDL'].plot(kind='density')


# In[60]:


plt.hist(dataset.HDL)


# In[ ]:





# In[ ]:




