# Generated by Django 2.2.7 on 2019-11-08 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField()),
                ('link', models.URLField()),
                ('alias', models.TextField()),
            ],
        ),
    ]
