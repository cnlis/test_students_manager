# Generated by Django 4.1.7 on 2023-03-11 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='teachers',
            field=models.ManyToManyField(related_name='teachers', to='students.teacher'),
        ),
    ]