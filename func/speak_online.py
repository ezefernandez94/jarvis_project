from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.headless = True

driver = webdriver.Chrome(options = chrome_options)
website = r"https://ttsmp3.com/text-to-speech/British2English/"
driver.get(website)

button_select = Select(driver.find_element(by = By.ID, value = "sprachwahl"))
button_select.select_by_visible_text("British English / Brian")

def speak(*args):

    speech = ""
    
    for phrase in args:
        speech += str(phrase)
    
    if len(speech) == 0:
        pass
    else:
        driver.find_element(by = By.ID, value = "voicetext").send_keys(speech)
        driver.find_element(by = By.ID, value = "vorlesenbutton").click()
        driver.find_element(by = By.ID, value = "voicetext").clear()



