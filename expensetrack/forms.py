from django.forms import ModelForm,PasswordInput
from .models import Expense,MyUser

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['first_name','last_name','username','password','phone','email']
        widgets = {
        'password': PasswordInput()
        }
