from selenium import webdriver
import time
import pywhatkit
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.keys import Keys

numeros = open("qb.txt","r")
time.sleep(5)
novo = webdriver.Chrome(ChromeDriverManager().install())
mensagem = "Lorem ipsum \n laoreet convallis faucibus sit conubia tincidunt commodo,\n congue aptent velit himenaeos arcu blandit eleifend justo,\n sollicitudin dui himenaeos torquent lacus ut primis.\n blandit sagittis sed proin fringilla donec aenean tellus ullamcorper fringilla vel,\n ornare mattis ac nulla euismod sapien vel pharetra velit." # tincidunt ut id varius pellentesque platea ullamcorper consequat donec. maecenas ipsum quisque ullamcorper augue aliquet fusce potenti eleifend, luctus integer congue morbi tempus lectus tempus non himenaeos, vestibulum justo facilisis massa quam potenti integer. arcu sollicitudin tellus litora donec volutpat posuere ut interdum, maecenas justo ut feugiat habitant convallis fermentum lorem ut, lacinia vulputate lacus aliquet torquent pulvinar risus.
#mensagem = open("texto.txt","r")

def enviar_mensagem(mensagem):
    campo_mensagem = novo.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

for linha in numeros:
    numero = linha.split()
    time.sleep(5)
    #novo = webdriver.Chrome(ChromeDriverManager().install())
    novo.get('https://web.whatsapp.com/send?phone=%5B%27{}%27%5D&text={}'.format(numero,""))
    time.sleep(5)
    enviar_mensagem(mensagem)

#<a class title="Compartilhe no WhatsApp" 
#<a class="_36or" href="https://web.whatsapp.com/send?phone=%5B%27+5521964252845%27%5D&amp;text=sua+mensagem">use o WhatsApp Web</a>
