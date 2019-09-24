
# coding: utf-8

# In[12]:


#A sample work pending when sql data is connected and exracted
#importing libraries
import pandas as pd
#import pandas_profiling
import numpy as np

#loading a sample file that will make suggestions on loan ammount to be requested by a client using applicant's income as metric
metadata = pd.read_csv('Loan_Pred_Train.csv')


# In[3]:


metadata.head()


# In[6]:


#copying file
metadata2 = metadata.copy()


# In[8]:


#data overview
metadata2.describe()


# In[10]:


#looking for missing values
metadata2.isnull().sum()

