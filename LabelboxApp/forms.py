from django import forms
from django.db import models
from LabelboxApp.models import Album


class HotelForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['name', 'Job', 'release_date','hotel_Main_Img']