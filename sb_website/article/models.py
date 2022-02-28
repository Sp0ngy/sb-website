from django.db import models

# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=100, null=False, verbose_name='Article Titel')
    template = models.ForeignKey('ArticleTemplate', on_delete=models.CASCADE, null=False, verbose_name='Article Type')
    category = models.ForeignKey('ArticleCategory', on_delete=models.CASCADE, null=True, verbose_name='Article Category')
    short_description_en = models.TextField(max_length=500, null=False, verbose_name='Short Description EN')
    short_description_tr = models.TextField(max_length=500, null=False, verbose_name='Short Description TR')
    description_en = models.TextField(max_length=10000, null=False, verbose_name='Description EN')
    description_tr = models.TextField(max_length=10000, null=False, verbose_name='Description TR')
    thumbnail = models.ImageField(upload_to='article/', default='article/placeholder.png')

    # Standard
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Object Name
    def __str__(self):
        return self.title

    # String shown in Admin-Interface
    class Meta:
        verbose_name = 'Article'

class ArticleImages(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    # TODO: make path for upload_to dynamic
    image = models.ImageField(upload_to='article/images', default=None)

    # Object Name

    def __str__(self):
        objectname = self.article.title
        return objectname

    # String shown in Admin-Interface
    class Meta:
        verbose_name = 'Images of Article'

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

#article_title
#article_type: Video, Text_Image, Text
#article_category
#article_short_description_en
#article_short_description_tr
#article_description_en
#article_description_tr
#thumbnail (will be shown on Cancer Knowledge List view)
#image/s (multiple) see https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django
#video
                                                                 #
#created_at
#updated_at
                                                                 #
#CancerKnowledgeListView:
                                                                 #
#Template shows article_title, short_description, thumbnail, pub_date;
#if has Video, show little Play Button (and Language on List View)