from django.shortcuts import render
from django.http import HttpResponse
from yolo import detect
from django.views.decorators.csrf import csrf_exempt
from .models import Item

import requests

# Create your views here.
def index(request):
    context = {
        "message": "Hello World"
    }
    return render(request, "ecommerce/index.html", context)


# API
@csrf_exempt
def process_image(request):
    print("Collecting Result")
    image = request.FILES.get('img')
    # images 0.5 0.5 data/images/dog.jpg data/images/office.jpg
    result = detect.main('images', 0.5, 0.5, image)
    print(result)
    return True


def SellView(request):
    all_sell_items = Item.objects.all()
    return render(request, 'selling_list.html',
        {'all_sell_items': all_sell_items})

