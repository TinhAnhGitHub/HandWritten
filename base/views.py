from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import CanvasImage
from PIL import Image
from io import BytesIO
import base64, secrets
from django.core.files.base import ContentFile
from .LeNet import LeNet5
from torch import load, device
import torch 
from torchvision import transforms
from numpy import argmax
# Create your views here.
INIT = True
def get_image_from_data_url( data_url, resize=True):
    _format, _dataurl       = data_url.split(';base64,')
    _filename, _extension = 'digit_picture', 'png'
    file = ContentFile( base64.b64decode(_dataurl), name=f"{_filename}.{_extension}")
    if resize:
        image = Image.open(file)
        image_io = BytesIO()
        image.save(image_io, format=_extension)
        file = ContentFile( image_io.getvalue(), name=f"{_filename}.{_extension}" )
    return file #, ( _filename, _extension )

def home(request):
   
    img = CanvasImage.objects.get(id=5)
    print(request.method)
    if request.method == 'POST':
        imgdata = get_image_from_data_url(request.POST.get('image'))

        img.image.delete()
        img.image = imgdata
        
        model = LeNet5(10)
        model.load_state_dict(load('../django-digit/base/LeNet.pt',map_location=device('cpu')))

        data = Image.open(imgdata).convert("L")
        

        
        resize_transform = transforms.Compose(
            [transforms.Resize((32, 32)),
            transforms.ToTensor(),
            transforms.Normalize((0,), (1,))  # standarize data with zero means and unit variance
            ]
            )
        data = resize_transform(data)
        data = data.unsqueeze(0)
        if  not torch.all(data == 0).item():
            request.session['INIT2'] = False
        if torch.all(data == 0).item():
            if INIT:
                context = {"make_pred": False,
                           "result": "Please draw on the canvas"}
                
           
            return render(request, 'main.html', context)
        
        _, output = model(data)
        img.result = str(argmax(output.detach().numpy()))
        img.save()
        
        context = {'make_pred': True, 'result': "Your image produces number " + img.result}
    else:
        context = {'make_pred': False, 'result': "Please draw on the canvas"}
              
    return render(request, 'main.html', context)
