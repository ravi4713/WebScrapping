import selenium
from selenium import webdriver

import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver=webdriver.Edge(executable_path='C:/Users/RAVI KUMAR RUNGTA/webdrivers/msedgedriver')


driver.get("https://www.instagram.com/")