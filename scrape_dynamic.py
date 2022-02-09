from selenium import webdriver
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
  driver.get("http://automated.pythonanywhere.com")
  return driver

def clean_text(text):
  """Extract only temperature value"""
  output = text.split(":")
  return float(output[1])

def main():
  driver = getdriver()
  time.sleep(3)
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  temp = clean_text(element.text)
  print(temp)
  

main()

