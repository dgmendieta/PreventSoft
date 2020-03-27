# Generated by Django 2.2.3 on 2020-02-24 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hazard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Precaution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('precautions', models.ManyToManyField(blank=True, to='hazard.Hazard')),
            ],
        ),
    ]