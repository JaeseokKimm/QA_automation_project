#!/usr/bin/env python
# coding: utf-8

# # Data Validation Script  
# 
# ## Overview  
# This script performs **data validation for restaurant dataset values** to ensure data integrity and correctness.  
# It checks for:  
# - **Valid price values** (must be greater than zero)  
# - **Correct drink values** (should match predefined options: "Yes" or "No")  
# - **Presence of required fields**  
# 
# ## Purpose  
# - Automatically detect data entry errors  
# - Ensure that dataset values meet expected business rules  
# - Support a structured data validation process for quality assurance  
# 
# ## How to Run  
# Run the following command in the terminal:  
# ```bash
# python validate_data.py
# 

# In[1]:


import pandas as pd


# In[2]:


data = "C:/Users/jaeki/OneDrive/바탕 화면/데이터/데이터 분석/data/Restaurant.csv"

df = pd.read_csv(data)
df


# Make function to check errors in this data frame.
# We will check column Customers, Price and Drink

# In[3]:


def validate_data(df):
    errors = []
    if (df['Customers'] <= 0).any():
        errors.append("Customers column contains values <= 0")
        
    if (df['Price'] <= 0).any():
        errors.append("Price column contains values <= 0")
        
    if not (df['Drink'].isin({"Yes","No"})).all():
        errors.append("Drink column contains invaild values")
        
    return errors if errors else ["data is vaild"]


print('\n'.join(validate_data(df)))
        

