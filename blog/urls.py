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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import login, register
from post.views import post_create, post_delete, post_detail, post_edit, post_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", post_list, name="post-list"),
    path("post/create", post_create, name="post-create"),
    path("post/<int:id>/edit", post_edit, name="post-edit"),
    path("post/<int:id>/detail", post_detail, name="post-detail"),
    path("post/<int:id>/delete", post_delete, name="post-delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
