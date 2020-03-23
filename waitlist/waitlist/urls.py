from django.urls import include, path
from rest_framework import routers
from rest import views
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView


urlpatterns = [
         path('', TemplateView.as_view(template_name='index.html')),
         path('rest/waitlist', views.WaitlistView.as_view()),
         path('rest/signup', views.SignUpView.as_view())
        ]
