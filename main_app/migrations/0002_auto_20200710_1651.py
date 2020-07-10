# Generated by Django 3.0.8 on 2020-07-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyboard',
            name='case',
        ),
        migrations.AddField(
            model_name='keyboard',
            name='case',
            field=models.ManyToManyField(to='main_app.Case'),
        ),
        migrations.RemoveField(
            model_name='keyboard',
            name='keycap',
        ),
        migrations.AddField(
            model_name='keyboard',
            name='keycap',
            field=models.ManyToManyField(to='main_app.Keycap'),
        ),
        migrations.RemoveField(
            model_name='keyboard',
            name='pcb',
        ),
        migrations.AddField(
            model_name='keyboard',
            name='pcb',
            field=models.ManyToManyField(to='main_app.PCB'),
        ),
        migrations.RemoveField(
            model_name='keyboard',
            name='stabilizer',
        ),
        migrations.AddField(
            model_name='keyboard',
            name='stabilizer',
            field=models.ManyToManyField(to='main_app.Stabilizer'),
        ),
        migrations.RemoveField(
            model_name='keyboard',
            name='switch',
        ),
        migrations.AddField(
            model_name='keyboard',
            name='switch',
            field=models.ManyToManyField(to='main_app.Switch'),
        ),
    ]
