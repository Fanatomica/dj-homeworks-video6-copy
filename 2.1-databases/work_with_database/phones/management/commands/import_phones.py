import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            phone = Phone(id = phone['id'], name = phone['name'], image = phone['image'], price = phone['price'],
                          release_date = phone['release_date'], lte_exists = phone['lte_exists'], slug = ['null'])
            phone.slug = slugify(phone.name)
            phone.save()