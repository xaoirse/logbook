# Generated by Django 3.0.2 on 2020-02-04 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbookapp', '0002_auto_20200123_0418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inter_dep',
            name='master',
        ),
        migrations.AddField(
            model_name='inter_dep',
            name='master',
            field=models.ManyToManyField(to='logbookapp.Masters', verbose_name='استاد'),
        ),
    ]