from django.urls import path

from . import views

""" The 'name' parameter is used when referencing a URL from templates. This
allows us to make global changes to the URL patterns of our project while
only changing a single file
"""
urlpatterns = [
    path('', views.index, name='index')
]
