#!/usr/bin/env python
# coding: utf-8

# # Automated Data Testing with Pytest  
# 
# ## Overview  
# This script uses `pytest` to **automate the validation of restaurant dataset values**.  
# It checks for:  
# - **Valid price values** (must be greater than zero)  
# - **Correct drink values** (should match predefined options)  
# - **Presence of required fields**  
# 
# ## Purpose  
# - Ensures that data validation rules are correctly enforced  
# - Detects errors in structured data automatically  
# - Supports test-driven development (TDD) for data integrity  
# 
# ## How to Run  
# Run the following command in the terminal:  
# ```bash
# pytest test_validation.py
# 

# In[1]:


import pandas as pd
import pytest


# In[2]:


data = "C:/Users/jaeki/OneDrive/바탕 화면/데이터/데이터 분석/data/Restaurant.csv"


# In[3]:


df = pd.read_csv(data)


# In[4]:


df


# In[ ]:


def test_price():
    assert (df['Price'] >= 0).all(), "Detected invaild value in Price column"
    
def test_customer():
    assert (df['Customers'] >= 0).all(), "Dectected invaild value in Customers column"
    
def test_dirnk():
    assert (df['Drink'].isin({"Yes", "No"})).all(), "Detected invaild value in Drink column"
    

