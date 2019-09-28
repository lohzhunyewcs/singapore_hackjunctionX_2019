from django.shortcuts import render, render_to_response
from django.http import HttpResponse, StreamingHttpResponse
from yolo import detect
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm
from PIL import Image
import base64
from .models import Item

import cv2
import numpy as np
import requests

# Create your views here.
def index(request):
    context = {
        "message": "Hello World",
        'canvas': '',
        'fresh': True
    }
    return render(request, "ecommerce/index.html", context)

def writeFile(file_name, bits):
    imgdata = base64.b64decode(bits)
    filename = f'{file_name}'  # I assume you have a way of picking unique filenames
    with open(f'/home/khaifung/Desktop/singapore_hackjunctionX_2019/web/yolo/data/images/{filename}', 'wb') as f:
        f.write(imgdata)

import base64
import re

def decode_base64(data, altchars=b'+/'):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)  # normalize
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'='* (4 - missing_padding)
    return base64.b64decode(data, altchars)

# API
@csrf_exempt
def process_image(request):
    file_name = 'zy_whatever_1'#input("Insert file name: ")
    file_name += '.png'
    # print("Collecting Result")
    # # print(f'request.get("img"): {request.get("img")}')
    # print(f'request: {type(request.body)}')
    # print(f'request.FILES.get(url): {request.FILES.get("url")}')
    imageBits = request.body
    print(f'{str(imageBits)[:100]}')
    print(f'type: {type(imageBits)}')
    imageBits = imageBits[22:]
    pad = len(imageBits)% 4
    imageBits += b"="*pad
    print(f'len of imagebits: {len(imageBits)}')
    print(f'request: {type(request.body)}')
#     cv2.imshow('', request.body)
#     print(f'request.body.get("imgBase64") : {request.body.get("imgBase64")}')
    writeFile(file_name, imageBits)
    # images 0.5 0.5 data/images/dog.jpg data/images/office.jpg
    # writeFile()
    result = detect.main('images', 0.5, 0.5, [f'/home/khaifung/Desktop/singapore_hackjunctionX_2019/web/yolo/data/images/{file_name}'])
    print(f'result: {result}')
    return HttpResponse({'result': 'success'}, content_type='json')

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             (request.FILES['file'])
#     result = detect.main('images', 0.5, 0.5, image)
#     print(result)
#     return True


def SellView(request):
    all_sell_items = Item.objects.all()
    return render(request, 'ecommerce/selling_list.html',
        {'all_sell_items': all_sell_items})

#template for tabs
def charts(request):
    return render(request, 'ecommerce/charts.html')