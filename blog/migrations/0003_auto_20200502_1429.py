# Generated by Django 3.0.5 on 2020-05-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200502_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date updated'),
        ),
    ]
