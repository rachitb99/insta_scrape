import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

from selenium.webdriver import FirefoxOptions

opts = FirefoxOptions()
opts.add_argument("--headless")




f1 = open("output.csv", "r")
recommendations = f1.read().split('\n')
f1.close()

f2 = open("followed.csv", "r")
followed = f2.read().split('\n')
f2.close()

followed = [x.split('|')[0] for x in followed]

to_follow = [x for x in recommendations if x not in followed]

# Username - mlnc_confessions_
# Password - MLAconfess@
driver = webdriver.Firefox(options=opts)

driver.get("http://www.instagram.com")

#target username
username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

#enter username and password
username.clear()
username.send_keys("mlnc_confessions_")
password.clear()
password.send_keys("MLAconfess@")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[type='submit']"))).click()

time.sleep(5)

#alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
#    (By.XPATH, '//button[contains(text(), "Not now")]'))).click()

#time.sleep(2)

#alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
#    (By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

# to_follow=['rbansal99']--------------------------------------------------------------------------------
import random
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print()

for user in to_follow:
  try:
    driver.get('https://www.instagram.com/'+ user)

    time.sleep(21 + random.choice(list1))

    # searchbox = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
    # searchbox.clear()

    # for x in user:
    #     time.sleep(0.2)
    #     searchbox.send_keys(x)

    # time.sleep(2)

    # WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
    #     (By.XPATH, '//div[text()="' + user + '"]'))).click()
    # time.sleep(2)

    try:
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[text()='Follow']"))).click()
        
        f3 = open("followed.csv", "a")
        try:
            private = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
                (By.XPATH, '//h2[contains(text(), "This account is private")]'))).click()
            f3.write(user + '|0' + '\n')
        except:
            f3.write(user + '|1' + '\n')
        f3.close()
    except:
        pass
  
  except:
    pass
  print(user)  

driver.quit()
