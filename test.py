from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.keys import Keys

#programa para enviar msg para numeros conhecidos ou desconhecidos 

numeros = open("qb.txt","r")
time.sleep(5)
novo = webdriver.Chrome(ChromeDriverManager().install())
msg = open("texto.txt","r",encoding="utf8")
mensagem = str(msg.read())


def enviar_mensagem(mensagem):
    campo_mensagem = novo.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

for linha in numeros:
    numero = linha.split()
    time.sleep(5)
    novo.get('https://web.whatsapp.com/send?phone=%5B%27{}%27%5D&text={}'.format(numero,""))
    time.sleep(5)
    enviar_mensagem(mensagem)
