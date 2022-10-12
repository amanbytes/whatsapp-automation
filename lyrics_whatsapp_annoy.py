from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("user-data-dir=C:/Users/Aman/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome('D:/Python/Small_Py_Projects/chromedriver.exe',chrome_options=options)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 100)

target = '"Target"'
lyrics=open('lyrics.txt','r')
text = lyrics.read()
lyrics.close()
text=text.split()
lines=[]
line=''
for word in text:
    if len(line)+len(word)>20:
        lines.append(line)
        line=''
    line = line+' '+word
lines.append(line)


x_arg = '//span[contains(@title,'+ target +')]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
for word in lines:
    input_box.send_keys(word+ Keys.ENTER)
    time.sleep(0.2)
