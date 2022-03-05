from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# static()
app_name = 'article'
urlpatterns = [
    path('knowledge/', views.ArticleList.as_view(), name='article_list'),
    path('knowledge/<int:pk>', views.ArticleDetail.as_view(), name='article_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)