# Generated by Django 5.0.3 on 2024-04-01 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
