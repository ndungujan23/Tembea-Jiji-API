# Generated by Django 3.0.2 on 2020-01-18 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='busstop',
            options={'ordering': ('stop_name',)},
        ),
        migrations.AlterModelOptions(
            name='route',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='stage',
            options={'ordering': ('stage_name',)},
        ),
        migrations.RenameField(
            model_name='route',
            old_name='route_number',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='busstop',
            name='route',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='route',
        ),
        migrations.AddField(
            model_name='route',
            name='stages',
            field=models.ManyToManyField(to='routes.Stage'),
        ),
        migrations.AddField(
            model_name='route',
            name='stops',
            field=models.ManyToManyField(to='routes.BusStop'),
        ),
    ]
