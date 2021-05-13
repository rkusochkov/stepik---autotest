from selenium import webdriver
import time

link = 'https://m.olimp.bet/'

try:
    browser = webdriver.Chrome()
    browser.get(link)

finally:
    time.sleep(10)
    browser.quit()