# Generated by Django 2.2.3 on 2020-03-23 13:35

import APR.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APR', '0012_auto_20200320_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apr',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apr',
            name='documentnumber',
            field=models.IntegerField(default=APR.models.set_documentnumber, unique=True),
        ),
        migrations.AlterField(
            model_name='aprline',
            name='epps',
            field=models.ManyToManyField(blank=True, null=True, to='EPP.EPP'),
        ),
        migrations.AlterField(
            model_name='aprline',
            name='hazards',
            field=models.ManyToManyField(blank=True, null=True, to='hazard.Hazard'),
        ),
        migrations.AlterField(
            model_name='aprline',
            name='precautions',
            field=models.ManyToManyField(blank=True, null=True, to='precaution.Precaution'),
        ),
        migrations.AlterField(
            model_name='aprline',
            name='tools',
            field=models.ManyToManyField(blank=True, null=True, to='tool.Tool'),
        ),
    ]