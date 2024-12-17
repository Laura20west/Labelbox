from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from LabelboxApp.models import Album
from .forms import HotelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
 Albums = Album.objects.all()
 return render(request, 'home.html', {'Albums': Albums})
def about(request):
 return render(request, 'about.html')


# Create your views here.


def image(request):
  if request.method == 'POST':
   form = HotelForm(request.POST, request.FILES)

   if form.is_valid():
    form.save()
    Albums = Album.objects.all()
    return render(request, 'home.html', {'Albums': Albums})
  else:
   form = HotelForm()
   return render(request, 'image.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


