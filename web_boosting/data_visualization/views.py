from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def eda(request):
    return HttpResponse("<h1>Исследовательский анализ данных</h1>")

def test(request):
    return HttpResponse("<h1>Тест модели</h1>")

def result(request):
    return HttpResponse("<h1>Результат итоговой работы</h1>")

def csv_upload(request):
    return render(request, "csv-import-data.html")
