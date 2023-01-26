"""
Config para o replit
"""


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_argument('headless')

url = "https://wise.com/gb/currency-converter/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

#pegando o valor que pode ser por id, class, name...
result = driver.find_element('xpath', '//*[@id="target-input"]')
#print(result)

#para pegar só o atributo daquele elemento (oq está dentro da caixa imput)
entrada = result.get_attribute("value")
print(entrada)

campo_entrada = driver.find_element('xpath', '//*[@id="source-input"]')
#adicionando valor send_keys()
campo_entrada.send_keys("100")

campo_saida = result.get_attribute("value")
print(campo_saida)