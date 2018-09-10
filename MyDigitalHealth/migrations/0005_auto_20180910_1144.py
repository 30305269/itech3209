# Generated by Django 2.0.5 on 2018-09-10 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyDigitalHealth', '0004_auto_20180910_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cards',
            name='card_group',
        ),
        migrations.RemoveField(
            model_name='sorted_package',
            name='card_group',
        ),
        migrations.AddField(
            model_name='card_groups',
            name='cards',
            field=models.ManyToManyField(to='MyDigitalHealth.Cards'),
        ),
        migrations.RemoveField(
            model_name='sorted_package',
            name='cards',
        ),
        migrations.AddField(
            model_name='sorted_package',
            name='cards',
            field=models.ManyToManyField(to='MyDigitalHealth.Cards'),
        ),
    ]
