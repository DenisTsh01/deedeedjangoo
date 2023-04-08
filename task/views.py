from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from task.form import TaskCreateForm
from task.models import Task
from users.models import ExtendUser

# task


class DailyTaskCreateView(CreateView):
    template_name = 'home/task_add.html'
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        extend_user = ExtendUser.objects.get(username=self.request.user.username)
        context['extend_user'] = extend_user
        print(context)

        return context

    def post(self, request, *args, **kwargs):
        form = TaskCreateForm(data=request.POST)



class DailyTaskListView(ListView):
    template_name = ""
    model = Task
    context_object_name = "all_tasks"
