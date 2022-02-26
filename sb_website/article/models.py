from django.db import models

# Create your models here.

# TODO: change to correct Model
class Default(models.Model):
    pass

#article_title
#article_type: Video, Text/Image
#article_category
#article_short_description_en
#article_short_description_tr
#article_description_en
#article_description_tr
#thumbnail (will be shown on Cancer Knowledge List view)
#image/s (multiple)
#video
                                                                 #
#created_at
#updated_at
                                                                 #
#CancerKnowledgeListView:
                                                                 #
#Template shows article_title, short_description, thumbnail, pub_date;
#if has Video, show little Play Button (and Language on List View)