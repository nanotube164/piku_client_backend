# Generated by Django 3.1.3 on 2022-10-28 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20221028_0835'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductUser',
        ),
    ]