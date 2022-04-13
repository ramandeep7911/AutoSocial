from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pyautogui
import time


options = Options()
options.add_argument(r"user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data\profile 1")
# options.add_argument("--kiosk") # Make Full Screen
options.add_argument('--disable-blink-features=AutomationControlled') # avoiding detection
options.add_experimental_option("excludeSwitches", ["enable-automation"])
s = Service(r"C:\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)
# driver.execute_script("window.open('https://video.nest.com/embedded/live/9SnUJNs4AJ?autoplay=1');")
time.sleep(1)

driver.execute_script("window.open('https://www.tiktok.com/login/phone-or-email/email');")
time.sleep(5)
pyautogui.typewrite("romysingh11@gmail.com")
time.sleep(2)
pyautogui.press('tab')
pyautogui.typewrite("Prexmp8085rd!")
time.sleep(2)
pyautogui.press('enter')
time.sleep(4)
driver.execute_script("window.open('https://www.tiktok.com/upload?lang=en');")


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

# start_rec()
# stop_rec()


time.sleep(10)
# driver.quit()
print('Hello')
