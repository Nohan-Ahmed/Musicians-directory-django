from django.shortcuts import render, redirect
from album import models


def home(req):
    albums = models.AlbumModel.objects.all()
    print(albums)
    return render(req, 'index.html', {'albums': albums})
