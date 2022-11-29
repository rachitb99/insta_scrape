import random
import time
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os
directory = 'accounts'

existing = []

for filename in os.listdir(directory):
    existing.append(filename)

f2 = open("followed.csv", "r")
followed = f2.read().split('\n')
f2.close()


followed = [x.split('|') for x in followed if x!='']

followed = [x[0] for x in followed if x[1] == '1']

to_get_followers = [x for x in followed if x not in existing]

driver = webdriver.Firefox()

driver.get("http://www.instagram.com")

#target username
username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

#enter username and password
username.clear()
username.send_keys("randolfjakarta")
password.clear()
password.send_keys("user@2000")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[type='submit']"))).click()

for account in to_get_followers:
  driver.get('https://www.instagram.com/'+ account + '/followers')
  try:
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.XPATH, "//div[text()='Follow']"))).click()
  except:
    pass