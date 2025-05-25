from selenium import webdriver
from selenium.webdriver.common.by import By
import time
co=webdriver.ChromeOptions()
co.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=co)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# artnum=driver.find_element(By.XPATH,value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# print(artnum.text)

driver.get("https://secure-retreat-92358.herokuapp.com/")
time.sleep(3000)

n1=driver.find_element(By.NAME,value="fname")
n2=driver.find_element(By.NAME,value="lname")
em=driver.find_element(By.NAME,value="email")

n1.send_keys("damru")
n2.send_keys("kesh")
em.send_keys("kesh@kesh.com")
sb=driver.find_element(By.XPATH,value="/html/body/form/button")
sb.click()