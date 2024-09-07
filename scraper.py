from selenium import webdriver
from selenium.webdriver.common.by import By
import re

url = "https://market.yandex.ru/product--macbook-air-13-2024/77121092?sku=102833204153&uniqueId=16327879&do-waremd5=eU2yNcDhY3IAuvI5gCgpbw&sponsored=1&nid=26895412"

driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(1)

price = driver.find_element(by=By.CLASS_NAME, value="Jdxhz").text
price = re.sub(r"\D", "", price)

print(price)