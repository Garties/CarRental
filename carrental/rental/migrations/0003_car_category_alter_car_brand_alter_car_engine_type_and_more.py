# Generated by Django 5.0.3 on 2024-05-22 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_remove_user_address_address_delete_adress'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='category',
            field=models.CharField(choices=[('suv', 'SUV'), ('miejski', 'miejski'), ('terenowy', 'terenowy'), ('van', 'VAN'), ('sportowy', 'sportowy')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=50, verbose_name='Marka'),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine_type',
            field=models.CharField(choices=[('benzynowy', 'Benzynowy'), ('diesel', 'Diesel'), ('hybrydowy', 'Hybrydowy'), ('elektryczny', 'Elektryczny'), ('wodorowy', 'Wodorowy')], max_length=20, verbose_name='Typ silnika'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=50, verbose_name='Model'),
        ),
    ]