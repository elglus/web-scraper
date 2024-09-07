from urllib import request

pages = request.urlopen("https://market.yandex.ru/product--macbook-air-13-2024/77121092?sku=102832949157&uniqueId=901698")
print(pages)