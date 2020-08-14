from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from todo_app.models import todo_item

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User

        fields = ('first_name','last_name','username','email','password')

class todoForm(forms.ModelForm):

    class Meta():
        model = todo_item

        fields = ('title','description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'description': forms.Textarea(attrs={'class': 'myfieldclass1'})
        }