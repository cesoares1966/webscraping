
# pip install chromedriver-autoinstaller
# https://pypi.org/project/webdriver-manager/

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

url = "https://books.toscrape.com/index.html"
driver.get(url)
time.sleep(2)

livros = dict()
links = driver.find_elements(By.TAG_NAME,value='a')[54:92:2]
lista_titulos = [title.get_attribute('title') for title in links]

lista_estoque =[]
for titulo in links:

    titulo.click()
    estoque = driver.find_element(By.CLASS_NAME, value='instock').text
    qtde = re.findall(r'(?<=In\sstock\s\().*(?=\savailable\))',estoque)
    lista_estoque.append(qtde[0])
    driver.back()
    time.sleep(1)

data = {'titulo':lista_titulos,'estoque':lista_estoque}
dados = pd.DataFrame(data)
dados.to_excel('livros.xlsx')
print(dados)

time.sleep(5)
driver.quit()



