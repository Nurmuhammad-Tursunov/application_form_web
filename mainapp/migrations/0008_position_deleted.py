# Generated by Django 4.2.7 on 2023-11-07 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_remove_application_degree_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]