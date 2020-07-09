# Generated by Django 3.0.8 on 2020-07-09 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switch',
            name='switch_type',
            field=models.CharField(choices=[('LI', 'Linear'), ('TA', 'Tactile'), ('CL', 'Clicky'), ('MI', 'Other')], default='LI', max_length=2),
        ),
    ]
