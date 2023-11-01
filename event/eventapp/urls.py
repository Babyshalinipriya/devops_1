from django.urls import path
from .import views
urlpatterns=[
    path("",views.htmlexample,name="htmlexample"),
    path("signin/",views.signin,name="signin"),
    path("main/",views.main,name="main")
]