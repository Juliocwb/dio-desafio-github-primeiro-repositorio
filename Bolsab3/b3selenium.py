import time
import pandas as pd
from selenium import webdriver

options = webdriver.ChromeOptions()

prefs ={"download.default_directory":'/Users/Usuario/Documents/ProjetosdePython/dio-desafio-github-primeiro-repositorio/Bolsab3'}

options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(executable_path='C:\ProgramData\Anaconda3\chromedriver', chrome_options=options)
driver.get ("https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br")

btn_download = driver.find_element("link text",'Download')
btn_download.click()
time.sleep(3)

driver.close()