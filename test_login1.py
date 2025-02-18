#!/usr/bin/env python
# coding: utf-8

# # Selenium Automated Login Test with Pytest  
# 
# This script automates the login functionality testing for the website "Practical Test Automation"  
# It uses Selenium WebDriver and Pytest to verify:  
# 
# **Successful login with valid credentials**  
# **Failed login attempt with an incorrect password**  
# 
# The test script automatically:  
# 1. Opens the login page  
# 2. Enters valid or invalid credentials  
# 3. Clicks the login button  
# 4. Verifies if the login was successful or if the correct error message appears  
# 
# 

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

#Selenium WebDriver setup (automatically downloads ChromeDriver)
@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()  # Close the browser after the test finishes

# 1. Test for successful login
def test_login_success(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    # Locate input fields & enter login credentials
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    
    # Click the login button
    driver.find_element(By.ID, "submit").click()
    
    time.sleep(2)  # Wait for the page to load
    
    # Verify successful login message (QA test validation)
    assert "Logged In Successfully" in driver.page_source, "Login failed!"

# 2. Test for failed login (invalid password)
def test_login_fail(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    # Locate input fields & enter incorrect login credentials
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("WrongPassword")
    
    # Click the login button
    driver.find_element(By.ID, "submit").click()
    
    time.sleep(2)  # Wait for the page to load
    
    # Verify if the correct error message appears (QA test validation)
    assert "Your password is invalid!" in driver.page_source, "Error message not displayed!"


# # How to Run the Tests
# 1. Save this script as test_login.py
# 2. Open the terminal or command prompt
# 3. Navigate to the script's directory
# 4. Run the following command: "pytest test_login1.py"
# 
# If the login test passes, the script confirms success
# If the login test fails, it raises an assertion error

# In[ ]:




