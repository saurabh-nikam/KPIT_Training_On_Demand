# Generated by Django 3.2.7 on 2021-10-28 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=50)),
                ('dateTimeOfUpload', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
