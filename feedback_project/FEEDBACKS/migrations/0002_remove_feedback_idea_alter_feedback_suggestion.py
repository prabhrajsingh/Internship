# Generated by Django 4.0.5 on 2022-07-03 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FEEDBACKS', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='idea',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='suggestion',
            field=models.TextField(),
        ),
    ]
