import speech_recognition as sr
from selenium import webdriver
import pyttsx3 as p
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class info():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\\Users\\Manikandan\Downloads\\chromedriver_win32\\chromedriver.exe")

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org/")
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)

        enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button/i')
        enter.click()
        info = self.driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[3]')
        info.click()
        readable_text=info.text
        engine = p.init()
        engine.say(readable_text)
        engine.runAndWait()

#bot = info()
#bot.get_info("taj mahal")