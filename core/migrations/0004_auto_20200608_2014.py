# Generated by Django 3.0.6 on 2020-06-08 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200608_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='content',
            field=models.TextField(max_length=800, verbose_name='Contenido'),
        ),
    ]
