# Generated by Django 2.2.6 on 2020-08-05 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_id', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('address_number', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('year', models.CharField(max_length=32)),
                ('month', models.CharField(max_length=32)),
                ('day', models.CharField(max_length=32)),
                ('univ', models.CharField(max_length=128)),
                ('department', models.CharField(max_length=128)),
                ('course', models.CharField(max_length=128)),
                ('enroll_date', models.CharField(max_length=128)),
                ('graduate_date', models.CharField(max_length=128)),
                ('carrer_vision', models.ImageField(upload_to='carrer_vision')),
                ('output', models.ImageField(blank=True, default=None, null=True, upload_to='output')),
            ],
        ),
    ]
