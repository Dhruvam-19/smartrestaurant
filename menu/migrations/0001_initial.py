# Generated by Django 3.1 on 2021-01-09 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.TextField(blank=True, max_length=30, null=True)),
                ('photo', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='menu')),
                ('type', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]