# Generated by Django 5.0.6 on 2024-08-17 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='category',
            field=models.CharField(default='uncategorized', max_length=100),
        ),
    ]
