# Generated by Django 2.2.3 on 2020-02-28 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APR', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apr',
            name='comments',
            field=models.TextField(blank=True),
        ),
    ]
