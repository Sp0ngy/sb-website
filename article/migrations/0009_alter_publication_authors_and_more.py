# Generated by Django 4.0.1 on 2022-04-04 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_alter_publication_authors_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='authors',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='List of Authors'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='conclusion',
            field=models.TextField(blank=True, null=True, verbose_name='Conclusion'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='methods',
            field=models.TextField(blank=True, null=True, verbose_name='Methods'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='result',
            field=models.TextField(blank=True, null=True, verbose_name='Result'),
        ),
    ]
