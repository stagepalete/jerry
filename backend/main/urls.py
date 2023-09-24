from django.urls import path
from main.views import *

urlpatterns = [
    path('', ListUsers.as_view() ,name='home'),
]
