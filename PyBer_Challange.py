#!/usr/bin/env python
# coding: utf-8

# # Pyber Challenge

# ### 4.3 Loading and Reading CSV files

# In[1]:


# Add Matplotlib inline magic command
get_ipython().run_line_magic('matplotlib', 'inline')
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd

# File to Load (Remember to change these)
city_data_to_load = "city_data.csv"
ride_data_to_load = "ride_data.csv"

# Read the City and Ride Data
city_data_df = pd.read_csv(city_data_to_load)
ride_data_df = pd.read_csv(ride_data_to_load)


# ### Merge the DataFrames

# In[2]:


# Combine the data into a single dataset
pyber_data_df = pd.merge(ride_data_df, city_data_df, how="left", on=["city", "city"])

# Display the data table for preview
pyber_data_df.head()


# ## Deliverable 1: Get a Summary DataFrame 

# In[1]:


#  1. Get the total rides for each city type
urban_ride_count = urban_cities_df.groupby(["city"]).count()["ride_id"]


# In[2]:


# 2. Get the total drivers for each city type
urban_drivers_sum = urban_cities_df.groupby(["city"]).sum()["ride_id"]


# In[3]:


#  3. Get the total amount of fares for each city type
urban_fare_sum = urban_fare_df.groupby(["city"]).sum()["ride_id"]


# In[4]:


#  4. Get the average fare per ride for each city type. 
urban_fare_sum = urban_fare_df.groupby(["city"]).sum()["ride_id"]/5


# In[5]:


# 5. Get the average fare per driver for each city type. 
urban_fare_sum = urban_fare_df.groupby(["city"]).sum()["ride_id"]/5


# In[8]:


#  6. Create a PyBer summary DataFrame. 


# In[9]:


#  7. Cleaning up the DataFrame. Delete the index name
pyber_summary_df.index.name = None


# In[10]:


#  8. Format the columns.


# ## Deliverable 2.  Create a multiple line plot that shows the total weekly of the fares for each type of city.

# In[11]:


# 1. Read the merged DataFrame


# In[12]:


# 2. Using groupby() to create a new DataFrame showing the sum of the fares 
#  for each date where the indices are the city type and date.


# In[13]:


# 3. Reset the index on the DataFrame you created in #1. This is needed to use the 'pivot()' function.
# df = df.reset_index()


# In[14]:


# 4. Create a pivot table with the 'date' as the index, the columns ='type', and values='fare' 
# to get the total fares for each type of city by the date. 

get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


# 5. Create a new DataFrame from the pivot table DataFrame using loc on the given dates, '2019-01-01':'2019-04-29'.


# In[16]:


# 6. Set the "date" index to datetime datatype. This is necessary to use the resample() method in Step 8.
# df.index = pd.to_datetime(df.index)


# In[17]:


# 7. Check that the datatype for the index is datetime using df.info()


# In[18]:


# 8. Create a new DataFrame using the "resample()" function by week 'W' and get the sum of the fares for each week.


# In[19]:


# 8. Using the object-oriented interface method, plot the resample DataFrame using the df.plot() function. 

# Import the style from Matplotlib.
from matplotlib import style
# Use the graph style fivethirtyeight.
style.use('fivethirtyeight')


# In[ ]:




