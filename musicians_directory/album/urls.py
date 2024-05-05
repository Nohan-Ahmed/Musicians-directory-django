from django.urls import path
from . import views

app_name = 'album'
urlpatterns = [
    path('add/', views.add_album, name='add_album'),
    path('delete/<int:id>', views.delete_album, name='delete_album'),
    path('edit/<int:id>', views.edit_album, name='edit_album'),
]
