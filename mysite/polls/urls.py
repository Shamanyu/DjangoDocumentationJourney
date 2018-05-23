from django.urls import path

from . import views

""" The 'name' parameter is used when referencing a URL from templates. This
allows us to make global changes to the URL patterns of our project while
only changing a single file
"""
urlpatterns = [
    path('', views.index, name='index'),
    # '<>' helps capture the variable and pass it off as parameter to the view
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
