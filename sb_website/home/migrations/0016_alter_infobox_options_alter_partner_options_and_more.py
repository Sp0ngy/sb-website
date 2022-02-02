# Generated by Django 4.0.1 on 2022-02-01 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_infobox_options_alter_partner_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='infobox',
            options={'verbose_name': 'Infoboxe'},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name': 'Partner'},
        ),
        migrations.AddField(
            model_name='subscription',
            name='date_of_birth',
            field=models.DateField(blank=True, default=2022),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscription',
            name='internal_note',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='infobox',
            name='info_text',
            field=models.TextField(help_text='Infoboxes will only be shown in English on the website.', verbose_name='Info Text'),
        ),
    ]
