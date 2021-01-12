from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.keys import Keys

#programa para enviar mensagens para contatos armazenados na agenda. 

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(8)
contatos = ['Trabalho','Aline Nunes','Adeilton','Paixão Vegan - Rep SP', 'Paixão teste','+5521971468941']
mensagem = "teste"

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)


for contato in contatos:
    buscar_contato(contato)
    #enviar_mensagem(mensagem)