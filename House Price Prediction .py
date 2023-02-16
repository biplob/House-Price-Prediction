#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.chdir(r'E:\data wrangling')


# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv('house-price.csv')


# In[4]:


df.head()


# In[5]:


df.shape


# In[6]:


df.columns


# In[7]:


df.area_type.unique()


# In[8]:


df['society'].unique()


# In[9]:


df.area_type.value_counts()


# In[10]:


df.availability.value_counts()


# In[11]:


df.location.value_counts()


# In[12]:


data = df.drop(['area_type', 'availability', 'society', 'balcony'], axis='columns')


# In[13]:


data.shape


# In[14]:


data.head() # check new data frame


# ### Handle Null Value

# In[15]:


data.isnull().sum()


# In[16]:


new_data = data.dropna() # Assign new data frame


# In[17]:


new_data.shape # check how many row are drop 


# In[18]:


new_data.isnull().sum() # check is any value are null


# In[19]:


x = '4 BHK'
x.split()


# In[20]:


int(x.split()[0])


# In[21]:


def extract_number(x):
    return int(x.split()[0])


# In[22]:


# new_data['BHK'] = new_data['size'].apply(extract_number)


# In[23]:


new_data['BHK'] = new_data['size'].apply(lambda x:int(x.split()[0]))


# In[24]:


new_data.head()


# In[25]:


new_data.BHK.unique()


# In[26]:


new_data[new_data.BHK == 43]


# In[27]:


new_data[new_data.BHK == 19]


# In[28]:


new_data.total_sqft.unique()


# In[29]:


new_data['bath'].unique()


# In[30]:


new_data[new_data.bath == 40]


# ## total_sqft Feature Engineering

# In[31]:


def is_float(x):
    try:
        float(x)
    except:
        return False
    return True


# In[32]:


is_float(10000)


# In[33]:


is_float('1000.10000')


# In[34]:


new_data[~new_data.total_sqft.apply(is_float)].head(10)


# In[35]:


def convert_sqfeet(x):
    tokens = x.split('-')
    if len(tokens) == 2:
        return (float(tokens[0])+float(tokens[1]))/2
    try:
        return float(x)
    except:
        return None


# In[36]:


ndata = new_data.copy()
ndata.total_sqft = ndata.total_sqft.apply(convert_sqfeet)


# In[37]:


ndata.head(20)


# In[38]:


ndata.isnull().sum()


# In[39]:


ndata = ndata[ndata.total_sqft.notnull()]


# In[40]:


ndata.head(10)


# In[41]:


ndata.loc[122]


# In[42]:


ndata.shape


# ## Price Per Square Feet Feature

# In[43]:


newdata = ndata.copy()


# In[44]:


newdata['price_per_sqfeet'] = newdata['price']*100000 / newdata['total_sqft']
newdata.head(10)


# In[45]:


newdata['price_per_sqfeet'].describe()


# In[46]:


newdata.to_csv('HousePrice.csv', index=False)


# In[47]:


newdata['location'].value_counts()


# In[48]:


newdata[newdata.total_sqft / newdata.BHK <300].head(10)


# In[49]:


newdata.shape


# In[69]:


df6 = newdata[~(newdata.total_sqft / newdata.BHK <300)]


# In[70]:


df6.shape


# ## Dimension Removal

# In[71]:


df6.head()


# In[72]:


df6.location = df6.location.apply(lambda x: x.split())


# In[73]:


location_state = df6.location.value_counts(ascending = False)
location_state


# In[74]:


location_state.values.sum()


# In[75]:


len(location_state)


# In[76]:


len(location_state[location_state > 10]) # location_state greate than 10


# In[77]:


len(location_state[location_state < 10]) # Location_state less than 10


# In[78]:


location_state_less_than_10 = location_state[location_state > 10]
location_state_less_than_10


# In[80]:


df6.head()


# In[83]:


df6[df6.bath > df6.BHK+2]


# In[87]:


df7 = df6[df6.bath < df6.BHK+2]
df7.shape


# In[89]:


df7.to_csv('Final Data.csv', index=False)


# In[ ]:




