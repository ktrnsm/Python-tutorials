#85 Selenium
from selenium import webdriver
import time

driver=webdriver.Chrome("C:/Users/Şebnem/Desktop/chromedriver.exe")

url="https://www.google.com/doodles"
driver.get(url)
driver.maximize_window()
time.sleep(2)
driver.save_screenshot("screenshot.png")
time.sleep(2)
url2="https://www.google.com/search?rlz=1C1FKPE_trTR978TR978&q=earth&spell=1&sa=X&ved=2ahUKEwilp6iQ68X9AhWmQ_EDHaWPCaoQBSgAegQIHhAB&biw=1536&bih=700&dpr=1.25"
driver.get(url2)
time.sleep(2)
driver.back(url)
driver.close

print(driver.page_source)# source code printed
driver.close()
