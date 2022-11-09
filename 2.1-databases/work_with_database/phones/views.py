from django.shortcuts import render, redirect
from django.core.management import call_command
from phones.models import Phone
#from phones.management.commands.import_phones import Command


def index(request):
    call_command('import_phones')
    return redirect('catalog')


def show_catalog(request):
    instr = request.GET.get("sort", "name")
    if instr == 'name':
        phone_objects = Phone.objects.all().order_by("name")
    elif instr == 'min_price':
        phone_objects = Phone.objects.all().order_by("price")
    elif instr == 'max_price':
        phone_objects = Phone.objects.all().order_by("-price")
    else:
        phone_objects = Phone.objects.all()
    template = 'catalog.html'
    context = {'phones' : phone_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_objects = Phone.objects.all()
    for c in phone_objects:
        if c.lte_exists == 'False':
            c.lte_exists = ""
        if c.slug == slug:
            phone_object = Phone(id=c.id, name=c.name, image=c.image, price=c.price,
                                    release_date=c.release_date, lte_exists=c.lte_exists, slug=c.slug)
    context = {'phone' : phone_object}
    return render(request, template, context)