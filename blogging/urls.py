from django.urls import path
from .views import home,blog_details,create_comment
urlpatterns = [
    path("home/",home,name='home'),
    path("blog_details/<int:id>/",blog_details,name='blog_details'),
    path("create-comment/<int:blog_id>/",create_comment,name='create_comment')
]