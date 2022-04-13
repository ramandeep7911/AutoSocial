from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pyautogui
import time


options = Options()
options.add_argument(r"user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data")
options.add_argument("--kiosk")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
s = Service(r"C:\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)
driver.execute_script("window.open('https://video.nest.com/embedded/live/9SnUJNs4AJ?autoplay=1');")
time.sleep(10)

def start_rec():
    pyautogui.keyDown('ctrl')
    time.sleep(1)
    pyautogui.keyDown('r')
    print('started')
    time.sleep(1)
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    pyautogui.keyUp('r')
    print('Up now')
    print('testing')
    print('git')

def stop_rec():
    time.sleep(20)
    pyautogui.keyDown('ctrl')
    time.sleep(1)
    pyautogui.keyDown('r')
    print('stopped')
    time.sleep(1)
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    pyautogui.keyUp('r')
    print('up now')

start_rec()
stop_rec()
time.sleep(10)
driver.quit()
print('Hello')
