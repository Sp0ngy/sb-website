# Generated by Django 4.0.1 on 2022-02-28 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_articlecategory_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, upload_to='article/images')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.article')),
            ],
        ),
    ]
