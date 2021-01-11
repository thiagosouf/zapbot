from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Teste"
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
        for grupo in self.grupos:
            print("enviando msg para:", grupo)
            #localizador = self.driver.find_element_by_class_name('_2HE1Z _1aIlm')
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(5)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('DuUXI')
            time.sleep(5)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
            time.sleep(5)
            botao_enviar.click()
            time.sleep(5)
        
bot = WhatsappBot()
bot.EnviarMensagens()
