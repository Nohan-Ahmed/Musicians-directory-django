from django.db import models
from musician.models import MusicianModel

# Create your models here.
class AlbumModel(models.Model):
    AlbumName = models.CharField(max_length=50)
    musician = models.ForeignKey(to=MusicianModel,
                                 on_delete=models.CASCADE)
    Album_release_date = models.DateTimeField(auto_now_add=True)
    Rating_between = models.CharField(max_length=1, choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    def __str__(self) -> str:
        return self.AlbumName