from django.db import models

# Create your models here.
class Article(models.Model):

    title = models.CharField(max_length=100, verbose_name='Article Titel')
    template = models.ForeignKey('ArticleTemplate', on_delete=models.CASCADE, verbose_name='Article Template')
    category = models.ForeignKey('ArticleCategory', on_delete=models.CASCADE, null=True, verbose_name='Article Category')
    short_description_en = models.TextField(max_length=350, verbose_name='Short Description EN', help_text='Short, interessting text for catching the reader.')
    short_description_tr = models.TextField(max_length=350, blank=True, verbose_name='Short Description TR')
    main_description_en = models.TextField(max_length=10000, verbose_name='Description EN')
    main_description_tr = models.TextField(max_length=10000, blank=True, verbose_name='Description TR')
    thumbnail = models.ImageField(upload_to='article/', default='article/placeholder.png')

    primary_image = models.ImageField(upload_to='article/%Y/%m/%d', default=None, blank=True, null=True)
    primary_video = models.FileField(upload_to='article/%Y/%m/%d', default=None, blank=True, null=True, help_text='Required format: MP4')
    primary_media_source = models.CharField(max_length=150, blank=True, verbose_name='Primary Image Source')

    paragraph1 = models.ForeignKey('Paragraph', blank=True, null=True, on_delete=models.CASCADE, related_name='first_paragraph')
    paragraph2 = models.ForeignKey('Paragraph', blank=True, null=True, on_delete=models.CASCADE, related_name='second_paragraph')
    paragraph3 = models.ForeignKey('Paragraph', blank=True, null=True, on_delete=models.CASCADE, related_name='third_paragraph')

    # Standard
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Object Name
    def __str__(self):
        return self.title

    # String shown in Admin-Interface
    class Meta:
        verbose_name = 'Article'
        ordering = ['-created_at']

# Addable Paragraph for a Article
class Paragraph(models.Model):
    paragraph_image = models.ImageField(upload_to='article/%Y/%m/%d', default=None, blank=True, null=True,
                                        help_text='Ratio Width=1 Height=1')
    paragraph_image_source = models.CharField(max_length=150, blank=True, verbose_name='Paragraph Image Source')
    headline = models.CharField(max_length=300, verbose_name='Paragraph Headline')
    description_en = models.TextField(max_length=10000, verbose_name='Description EN')
    description_tr = models.TextField(max_length=10000, blank=True, verbose_name='Description TR')

    # Standard
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Object Name
    def __str__(self):
        return self.headline

    # String shown in Admin-Interface
    class Meta:
        verbose_name = 'Paragraph'


# Necessary for selecting correct template
class ArticleTemplate(models.Model):
    name = models.CharField(max_length=50, null=False)

    # Object Name
    def __str__(self):
        return self.name

    # String shown in Admin-Interface
    class Meta:
        verbose_name = 'Article Template'

class ArticleCategory(models.Model):
    name = models.CharField(max_length=50, null=False)

    # Standard
    created_at = models.DateTimeField(auto_now_add=True)

    # Object Name
    def __str__(self):
        return self.name

    # String shown in Admin-Interface
    class Meta:
        verbose_name = 'Article Category'
