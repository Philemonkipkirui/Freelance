from django import forms
from .models import Task

class task_data(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'status','client_name']
        widgets = {
            'title': forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-md text-black bg-white'
            }),

            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md text-black bg-white',
                'rows': 3
            }),
            'client_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md text-black bg-white'
            }),
            'due_date': forms.DateTimeInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md text-black bg-white',
                'type': 'datetime-local'
            }),
            'priority': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md text-black bg-white',
            }),
            'status': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md text-black bg-white'
            }),
        }