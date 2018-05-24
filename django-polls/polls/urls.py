from django.urls import path

from . import views

""" The 'name' parameter is used when referencing a URL from templates. This
allows us to make global changes to the URL patterns of our project while
only changing a single file
"""

""" Namespacing urls so that they don't clash with urls with the same name in
another app
"""
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # '<>' helps capture the variable and pass it off as parameter to the view
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
