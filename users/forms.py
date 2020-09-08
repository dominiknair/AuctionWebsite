from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
import datetime


CURRENT_YEAR = datetime.date.today().year
YEARS = list(range(CURRENT_YEAR - 100, CURRENT_YEAR+1))

class DateInput(forms.DateInput):
    input_type = 'date'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    dob = forms.DateField(
        initial=datetime.date.today(),
        widget=DateInput,
        required=True,
        label="Date of birth"
    )
    class Meta:
        model = Profile
        fields = ['pic','dob']
        
class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):
    dob = forms.DateField(
        initial=datetime.date.today(),
        widget=DateInput,
        required=True,
        label="Date of birth"
    )
    class Meta:
        model = Profile
        fields = ['pic','dob']
