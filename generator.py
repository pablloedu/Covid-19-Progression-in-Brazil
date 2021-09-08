import datetime
import csv
import requests
from modules.helpers import *
url = 'https://api.covid19api.com/dayone/country/brazil'
resp = requests.get(url)

raw_data = resp.json()

final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'],
                      obs['Recovered'], obs['Active'], obs['Date']])
final_data.insert(0, ['confirmados', 'obitos',
                  'recuperados', 'ativos', 'data'])

CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

for i in range(1, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10]

with open('brasil-covid.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)

for i in range(1,len(final_data)):
    final_data[i][DATA] = datetime.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')

y_data1 = []
for obs in final_data[1::10]:
    y_data1.append(obs[CONFIRMADOS])

y_data2 = []
for obs in final_data[1::10]:
    y_data2.append(obs[RECUPERADOS])

labels = ['Confirmados', ' Recuperados']

x = []
for obs in final_data[1::10]:
    x.append(obs[DATA].strftime('%d/%m/%Y'))

chart = creat_chart(x,[y_data1, y_data2], labels, title="Confirmados VS Recuperados")
chart_content = get_api_chart(chart)
save_image('primeiro-grafico.png', chart_content)

url_base = 'https://quickchart.io/chart'

link = (f'{url_base}?c={str(chart)}')

save_image('qr-code.png', get_api_qrcode(link))
