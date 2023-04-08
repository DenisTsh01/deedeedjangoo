from django import forms
from django.forms import TextInput, Select, DateInput
from task.models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_date', 'task_deadline', 'task_information', 'category','extend_user']
        widgets = {
            'task_name': TextInput(attrs={
                'placeholder': 'Task name. ',
                'class': 'form-control',
                'required': True,
            }),
            'task_date': TextInput(attrs={
                'placeholder': '(yy-mm-dd)',
                'class': 'form-control',
                'required': True,
                }),
                'task_deadline': TextInput(attrs={
                    'placeholder': "Deadline.(optional)",
                    'class': 'form-control',
                    'required': False,


            # }),
            # 'start_hour': TextInput(attrs={
            #     'placeholder': '(hour)',
            #     'class': 'form-control',
            #     'required': False,
            }),
            'task_information': TextInput(attrs={
                'placeholder': 'Description.(optional)',
                'class': 'form-control',
                'required': False,
            }),

            'category':  Select(attrs={
                'placeholder': "Task type.(required)",
                'class': 'form-control',
                'required': False,

            }),
            'extend_user': Select(attrs={
                'placeholder': "",
                'class': 'form-control',
                'required': False,

            }),
        }


    def clean(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data.get('task_name')
        data = cleaned_data.get('task_date')
        all_tasks = Task.objects.all()
        for task in all_tasks:
            if str(name) == str(task.task_name) and data == task.task_date:
                msg = 'This task is already assigned'
                self._errors['task_name'] = self.error_class([msg])
        return cleaned_data


