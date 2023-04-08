import datetime
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView
from datetime import datetime, timezone

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from numpy.distutils.command.install_data import install_data

from chatbot.Chattbot import get_response_from_bot
from pocket.models import Budget

from task.models import Task
from chatbot.weather_manager import home_weather_response
from users.models import ExtendUser
from django.utils import timezone


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "home/home_view.html"

    def get_context_data(self, **kwargs):
        tasks_data = Task.objects.filter(extend_user_id=self.request.user.id)
        today = timezone.now()

        for task in tasks_data:
            diff = task.task_deadline - today
            task.days_until_deadline = diff.days + 1

        context = {'tasks': tasks_data}

        user = ExtendUser.objects.get(id=self.request.user.id)
        city = user.city
        context['city'] = city
        weather_list = home_weather_response(city)
        context['sky'] = weather_list.get('sky', None)
        context['weather_degrees_celsius'] = weather_list.get('weather_degrees_celsius', None)
        context['weather_degrees_feels_like'] = weather_list.get('weather_degrees_feels_like', None)
        context['weather_degrees_min'] = weather_list.get('weather_degrees_min', None)
        context['weather_degrees_max'] = weather_list.get('weather_degrees_max', None)
        context['weather_humidity'] = weather_list.get('weather_humidity', None)

        return context


def get_time(task_date):
    today = datetime.date.today()
    task_date_x = task_date
    diff = task_date_x - today
    return diff.days


class ContactTemplateView(TemplateView):
    template_name = "home/contact_page.html"

@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        print(request.POST)
        message = request.POST.get('message', '')
        reply = get_response_from_bot(message)
        return HttpResponse(reply)
    return render(request, "home/chat.html", {})


class IntroductionTemplateView(TemplateView):
    template_name = "home/introduction.html"


class TaskUpdateView(UpdateView):
    template_name = "home/task_update.html"
    model = Task
    fields = ['task_name', 'task_deadline', 'task_information', 'category', 'completed']
    success_url = reverse_lazy("home_page")
