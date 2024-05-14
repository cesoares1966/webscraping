
import sys
import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service = Service()


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=service,options=options)
driver.get('https://google.com/')


time.sleep(10)
driver.quit()
