import os
import requests
import cv2
import numpy as np

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


def download_image_by_url(image_url):
    req = requests.get(image_url)
    arr = np.asarray(bytearray(req.content), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)
    return img


base_url = "https://yandex.ru/images/"
url1 = "https://yandex.ru/images/search?text=*bay%20horse"
url2 = "https://yandex.ru/images/search?text=*zebra*"
fo = webdriver.FirefoxOptions()
fp = webdriver.FirefoxProfile()
try:
    os.mkdir("dataset")
    os.mkdir("dataset\\bay horse")
    os.mkdir("dataset\\zebra")
except FileExistsError:
    print("Папка уже существует")

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

    image_num = 0
    for image_div in image_divs:
        image_link = image_div.find_element(By.TAG_NAME, "img").get_property("src")
        print(image_link, end="\n")
        image = download_image_by_url(image_link)
        image_name = str(image_num)
        while len(image_name) < 4:
            image_name = "0" + image_name
        image_num += 1
        if url == url1:
            cv2.imwrite(f"dataset\\bay horse\{image_name}.jpg", image)
        else:
            cv2.imwrite(f"dataset\\zebra\{image_name}.jpg", image)
browser.close()
