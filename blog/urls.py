"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from post.views import post_create, post_detail, post_edit, post_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", post_list, name="post-list"),
    path("post/create", post_create, name="post-create"),
    path("post/<id:int>/edit", post_edit, name="post-edit"),
    path("post/<id:int>/detail", post_detail, name="post-detail"),
]
