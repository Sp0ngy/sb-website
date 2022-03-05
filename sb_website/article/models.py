from django.db import models

# Create your models here.
# TODO: check models attribute null=True if necessary or not
class Article(models.Model):

    title = models.CharField(max_length=100, verbose_name='Article Titel')
    template = models.ForeignKey('ArticleTemplate', on_delete=models.CASCADE, verbose_name='Article Template')
    category = models.ForeignKey('ArticleCategory', on_delete=models.CASCADE, null=True, verbose_name='Article Category')
    short_description_en = models.TextField(max_length=500, verbose_name='Short Description EN', help_text='Short, interessting text for catching the reader')
    short_description_tr = models.TextField(max_length=500, blank=True, verbose_name='Short Description TR')
    main_description_en = models.TextField(max_length=10000, verbose_name='Description EN')
    main_description_tr = models.TextField(max_length=10000, blank=True, verbose_name='Description TR')
    thumbnail = models.ImageField(upload_to='article/', default='article/placeholder.png')

    #TODO: Change to Fielfield so it can handle image and video, check if filefield is enough to identify which template is needed, so "template" can be deleted

    primary_image = models.ImageField(upload_to='article/%Y/%m/%d', default=None, blank=True, null=True, help_text='Ratio Width=1 Height=1')
    primary_image_source = models.CharField(max_length=150, blank=True, verbose_name='Primary Image Source')

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

    # Object Name
    def __str__(self):
        return self.name

    # String shown in Admin-Interface
    class Meta:
        verbose_name = 'Article Category'
