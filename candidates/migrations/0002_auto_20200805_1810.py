# Generated by Django 2.2.6 on 2020-08-05 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='carrer_vision',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='carrer_vision'),
        ),
    ]
