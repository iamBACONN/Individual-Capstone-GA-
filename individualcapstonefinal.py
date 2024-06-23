#!/usr/bin/env python
# coding: utf-8

# ## overall code

# import pandas as pd
# from ydata_profiling import ProfileReport
# df=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/NYPD_Arrests_Data__Historic_.csv')
# def split_by_year(file_path, dest_folder):
#   
#     #Read a CSV file, split it into smaller CSV files based on the year, and save them in the destination folder.
# 
#     df=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/NYPD_Arrests_Data__Historic_.csv')
#     
#     #Split year from arrest date column
#     if 'ARREST_DATE' in df.columns:
#         df['Year'] = pd.to_datetime(df['ARREST_DATE']).dt.year
#     elif 'Year' not in df.columns:
#         raise ValueError("No 'Date' or 'Year' column found in the CSV file.")
#     for year in df['Year'].unique():
#         year_data = df[df['Year']== year]
#         
#         #to rewrite into a new CSV file
#         year_csv = f"C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_{year}.csv"
#         year_data.to_csv(year_csv, index= False)
# 
# #call the function to split the CSV to years and place the generated CSvs to correct folders
# split_by_year('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/NYPD_Arrests_Data__Historic_.csv', 'C:/Users/bacon/Desktop/GA individual Capstone/Nypd')
# #The following codes will just create each csv that I split into years into a DataFrame.
# df14=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_2014.csv')
# df15=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_2015.csv')
# df16=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_2016.csv')
# df17=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_2017.csv')
# df18=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_2018.csv')
# df19=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_2019.csv')
# df20=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_2020.csv')
# df21=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_2021.csv')
# df22=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_2022.csv')
# df23=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_2023.csv')
# df_dec = pd.concat([df14,df15,df16,df17,df18,df19,df20,df21,df22,df23])
# df = df_dec.drop(df_dec.columns[[2,3,4,6,10,13,18]], axis=1) 
# #lowercase columns as it was bothering me ....
# def columns_to_lower(df):
#     df.columns = df.columns.str.lower()
#     return df
# df= columns_to_lower(df)
# #null handling
# df.ofns_desc = df.ofns_desc.fillna('undetermined')
# df.ofns_desc = df.ofns_desc.replace('(null)', 'undetermined')
# df.law_cat_cd = df.law_cat_cd.replace('(null)', 'undetermined')
# df.law_cat_cd = df.law_cat_cd.fillna('undetermined')
# import numpy as np
# 

# In[1]:


import pandas as pd
from ydata_profiling import ProfileReport


# In[2]:


df=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/NYPD_Arrests_Data__Historic_.csv')
profile = ProfileReport(df, title="Profiling Report")


# In[3]:


df.columns


# In[9]:


profile


# In[4]:


def split_by_year(file_path, dest_folder):
  
    #Read a CSV file, split it into smaller CSV files based on the year, and save them in the destination folder.

    df=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/NYPD_Arrests_Data__Historic_.csv')
    
    #Split year from arrest date column
    if 'ARREST_DATE' in df.columns:
        df['Year'] = pd.to_datetime(df['ARREST_DATE']).dt.year
    elif 'Year' not in df.columns:
        raise ValueError("No 'Date' or 'Year' column found in the CSV file.")
    for year in df['Year'].unique():
        year_data = df[df['Year']== year]
        
        #to rewrite into a new CSV file
        year_csv = f"C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_{year}.csv"
        year_data.to_csv(year_csv, index= False)


# In[ ]:


#call the function to split the CSV to years and place the generated CSvs to correct folders
split_by_year('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/NYPD_Arrests_Data__Historic_.csv', 'C:/Users/bacon/Desktop/GA individual Capstone/Nypd')


# The following codes will just create each csv that I split into years into a DataFrame, then will 

# In[66]:


df14=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_2014.csv')
df15=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_2015.csv')
df16=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_2016.csv')
df17=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_2017.csv')
df18=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_2018.csv')
df19=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_2019.csv')
df20=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_2020.csv')
df21=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_2021.csv')
df22=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_2022.csv')
df23=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/data_2023.csv')


# In[67]:


df_dec = pd.concat([df14,df15,df16,df17,df18,df19,df20,df21,df22,df23])


# In[ ]:


df_dec.shape


# In[ ]:


df_dec.head(10)

#do not need pd_cd pd_cd pd_desc ky cd law code jurisdiction_code perp race lon_lat


# ## CheckPoint1
# Will drop/delete columns \
# pd_cd, pd_desc - These are NYPD internal desciption and classification code for the arrest\
# ky cd - still internal 3 digit code \
# law code - this is specific law code that the suspect violated. (will not be doing individual research on all)\
# jurisdiction_code- This is a code for the type of cop responsible for the arrest.\
# perp race- I will not include race in the analysis as this may potentially show extreme biases in the results\
# lon_lat- I will keep individual columns and not the concat.\
# 
# *noticed that some of the offense columns are null will have to replace will notgive and whatever category it is.

# 

# In[68]:


df_dec.isnull().sum()


# Restart point

# In[69]:


df = df_dec.drop(df_dec.columns[[2,3,4,6,10,13,18]], axis=1) 


# In[27]:


df.shape


# In[70]:


#lowercase columns as it was bothering me ....
def columns_to_lower(df):
    df.columns = df.columns.str.lower()
    return df


# In[71]:


df= columns_to_lower(df)


# In[72]:


df.head()


# In[73]:


def df_to_lower(df):
    # Convert all string values in the DataFrame to lowercase
    df = df.applymap(lambda x: str(x).lower() if isinstance(x, str) else x)
    return df


# In[74]:


df = df_to_lower(df)


# In[75]:


df.head()


# # NULL handling

# nulls 
# ofns_desc           4872\
# law_cat_cd         14506

# In[76]:


df.ofns_desc = df.ofns_desc.fillna('unknown')


# In[77]:


df.ofns_desc = df.ofns_desc.replace('(null)', 'unknown')


# In[78]:


df.law_cat_cd.unique()
# notices there is also a null and a string literal null. replaced both with not given
#but also an I & 9, might have to do some external research to find the meaning - nvm will put it under uncategorzied.


# In[79]:


df.law_cat_cd = df.law_cat_cd.replace('(null)', 'unknown')


# In[80]:


df.law_cat_cd = df.law_cat_cd.fillna('unknown')


# law_cat_cd\
# m              1538113\
# f               859538\
# v                80118\
# unknown      14508\
# i                 8898\
# 9                 1067\
# 
# m= misdemeanor
# f= felony
# v= violation
# i= infraction
# 9= no idea/ will change to 
# unknown = not given 

# In[81]:


df.law_cat_cd.value_counts()


# In[82]:


df.to_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/Nypddata_capstone.csv', index=False)


# In[2]:


import pandas as pd


# In[83]:


fdf=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/Nypddata_capstone.csv')


# In[62]:


fdf.law_cat_cd.unique()


# In[84]:


fdf.law_cat_cd = fdf.law_cat_cd.replace('i', 'uncategorized').replace('9','uncategorized')


# In[85]:


fdf.law_cat_cd = fdf.law_cat_cd.replace('unknown', 'uncategorized')


# In[88]:


fdf.to_csv('C:/Users/bacon/Desktop/GA individual Capstone/Nypd/Nypddata_capstone.csv', index=False)


# In[10]:


df=pd.read_csv('C:/Users/bacon/Desktop/GA individual Capstone/RentData/medianAskingRent_All.csv')


# In[12]:


df2=pd.read_excel('C:/Users/bacon/Desktop/GA individual Capstone/RentData/medianrent .xlsx')


# In[87]:


fdf.head()

