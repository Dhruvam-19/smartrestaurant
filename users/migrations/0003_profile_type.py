# Generated by Django 3.1 on 2021-02-19 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210105_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='type',
            field=models.CharField(blank=True, choices=[('M', 'Manager'), ('C', 'Chef'), ('W', 'Waiter')], max_length=50, null=True),
        ),
    ]
