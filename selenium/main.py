from selenium import webdriver
from selenium.webdriver.common.by import By
import time
co=webdriver.ChromeOptions()
co.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=co)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# artnum=driver.find_element(By.XPATH,value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# print(artnum.text)

driver.get("https://www.wikipedia.org/")
sb=driver.find_element(By.XPATH,value="/html/body/main/div[2]/form/fieldset/div/input")
sb.send_keys("shakesphere")
but=driver.find_element(By.XPATH,value="/html/body/main/div[2]/form/fieldset/button/i")
but.click()