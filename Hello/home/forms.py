from django.forms import ModelForm, fields
from home.models import ToDo



class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['title','notes','status','priority']