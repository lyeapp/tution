# Generated by Django 3.2.3 on 2022-05-04 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuitionapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Parentname',
            field=models.CharField(max_length=150, verbose_name='Parentname'),
        ),
    ]