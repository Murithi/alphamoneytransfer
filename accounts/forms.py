import random
import datetime
import string
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Client


class SignUpForm(UserCreationForm):

    first_name = forms.CharField(label="First Name", max_length=120,
                                 widget=forms.TextInput({'class': 'form-control', 'placeholder': 'First Name'}))

    last_name = forms.CharField(label="Last Name", max_length=120,
                                widget=forms.TextInput({'class':'form-control', 'placeholder': 'Last Name'}))

    username = forms.CharField(label="Username", max_length=120,
                               widget=forms.TextInput({'class': 'form-control','placeholder': 'Username'}))
    email = forms.EmailField(label="Email Address", max_length=120,
                             widget=forms.TextInput({'class': 'form-control', 'placeholder': ''}))
    phone_number = forms.CharField(label="Phone Number", max_length=10,
                                   widget=forms.TextInput({'class': 'form-control'}))
    password1 = forms.CharField(label="Password",
                                widget=forms.widgets.PasswordInput({'class': 'form-control', }))
    password2 = forms.CharField(label="Password (again)",
                                widget=forms.widgets.PasswordInput({'class': 'form-control', }),
                                )

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'phone_number')

    def clean(self):
        """
        Verifies that the values entered into the password fields match
        NOTE: Errors wil appear in 'non_field_errors()'' because it applies to more than one field.
        """
        cleaned_data = super(SignUpForm, self).clean()



        if 'password1' in cleaned_data and 'password2' in cleaned_data:
            if cleaned_data['password1'] != cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again")
            return cleaned_data

    def save(self, commit=True):
        newuser = super(UserCreationForm, self).save(commit=False)
        newuser.email = self.cleaned_data['email']
        newuser.username = self.cleaned_data['username']
        newuser.first_name = self.cleaned_data['first_name']
        newuser.last_name = self.cleaned_data['last_name']
        newuser.set_password(self.cleaned_data["password1"])
        newphonenum = self.cleaned_data['phone_number']
        if len(newphonenum) == 10:
            newphonenum = '+254' + newphonenum[1:10]
        newuser.phone_number = newphonenum
        randomkey = ''.join(random.choice(string.letters) for i in xrange(32))
        newuser.email_confirm_key = randomkey
        newuser.key_expires = datetime.datetime.today() + datetime.timedelta(2)
        if commit:
            newuser.is_active = False
            newuser.save()
        return newuser


class VerificationForm(forms.Form):
    verification_token = forms.CharField(label="Enter code recieved in your Phone:", max_length=20,
                                         widget=forms.TextInput({'class': 'form-control'}))