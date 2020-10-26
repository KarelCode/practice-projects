from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\msedgedriver.exe"
driver = webdriver.Edge(PATH)
driver.maximize_window()

driver.get("https://nhentai.net/")

link = driver.find_element_by_link_text("Random")
link.click()

stranky = driver.find_elements_by_class_name("thumb-container")
stranky_pocet = len(stranky)

stranky[0].click()

for i in range(stranky_pocet - 1):    
    time.sleep(0.2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(0.2)
    next = driver.find_element_by_class_name("next")
    next.click()

time.sleep(0.2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)


driver.quit()
