# Generated by Django 3.0.4 on 2020-03-15 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20200315_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='photo',
            field=models.ImageField(upload_to='produtos'),
        ),
    ]