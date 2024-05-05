from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.


def add_album(req):
    if req.method == 'POST':
        form = forms.AlbumForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('album:add_album')
    else:
        form = forms.AlbumForm()
    return render(req, './album/add_album.html', {'form': form})


def delete_album(req, id):
    models.AlbumModel.objects.get(pk=id).delete()
    return redirect('home')


def edit_album(req, id):
    album = models.AlbumModel.objects.get(pk=id)
    if req.method == 'POST':
        form = forms.AlbumForm(req.POST, isinstance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.AlbumForm(instance=album)
    return render(req, './album/add_album.html', {'form': form})
