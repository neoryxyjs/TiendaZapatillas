# Generated by Django 4.2.3 on 2023-07-06 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_zapatilla_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zapatilla',
            name='info1',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Info1'),
        ),
        migrations.AlterField(
            model_name='zapatilla',
            name='info2',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Info2'),
        ),
        migrations.AlterField(
            model_name='zapatilla',
            name='info3',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Info3'),
        ),
    ]
