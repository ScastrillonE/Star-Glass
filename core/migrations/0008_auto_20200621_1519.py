# Generated by Django 3.0.6 on 2020-06-21 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_popup'),
    ]

    operations = [
        migrations.AddField(
            model_name='popup',
            name='content2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='popup',
            name='title',
            field=models.CharField(max_length=250, null=True),
        ),
    ]