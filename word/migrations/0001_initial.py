# Generated by Django 4.1.4 on 2022-12-23 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField()),
                ('meaning', models.TextField()),
                ('test_num', models.IntegerField()),
                ('genre', models.TextField()),
                ('favorite', models.IntegerField()),
            ],
        ),
    ]
