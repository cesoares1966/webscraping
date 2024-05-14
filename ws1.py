
# pip install chromedriver-autoinstaller
# https://pypi.org/project/webdriver-manager/

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://www.estantevirtual.com.br")
time.sleep(2)


search_bar = driver.find_element(By.NAME, value='term')
search_bar.send_keys("python")
search_bar.send_keys(Keys.RETURN)


time.sleep(15)
driver.quit()



