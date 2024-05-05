from django.db import models


# Create your models here.
class MusicianModel(models.Model):
    CHOICES = [
        ('Piano', 'Piano'),
        ('Guitar', 'Guitar'),
        ('Drums', 'Drums'),
        ('Violin', 'Violin'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    instrument_type = models.CharField(max_length=50, choices=CHOICES)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
