#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[ ]:





# In[6]:


Age = [12, 34, 45, 34, 23, 45, 12, 12, 13, None]
Gender = ['m', 'f', 'm', 'm', None, 'f', 'm', 'f', 'm', 'f']
monthsick = [1, 2, 3, 4, 5, 4, 2, 4, 2, 1]
MalariaParasiteDensity = [1, 2, 1, 1, 2, 3, 1, 2, None, 1]
Community = [1, 2, 3, 4, 5, 8, 5, 5, 1, 9]
infectionWindow = [4, 6, 6, 8, 9, None, 4, 6, 8, 1000]
Genotype = ['AA', 'AS', 'AC', 'SC', 'SS', 'AA', 'AS', 'AS', 'AC', 'SS']


# In[7]:


patientData = [Age, Gender, monthsick, MalariaParasiteDensity, Community, infectionWindow, Genotype]


# In[8]:


df = pd.DataFrame()


# In[9]:


df['Age'] = Age
df['Gender'] = Gender
df['monthsick'] = monthsick
df['MalariaParasiteDensity'] = MalariaParasiteDensity
df['Community'] = Community
df['infectionWindow'] = infectionWindow
df['Genotype'] = Genotype


# In[10]:


df


# In[11]:


filepath = 'C:/dataset/'
filename = 'diabetes.csv'


# In[12]:


dataset = pd.read_csv(filepath + filename)


# In[13]:


dataset


# In[14]:


dataset.size


# In[15]:


dataset.info()


# In[16]:


dataset.describe()


# In[17]:


import matplotlib.pyplot as plt


# In[19]:


dataset.columns


# In[22]:


newData = dataset.loc[:, ['ID', 'No_Pation', 'AGE', 'Urea', 'Cr', 'HbA1c', 'Chol', 'TG',
       'HDL', 'LDL', 'VLDL', 'BMI']]

newData


# In[24]:


from pandas import read_csv 
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler 

dataframe = newData 
array = dataframe.values

x = array[:,0:11]
y = array[:, 11]
demo = MinMaxScaler(feature_range=(0, 1))
rescaledX = demo.fit_transform(x)

set_printoptions(precision=3)
print(rescaledX[0:5, :])


# In[25]:


rescaledXdf = pd.DataFrame(rescaledX)
rescaledXdf.columns = ['ID', 'No_Pation', 'AGE', 'Urea', 'Cr', 'HbA1c', 'Chol', 'TG',
       'HDL', 'LDL', 'VLDL']
rescaledXdf


# In[26]:


rescaledXdf.describe()


# In[27]:


from sklearn.preprocessing import Normalizer
from pandas import read_csv
from numpy import set_printoptions

array = rescaledXdf.values

x = array[:, 0:12]
scaler = Normalizer().fit(x)
normalizedX = scaler.transform(x)

set_printoptions(precision=5)
print(normalizedX[0:5, :])


# In[28]:


normalizedX_df = pd.DataFrame(normalizedX)
normalizedX_df.columns = ['ID', 'No_Pation', 'AGE', 'Urea', 'Cr', 'HbA1c', 'Chol', 'TG',
       'HDL', 'LDL', 'VLDL']
normalizedX_df


# In[29]:


normalizedX_df.describe()


# In[30]:


normalizedX_df['AGE'].plot(kind= 'density')


# In[ ]:


from sklearn.preprocessing import StandardScaler
from pandas import read_csv
from numpy import set_printoptions

array = rescaledXdf.values

x = array[:, 0:12]
scaler = Normalizer().fit(x)
normalizedX = scaler.transform(x)

set_printoptions(precision=5)
print(normalizedX[0:5, :])


# In[ ]:





# In[52]:


dataset['AGE'].plot(kind='density')


# In[ ]:





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





# In[2]:





# In[ ]:




