"""feedback_project URL Configuration

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
from django.contrib import admin
from django.urls import path

admin.site.site_header = 'BACKEND'
admin.site.site_title = 'BACKEND PANEL'
admin.site.index_title = 'WELCOME TO FEEDBACKS MANAGE PANEL'

from . import views

#from .views import idea

from FEEDBACKS.views import (
    enter_suggestion,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.idea, name='idea'),
    #path('', idea, name='idea'),
    path('FEEDBACKS/create/', enter_suggestion, name = 'FEEDBACKS/create'),
]
