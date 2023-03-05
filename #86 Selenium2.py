#86 Selenium further data scalping
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # klavye kullanımı
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome("C:/Users/Şebnem/Desktop/chromedriver.exe")
url="https://www.dr.com.tr/"
driver.get(url)
time.sleep(2)
driver.maximize_window()
time.sleep(2)
book=driver.find_element(By.XPATH,"/html/body/div[1]/header/div[4]/div[2]/ul/li[1]/a")
time.sleep(1)
book.click()
time.sleep(2)   
searchbook=driver.find_element(By.XPATH,"/html/body/div[1]/header/div[3]/div/div/div[4]/div[2]/input")
searchbook.send_keys("world")
time.sleep(2)
searchbook.send_keys(Keys.ENTER) # enter tuşuna basacak
time.sleep(5)

for i in range(1,10):
    inf=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/main/div[4]/div[1]/div[{}]".format(i))
    print(inf)
    driver.close()

