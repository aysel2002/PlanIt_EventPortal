# Generated by Django 3.2.3 on 2021-05-25 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scmapp', '0002_auto_20210525_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='upcoming',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField(verbose_name='Y-m-d')),
                ('time', models.TimeField()),
                ('duration', models.IntegerField()),
            ],
        ),
    ]
