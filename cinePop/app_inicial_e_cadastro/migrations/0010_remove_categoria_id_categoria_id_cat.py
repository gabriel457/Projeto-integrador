# Generated by Django 4.2.6 on 2023-11-15 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_inicial_e_cadastro', '0009_remove_categoria_id_cat_categoria_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='id',
        ),
        migrations.AddField(
            model_name='categoria',
            name='id_cat',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]