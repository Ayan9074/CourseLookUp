# Generated by Django 3.1.6 on 2021-02-14 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210213_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='web',
            field=models.TextField(default='none'),
        ),
    ]
