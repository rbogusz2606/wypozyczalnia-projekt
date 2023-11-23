from . import views
from django.urls import path

urlpatterns = [
    path("GetData", views.getData, name = "GetData"),
    path("PostData", views.addObject, name= "PostData"),
    path("PutDelete/<int:pk>", views.PutDeteteFunc, name = "PutDelete")
]
