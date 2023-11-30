import os
import webbrowser

import requests
import cv2  # импорт библиотеки, предназначенной для работы с изображениями

import re
from re import sub
from decimal import Decimal
import io
from datetime import datetime

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


def bypass_yandex_images_captcha():
    try:
        captcha_button = browser.find_element(By.CLASS_NAME, "CheckboxCaptcha-Button")
        captcha_button.click()
        browser.implicitly_wait(10000)
    except:
        print("Unknown error occurred\n")
        return


base_url = "https://yandex.ru/images/"
url1 = "https://yandex.ru/images/search?text=*bay%20horse"
url2 = "https://yandex.ru/images/search?text=*zebra*"
fo = webdriver.FirefoxOptions()
fp = webdriver.FirefoxProfile()

browser = webdriver.Firefox()
browser.maximize_window()

for url in url1, url2:
    print(f"Вывод изображений по ссылке: {url}\n")
    browser.get(url)
    if browser.title == "Ой!":
        bypass_yandex_images_captcha()

    image_divs = browser.find_elements(By.CLASS_NAME, "SimpleImage")
    while len(image_divs) < 1200:
        load_button_div = browser.find_element(By.CLASS_NAME, "SerpList-LoadContent")
        load_button = load_button_div.find_element(By.TAG_NAME, "button")
        load_button.click()
        image_divs = browser.find_elements(By.CLASS_NAME, "SimpleImage")

    for image_div in image_divs:
        image_link = image_div.find_element(By.TAG_NAME, "img").get_property("src")
        print(image_link, end="\n")
browser.close()
# image = cv2.imread(path_to_file)   прочтение изображения из файла, path_to_file - путь до файла-изображения
# cv2.imwrite(path_to_save_image, image)   сохранение изображения по заданному пути, например, path_to_folder/image_name.jpg

# print(image.shape)  # распечатать размер прочитанного изображения

# инструкции для просмотра изображения
# cv2.imshow(window_name, image)
# cv2.waitKey(0)
