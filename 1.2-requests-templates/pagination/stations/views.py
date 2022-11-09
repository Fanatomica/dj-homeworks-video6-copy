from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
import csv
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):

    with open(settings.BUS_STATION_CSV, newline='') as csvfile:
        data_ = csv.DictReader(csvfile)
        data = list(data_)

    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(data, 10)
    page = paginator.get_page(page_number)

    context = {
         'bus_stations': page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)


