from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    #id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    about = models.TextField(blank=True)
    
    def __str__(self):
        return self.get_full_name()
    

class MessagingModel(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    email = models.EmailField() 
    phone_number = models.CharField(max_length=20) 
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messaging_users', null=True)
    your_comment = models.TextField(blank = True)

    def __str__(self): 
        return f"{self.your_comment} - {self.name} - {self.phone_number} - {self.email}" 


class ConsultingModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consulting_users')

    def __str__(self): 
        return f"{self.name} - {self.phone_number} - {self.email}" 


class NewsletterModel(models.Model):
    email = models.EmailField(unique=True)
    subscribed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class BlogPostModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
