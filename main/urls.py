from django.urls import path
from . import views
urlpatterns=[
    path("", views.index),
    path("student/<int:id>", views.studentDetails),
    path("records/", views.getRecords)
]

