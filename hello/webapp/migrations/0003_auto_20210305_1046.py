# Generated by Django 3.1.7 on 2021-03-05 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20210305_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.TextField(choices=[('food', 'food'), ('cell_phones', 'Cell_phones'), ('accessories', 'accessories')], default='other'),
        ),
    ]