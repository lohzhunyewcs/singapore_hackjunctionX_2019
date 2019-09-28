from django.shortcuts import render
from django.http import HttpResponse
from yolo import detect
from django.views.decorators.csrf import csrf_exempt

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
