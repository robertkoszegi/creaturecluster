# Generated by Django 3.2.6 on 2021-09-06 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20210906_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creature',
            name='diet',
            field=models.CharField(choices=[('animal', 'Animal'), ('plant', 'Plant')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='snack',
            name='snacktype',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
