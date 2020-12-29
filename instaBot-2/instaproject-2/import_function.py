import selenium
from selenium import webdriver

import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pandas as pd
import matplotlib.pyplot as plt
from selenium.common.exceptions import NoSuchElementException


driver=webdriver.Edge(executable_path='C:/Users/RAVI KUMAR RUNGTA/webdrivers/msedgedriver')
driver.get("https://www.instagram.com/")


username=driver.find_element_by_name("username")
username.send_keys("Sample")
password=driver.find_element_by_name("password")
password.send_keys("sample")
login=driver.find_element_by_tag_name("button")
login.submit()
print("WE have sucessfullly login into instagram")