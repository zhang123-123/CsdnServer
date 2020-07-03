"""csdnServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from banner.views import BannerView
from csdn.views import CsdnBlogView, BlogTypeView, TypeView, SearchBlogView, UserLLBlogView, MySeachView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('BannerView/', BannerView.as_view(), name='BannerView'),
    path('CsdnBlogView/', CsdnBlogView.as_view(), name='CsdnBlogView'),
    path('TypeView/', TypeView.as_view(), name='TypeView'),
    path('BlogTypeView/', BlogTypeView.as_view(), name='BlogTypeView'),
    # path('SearchBlogView/', SearchBlogView.as_view(), name='SearchBlogView'),
    path('SearchBlogView/', MySeachView(), name='SearchBlogView'),
    path('UserLLBlogView/', UserLLBlogView.as_view(), name='UserLLBlogView'),
    # path('BannerView1/', b_views.BannerView, name='BannerView')
]
