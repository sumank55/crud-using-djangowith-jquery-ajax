# Generated by Django 3.2.7 on 2021-09-07 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
