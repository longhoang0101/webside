# Generated by Django 2.2.7 on 2020-05-23 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0007_contact_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_image',
            field=models.ImageField(default='NULL', upload_to='static/Image'),
        ),
    ]
