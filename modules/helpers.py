from typing import Text
import requests as r
from PIL import Image
from urllib.parse import quote
from requests.models import Response

def get_datasets(y, labels):
    if type(y[0]) == list:
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'label': labels[i],
                'data': y[i]
            })
        return datasets
    else:
        return [{
            'label': labels[0],
            'data': y
        }]


def set_title(title=""):
    if title != "":
        display = 'true'
    else: display = 'false'

    return {
        'title': title,
        'display': display
    }

def creat_chart(x, y, labels, kind='bar', title=""):
    datasets = get_datasets(y, labels)
    options = set_title(title)
    chart = {
        'type': kind,
        'data': {
            'labels': x,
            'datasets': datasets
        },
        'options': options
    }
    return chart

def get_api_chart(chart):
    url_base = 'https://quickchart.io/chart'
    resp = r.get(f'{url_base}?c={str(chart)}')
    return resp.content

def save_image(path, content):
    with open(path, 'wb') as image:
        image.write(content)

def get_api_qrcode(link):
    text = quote(link) #parsing do link para url
    url_base = 'https://quickchart.io/qr'
    resp = r.get(f'{url_base}?text={text}')
    return resp.content

