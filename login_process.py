from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

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

def clean_text(text):
  """Extract only temperature value"""
  output = text.split(":")
  return float(output[1])

def main():
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


main()
  