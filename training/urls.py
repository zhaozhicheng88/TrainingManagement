from django.urls import path, include
from . import views as user_views

urlpatterns = [
    # path('', user_views.index, name='index'),
    path('', include('django.contrib.auth.urls')),

]
