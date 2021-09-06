# Generated by Django 3.2.6 on 2021-09-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_creature_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snack',
            name='color',
        ),
        migrations.AddField(
            model_name='creature',
            name='snacks',
            field=models.ManyToManyField(to='main_app.Snack'),
        ),
        migrations.AddField(
            model_name='snack',
            name='snacktype',
            field=models.CharField(default='animal', max_length=20),
        ),
        migrations.AlterField(
            model_name='creature',
            name='diet',
            field=models.CharField(max_length=10),
        ),
    ]
