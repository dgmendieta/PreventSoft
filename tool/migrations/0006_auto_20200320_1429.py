# Generated by Django 2.2.3 on 2020-03-20 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0005_remove_tool_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tool/'),
        ),
    ]