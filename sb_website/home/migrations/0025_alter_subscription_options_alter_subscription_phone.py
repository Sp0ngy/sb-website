# Generated by Django 4.0.1 on 2022-04-04 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_alter_subscription_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'verbose_name': 'Subscription'},
        ),
        migrations.AlterField(
            model_name='subscription',
            name='phone',
            field=models.CharField(max_length=20, unique=True, verbose_name='Phone'),
        ),
    ]
