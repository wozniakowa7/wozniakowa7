"""advertisingForum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from forum import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # auth
    path('register', views.register, name='register'),
    path('log', views.log, name='log'),
    path('logout', views.logout_user, name='logout'),

    # forum
    path('', views.home, name='home'),
    path('<int:adId>', views.detail, name='detail'),
    path('create', views.create, name='create'),
    path('my', views.my, name='my'),
    path('edit/<int:adId>', views.edit, name='edit'),
    path('delete/<int:adId>', views.deleteAd, name='deleteAd'),
    path('search', views.search, name='search'),
    path('industry/<str:industryKey>',
         views.display_industry, name='displayIndustry'),
    path('like/<int:adId>', views.like, name='like'),
]
