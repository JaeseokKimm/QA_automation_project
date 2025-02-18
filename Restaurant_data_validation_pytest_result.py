#!/usr/bin/env python
# coding: utf-8

# # Data Validation & Pytest Results  
# 
# ## Overview  
# This Jupyter Notebook documents the **data validation process and automated test results** for restaurant data.  
# It includes:  
# - Dataset validation using `validate_data.py`  
# - Automated tests using `pytest` (`test_validation.py`)  
# - Results of both validation and testing processes  
# 
# ## Purpose  
# - Ensures that the dataset meets expected quality standards  
# - Confirms that automated tests correctly detect errors  
# - Demonstrates how `pytest` validates structured data  
# 
# This notebook serves as a **summary of the validation and testing workflow**.  
# 

# In[1]:


get_ipython().system('python validate_data.py')


# In[2]:


get_ipython().system('pytest test_validation.py')


# Found error from code "def test_dirnk():
#     assert (df['Drink'].isin({"Yest", "No"})).all(), "Detected invaild value in Drink column"".
#     
#    fix "Yest" to "Yes"

# rerunning the code

# In[3]:


get_ipython().system('pytest test_validation.py')


# In[ ]:




