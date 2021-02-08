# Generated by Django 3.1.6 on 2021-02-08 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_content', models.CharField(max_length=250)),
                ('work_hours_per_day', models.IntegerField(default=0)),
                ('work_money', models.IntegerField(default=0)),
                ('work_company', models.CharField(max_length=250)),
                ('work_country', models.CharField(max_length=250)),
            ],
        ),
    ]
