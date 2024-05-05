from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def add_musician(req):
    if req.method=='POST':
        form = forms.MusicianForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('add_musician')
    else:
        form = forms.MusicianForm()
    return render(req, './musician/add_musician.html', {'form':form})

def edit_musician(req, id):
    musician = models.MusicianModel.objects.get(pk=id)
    if req.method=='POST':
        form = forms.MusicianForm(req.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = forms.MusicianForm(instance=musician)
    return render(req, './musician/add_musician.html', {'form':form})