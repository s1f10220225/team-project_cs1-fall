# Generated by Django 4.1.4 on 2023-01-05 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0002_test_word_list_name_alter_word_favorite_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=225, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='word',
            name='favorite',
        ),
        migrations.RemoveField(
            model_name='word',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='word',
            name='list_name',
        ),
        migrations.RemoveField(
            model_name='word',
            name='test_num',
        ),
        migrations.CreateModel(
            name='Listinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_num', models.IntegerField()),
                ('list_name', models.CharField(max_length=225, null=True)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Genre', to='word.genre')),
            ],
        ),
        migrations.AddField(
            model_name='word',
            name='belonging_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_info', to='word.listinfo'),
        ),
    ]
