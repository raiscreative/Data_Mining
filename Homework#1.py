#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv('gun-violence-data_01-2013_03-2018.csv')


# In[4]:


df.shape() 


# In[5]:


df.head(15)


# What the code does:
# Firstly it converts the date column from string to datetime format.
# Then it gets the day of the week name for the dates in the 'date' column and assigns it to a variable.
# Finally it inserts a new column named 'day_of_the_week' containing the day of the week names 
# right after the 'date' column, at index 2.

# In[12]:


# the 'date' column is reassigned with the new formated column.
df.date = pd.to_datetime(df.date)
# the variable dotw is assigned with the names of the week day.
dotw = df['date'].dt.day_name()
# the new column is inserted at index 2.
df.insert(2, 'day_of_the_week', dotw)


# In[13]:


df.head(15)


# In[ ]:





# In[ ]:





# In[ ]:




