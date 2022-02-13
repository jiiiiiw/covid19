import requests
from django.shortcuts import render

# Create your views here.

def covid19():
    URL = "http://openapi.seoul.go.kr:8088/547171685163686f35324270474f6e/json/TbCorona19CountStatus/1/365/"
    data = requests.get(URL).json()['TbCorona19CountStatus']['row']
    return data



def home(requests):
    data = covid19()
    data_week = data[:7]
    today = data[0]
    death = int(data[0]['DEATH']) - int(data[1]['DEATH'])
    recover = int(data[0]['RECOVER']) - int(data[1]['RECOVER'])
    data.reverse()
    data_week.reverse()

    return render(requests, 'home.html', {"data_list":data, "data_week":data_week, "today":today, "death":death, "recover":recover})