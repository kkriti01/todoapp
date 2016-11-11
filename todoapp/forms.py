from django import forms


from .models import Todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['id', 'name', 'description', 'priority', 'state_task', 'due_date']

