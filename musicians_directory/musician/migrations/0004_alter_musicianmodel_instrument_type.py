# Generated by Django 5.0.3 on 2024-05-04 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0003_alter_musicianmodel_instrument_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicianmodel',
            name='instrument_type',
            field=models.CharField(choices=[('Piano', 'Piano'), ('Guitar', 'Guitar'), ('Drums', 'Drums'), ('Violin', 'Violin')], max_length=50),
        ),
    ]
