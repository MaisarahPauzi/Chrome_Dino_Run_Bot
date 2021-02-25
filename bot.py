from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui 
from PIL import Image, ImageGrab 

def hit(key):
    pyautogui.keyDown(key)
    if key == "down":
        sleep(0.3)
        pyautogui.keyUp(key)
    return

def isCollide(background_color, data):
    for i in range(300, 360):
        for j in range(440, 485):
            if (data[i, j] < 170 and background_color == 255) or (data[i, j] >= 170 and background_color < 255):
                hit("up")
                return
  
        for j in range(160, 440):
            if (data[i, j] < 170 and background_color == 255)or (data[i, j] >= 170 and background_color < 255):
                hit("down")
                return
    return

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options=options)
try:
    driver.get("chrome://dino/")
except:
    sleep(2)
    game = driver.find_element_by_id('t')
    game.send_keys(Keys.SPACE)

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        background_color = data[10, 700]
        isCollide(background_color, data)
