from django.urls import path
from task.views import DailyTaskCreateView

urlpatterns = [

    path('task_add/', DailyTaskCreateView.as_view(), name='task'),

]
