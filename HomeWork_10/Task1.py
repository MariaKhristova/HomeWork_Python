#Программа получает данные о курсе доллара из ЦБ РФ и стоит график от начала текущего года
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import requests
import xml.etree.ElementTree as ET

today = datetime.today()
url = f'http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=01/01/{today.year}&date_req2={today.day:02d}/{today.month:02d}/{today.year}&VAL_NM_RQ=R01235'

res = requests.get(url)
res_xml = res.text

arr = []
arr2 = []
tree = ET.fromstring(res_xml)
for element in tree:
    val = element[1]
    arr.append(float(val.text.replace(',', '.')))
    dat = datetime.strptime(element.attrib['Date'], '%d.%m.%Y')
    arr2.append(dat)


print(arr2)

y = np.array(arr)
x = np.array(arr2)

fig, ax = plt.subplots()
ax.plot(x, y)

plt.title("Курс доллара от начала года")
plt.xlabel("Дата")
plt.ylabel("руб.")
plt.grid()

plt.show()
