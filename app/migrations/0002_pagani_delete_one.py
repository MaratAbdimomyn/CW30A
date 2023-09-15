# Generated by Django 4.2.5 on 2023-09-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagani',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=40)),
                ('models_name', models.CharField(max_length=40)),
                ('models_year', models.IntegerField()),
                ('power', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='One',
        ),
    ]
