# Generated by Django 4.0.1 on 2022-04-04 15:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_alter_publication_authors_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='reference',
            field=models.CharField(default=django.utils.timezone.now, help_text='Link to another online source, e.g. pubmed.com', max_length=600, verbose_name='Reference Link'),
            preserve_default=False,
        ),
    ]