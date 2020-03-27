# Generated by Django 2.2.3 on 2020-03-08 23:36

import APR.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APR', '0006_auto_20200304_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='aprline',
            name='activities',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apr',
            name='documentnumber',
            field=models.IntegerField(default=APR.models.set_documentnumber, unique=True),
        ),
        migrations.RemoveField(
            model_name='aprline',
            name='epps',
        ),
        migrations.AddField(
            model_name='aprline',
            name='epps',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='aprline',
            name='hazards',
        ),
        migrations.AddField(
            model_name='aprline',
            name='hazards',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='aprline',
            name='precautions',
        ),
        migrations.AddField(
            model_name='aprline',
            name='precautions',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
