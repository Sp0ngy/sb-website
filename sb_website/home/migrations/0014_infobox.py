# Generated by Django 4.0.1 on 2022-01-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_subscription_country_alter_subscription_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(blank=True)),
                ('info_name', models.CharField(max_length=100, verbose_name='Info Name')),
                ('info_text', models.TextField(verbose_name='Info Text')),
            ],
        ),
    ]
