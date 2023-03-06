#88-89 twitter follower scalping via selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


UserName="ktrnsmh2"
Password="814578Gr*"

driver=webdriver.Chrome("C:/Users/Şebnem/Desktop/chromedriver.exe")
url="https://twitter.com/login"
driver.get(url) 
driver.maximize_window()
time.sleep(3)

ka=driver.find_element (By.XPATH,"//input[@autocomplate='username']")
ka.send_keys(UserName)
time.sleep(2)
ka.send_keys(Keys.ENTER)
time.sleep(2)

pas=driver.find_element (By.XPATH,"//input[@autocomplate='current-password']")
pas.send_keys(Password)
time.sleep(2)
pas.send_keys(Keys.ENTER)
url="https://twitter.com/ktrnsmh2"
driver.get(url)
time.sleep(2)

follow=driver.find_element(By.CSS_SELECTOR,"#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(3) > div > div > div > div.css-1dbjc4n.r-1ifxtd0.r-ymttw5.r-ttdzmv > div.css-1dbjc4n.r-13awgt0.r-18u37iz.r-1w6e6rj > div.css-1dbjc4n.r-1mf7evn > a")
followlist=driver.find_element(By.XPATH,"//*[@id=react-root]/div/div/div[2]/main/div/div/div/div/div/section/div/div")
counter=1
for i in followlist:
    print(f"{counter}-{i.text}")
    counter+=1
    counter=counter
