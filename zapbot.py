from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = ["Teste"]
        self.grupos = ["Trabalho", "Cinema - Técnica"]
        options = webdriver.ChromeOptions()
        options.add_argument("lang=pt-br")
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")

    def EnviarMensagens(self):
        #<div tabindex="-1" class="_2HE1Z _1aIlm">
        #<span dir="auto" title="Cinema - Técnica" class="_1hI5g _1XH7x _1VzZY">Cinema - Técnica</span>
            #<div tabindex="-1" class="DuUXI">
                #<span data-testid="send" data-icon="send" class="">
        self.driver.get("https://web.whatsapp.com/")   
        time.sleep(5)
        a=0     
        for grupo in self.grupos:
            print("enviando msg para:", grupo)
            time.sleep(5)
            localizador = self.driver.find_element_by_xpath("//div[@class='_1awRl copyable-text selectable-text']")
            time.sleep(8)
            localizador.click()
            time.sleep(5)
            localizador.send_keys(self.grupos[a])
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(8)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('DuUXI')
            time.sleep(8)
            chat_box.click()
            time.sleep(5)
            chat_box.send_keys(self.mensagem[0])
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(5)
            botao_enviar.click()
            time.sleep(8)
            a=a+1
            print(a)
        
bot = WhatsappBot()
bot.EnviarMensagens()
