from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == 'name':
        phone_objects = Phone.objects.order_by('name')
        phones = []
        for p in phone_objects:
            voc = {}
            voc['name'] = p.name
            voc['price'] = p.price
            voc['image'] = p.image
            voc['slug'] = p.slug
            phones.append(voc)
        context = {
            'phones': phones,
        }
    elif sort == 'min_price':
        phone_objects = Phone.objects.order_by('price')
        phones = []
        for p in phone_objects:
            voc = {}
            voc['name'] = p.name
            voc['price'] = p.price
            voc['image'] = p.image
            voc['slug'] = p.slug
            phones.append(voc)
        context = {
            'phones': phones,
        }
    elif sort == 'max_price':
        phone_objects = Phone.objects.order_by('-price')
        phones = []
        for p in phone_objects:
            voc = {}
            voc['name'] = p.name
            voc['price'] = p.price
            voc['image'] = p.image
            voc['slug'] = p.slug
            phones.append(voc)
        context = {
            'phones': phones,
        }
    else:
        phone_objects = Phone.objects.all()
        phones = []
        for p in phone_objects:
            voc = {}
            voc['name'] = p.name
            voc['price'] = p.price
            voc['image'] = p.image
            voc['slug'] = p.slug
            phones.append(voc)
        context = {
            'phones': phones,
        }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.filter(slug=slug)
    phone = {}
    for p in phone_object:
        phone['name'] = p.name
        phone['price'] = p.price
        phone['image'] = p.image
        phone['release_date'] = p.release_date
        phone['lte_exists'] = p.lte_exists
    context = {
        'phone': phone,
    }
    return render(request, template, context)

