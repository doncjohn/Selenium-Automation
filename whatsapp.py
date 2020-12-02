from selenium import webdriver
from time import sleep
driver = webdriver.Chrome("C:\chromedriver.exe")
driver.get('https://web.whatsapp.com')
sleep(15)
msg = "Thanks for listening to EDITH || Even Dead I'm HERO ||"
keys=['DZONE','JINCY JOHNSON']
values=['DZONE','JINCY']
n=(0,1)
for i in n:
    key=keys[i]
    value=values[i]
    sleep(1)
    searchUser = driver.find_element_by_css_selector("input[type='text']")
    searchUser.click()
    searchUser.send_keys(key)
    sleep(1)
    user = driver.find_element_by_css_selector("span[title='"+key+"']")
    user.click()
    sleep(1)
    msgBox = driver.find_element_by_class_name('_3u328')
    msgBox.click()
    msgBox.send_keys("Hello " +value+ msg)
    send = driver.find_element_by_class_name('_3M-N-')
    send.click()