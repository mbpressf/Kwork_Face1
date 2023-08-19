from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os


driver = webdriver.Chrome()

url = 'https://toonme.com/'


while True:
    try:
        driver.get(url=url)
        break
    except:
        sleep(1)
 
script_path = os.path.abspath(__file__)
dir_path = os.path.dirname(script_path)
image_name = "face.png"
image_path = os.path.join(dir_path, image_name)

while True:
    try:   
        driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[1]/section/input').send_keys(image_path)
        break
    except:
        sleep(1)

while True:
    try:
        driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div[1]/button[6]').click()
        break
    except:
        sleep(1)

while True:
    try:
        driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div[2]/div[1]/div/button[1]').click()
        break
    except:
        sleep(1)

sleep(30)