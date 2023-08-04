from ast import main
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://youtube.com")

print(driver.title)
search = driver.find_element("name", "search_query")
arat = input("Aratmak istediğiniz metni giriniz: ")
search.send_keys(arat)
search.send_keys(Keys.RETURN)

print(driver.page_source)

time.sleep(5)

driver.quit()

