# Generated by Django 3.1.1 on 2020-10-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='myapp')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('activated', models.BooleanField(default=False)),
            ],
        ),
    ]
