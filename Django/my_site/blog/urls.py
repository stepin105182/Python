from . import views
from django.urls import path


app_name = 'blog'
     

urlpatterns = [
    path("",views.start,name="start"),
    path("posts",views.allposts,name="all-posts"),
    path("contact",views.contact,name="contact"),
    path("posts/<slug:slug>",views.post,name="post"),

]
