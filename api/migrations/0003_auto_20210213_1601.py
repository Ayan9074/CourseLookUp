# Generated by Django 3.1.6 on 2021-02-13 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_course_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='img',
            field=models.TextField(),
        ),
    ]
