# Generated by Django 3.2.6 on 2021-08-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movierecommender', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='vote_average',
            field=models.FloatField(default=0),
        ),
    ]