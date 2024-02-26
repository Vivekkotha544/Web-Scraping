import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"/home/kscr599/Desktop/WEB SCRAPING/chromedriver-linux64/"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get("https://www.timesjobs.com/jobfunction/it-software-jobs")
# my_element = driver.find_element_by_id('https://in.bookmyshow.com/hyderabad/movies/hanuman/ET00311673-6')
# my_element.click()
a = driver.find_element(By.CLASSNAME, "disc")
a.click()

driver.implicitly_wait(5)