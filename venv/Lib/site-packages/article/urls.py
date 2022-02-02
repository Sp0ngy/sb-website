from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# static()
app_name = 'article'
urlpatterns = [
    path('knowledge/', views.KnowledgeListView.as_view(), name='knowledge'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)