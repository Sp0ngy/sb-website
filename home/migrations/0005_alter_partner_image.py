# Generated by Django 4.0.1 on 2022-01-15 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_partner_title_alter_partner_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='image',
            field=models.ImageField(default='home/placeholder.png', upload_to='home/media/partneruploads/'),
        ),
    ]
