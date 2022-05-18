# Generated by Django 4.0.1 on 2022-02-02 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_infobox_options_alter_partner_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='phone',
            field=models.CharField(default='01738888899', max_length=20, verbose_name='Phone'),
            preserve_default=False,
        ),
    ]