import os
import requests
import cv2  # импорт библиотеки, предназначенной для работы с изображениями

import re
from re import sub
from decimal import Decimal
import io
from datetime import datetime

from bs4 import BeautifulSoup


url_base = "https://yandex.ru/images/"
url = "https://yandex.ru/images/search?text=*bay%20horse"
html_page_text = requests.get(url).text
soup = BeautifulSoup(html_page_text, 'lxml')

block = soup.find('div', class_="SerpList", recursive=True)
image_divs = block.find_all('div', class_="SimpleImage", recursive=True, limit=10)
for image_div in image_divs:
    image_link = image_div.find('img', class_="SimpleImage-Image").get('src')
    print(image_link, end="\n")



#image = cv2.imread(path_to_file)   прочтение изображения из файла, path_to_file - путь до файла-изображения
#cv2.imwrite(path_to_save_image, image)   сохранение изображения по заданному пути, например, path_to_folder/image_name.jpg

#print(image.shape)  # распечатать размер прочитанного изображения

# инструкции для просмотра изображения
#cv2.imshow(window_name, image)
#cv2.waitKey(0)