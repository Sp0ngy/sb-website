# Generated by Django 4.0.1 on 2022-03-05 18:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_remove_article_paragraph_article_paragraph1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paragraph',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paragraph',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='paragraph1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_paragraph', to='article.paragraph'),
        ),
        migrations.AlterField(
            model_name='article',
            name='paragraph2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_paragraph', to='article.paragraph'),
        ),
        migrations.AlterField(
            model_name='article',
            name='paragraph3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third_paragraph', to='article.paragraph'),
        ),
        migrations.AlterField(
            model_name='article',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.articletemplate', verbose_name='Article Template'),
        ),
    ]
