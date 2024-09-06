from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from app_accounting.models import User 
from django.contrib.auth.forms import PasswordChangeForm 
from .models import MessagingModel, ConsultingModel, NewsletterModel, BlogPostModel 


class CustomUserCreationForm(UserCreationForm): 
    class Meta: 
        model = User 
        fields = ('username',)
        labels = { 
            'username': 'username', 
        } 

class MyPasswordChangeForm(PasswordChangeForm): 
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 

        for field_name in ['old_password','new_password1','new_password2'] : 
            self.fields[field_name].widget = forms.PasswordInput() 


class MessagingForm(forms.ModelForm):  
    class Meta: 
        model = MessagingModel 
        fields = '__all__' 


class ConsultingForm(forms.ModelForm): 
    class Meta: 
        model = ConsultingModel 
        fields = '__all__'


class NewsletterForm(forms.ModelForm): 
    class Meta: 
        model = NewsletterModel 
        fields = '__all__' 


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPostModel
        fields = '__all__'