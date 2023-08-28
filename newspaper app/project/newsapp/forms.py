from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Category, Article

class RegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=50,
        required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name',}))
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username',}))
    email = forms.EmailField(required=True, 
    widget=forms.TextInput(attrs={'placeholder': 'Email',}))
    date_of_birth = forms.DateField(required=True, 
    widget=forms.TextInput(attrs={'placeholder': 'Date',}))
    password1 = forms.CharField(max_length=50,
        required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password',}))
    password2 = forms.CharField(max_length=50, required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['name','username', 'email', 'date_of_birth', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass  # Use the default AuthenticationForm for login

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'article_body', 'category']