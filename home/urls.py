"""home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



app_name = 'home'
urlpatterns = [
    path('', views.HomeInfoListView.as_view(), name='home'),
    path('privateservice/', views.PrivateServiceView.as_view(), name='privateservice'),
    path('professionalservice/', views.ProfessionalServiceView.as_view(), name='professionalservice'),
    path('membership/', views.MembershipView, name='membership'),
    path('partner/', views.PartnerListView.as_view(), name='partner'),
    path('information/', views.InformationView.as_view(), name='information'),
    path('maintenance/', views.MaintenanceView.as_view(), name='maintenance'),
    path('i18n/', include('django.conf.urls.i18n')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)