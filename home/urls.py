from django.urls import path
from home.views import HomeTemplateView, chat_view, ContactTemplateView, IntroductionTemplateView, TaskUpdateView

urlpatterns = [
    path('home/', HomeTemplateView.as_view(), name='home_page'),
    path('chat/', chat_view, name='chatbot'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),
    path('', IntroductionTemplateView.as_view(), name='introd'),
    path('task_update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    ]

