# Generated by Django 4.0.1 on 2022-01-14 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('image', models.ImageField(height_field=140, upload_to='partneruploads/', width_field=140)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.partnertype')),
            ],
        ),
    ]
