# Generated by Django 4.2.3 on 2023-07-06 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_alter_zapatilla_info1_alter_zapatilla_info2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zapatilla',
            name='descripcion',
            field=models.CharField(max_length=300, verbose_name='Descripcion'),
        ),
    ]
