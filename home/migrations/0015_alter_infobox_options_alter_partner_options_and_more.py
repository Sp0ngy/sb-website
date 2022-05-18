# Generated by Django 4.0.1 on 2022-01-24 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_infobox'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='infobox',
            options={'verbose_name': 'Infobox'},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name': 'PartnerTEST'},
        ),
        migrations.AlterModelOptions(
            name='subscription',
            options={'verbose_name': 'Subscriber'},
        ),
        migrations.AlterField(
            model_name='partner',
            name='image',
            field=models.ImageField(default='home/placeholder.png', upload_to='home/'),
        ),
    ]