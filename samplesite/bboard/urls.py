from django.urls import path
from .views import index, cur_time, by_rubric

urlpatterns = [
    path('', index),
    path('<int:rubric_id>/', by_rubric),
    path('cur_time/', cur_time),
]

