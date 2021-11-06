from django.urls import path
from hello import views
from hello.models import LogMessage
from django.views.generic import ListView

about_list_view = views.AboutListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/about.html",
)

urlpatterns = [
    path('home', views.home, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
    path("",about_list_view, name="about"),
    

   
    
    
]

