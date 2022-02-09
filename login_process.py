from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt

def getdriver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com/login/")
  return driver

def getdriver_without_login():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com")
  return driver

def clean_text(text):
  """Extract only temperature value"""
  output = text.split(":")
  print(output)
  return output[1]

def scrape_once():
  driver = getdriver()
  time.sleep(3)
  element=driver.find_element(By.ID, "id_username")
  element.send_keys("automated")
  element=driver.find_element(By.ID, "id_password")
  element.send_keys("automatedautomated"+Keys.RETURN)
  time.sleep(2)
  element = driver.find_element(by="xpath", value="/html/body/nav/div/a")
  element.click()
  time.sleep(3)
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  temp = clean_text(element.text)
  print(temp)

def write_file(text):
  filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
  with open(filename, 'w') as f:
    f.write(text)

def scape_multiple():
    driver = getdriver_without_login()
    while True:
        time.sleep(2)
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
        temp = clean_text(element.text)
        write_file(temp)
      
  