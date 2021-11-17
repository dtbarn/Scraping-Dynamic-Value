#Scraping Dynamic Value

from selenium import webdriver
import time

def get_driver():
  #options to make browsing easier
  options = webdriver.ChromeOptions()
  #info-bars may pop up and confuse cursor location
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
  '''Extract the temperature from the element'''
  output = float(text.split(": ")[1])
  return output

def main():
  driver = get_driver()
  time.sleep(2)
  #xpath can be found by using inspect on the 
  #web page to locate the item of interest
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)

  print(main())