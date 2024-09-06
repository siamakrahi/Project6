from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout    
from django.contrib.auth.forms import AuthenticationForm    
from django.contrib.auth.decorators import login_required    
from django.contrib import messages    
from .forms import CustomUserCreationForm, MessagingForm, ConsultingForm, NewsletterForm 
from .models import User, MessagingModel, ConsultingModel, NewsletterModel, BlogPostModel


def about(request):   
    return render(request, 'about.html')   
 

def blog(request):   
    return render(request, 'blog.html')  
 
 
def contact(request):   
    return render(request, 'contact.html')  
 
 
def home(request):   
    return render(request, 'home.html') 
  
 
def service(request):   
    return render(request, 'service.html') 
  
 
def team(request):   
    return render(request, 'team.html')   


def login_view(request):    
    if request.method == 'POST':    
        form = AuthenticationForm(request, data=request.POST)    
        if form.is_valid():    
            username = form.cleaned_data.get('username')    
            password = form.cleaned_data.get('password')    
            user = authenticate(username=username, password=password)    
            if user is not None:    
                login(request, user)    
                return redirect('home')    
            else:    
                messages.error(request, "Invalid login credentials. Please check your details.")    
 
        else:    
            messages.error(request, "Invalid login form. Please check your details.")    
    else:    
        form = AuthenticationForm()    
    return render(request, 'login.html', {'form': form})  


def signup_view(request):    
    if request.method == 'POST':    
        form = CustomUserCreationForm(request.POST)     
        if form.is_valid():    
            form.save()    
            username = form.cleaned_data.get('username')    
            # نیازی به تایید مجدد رمز عبور نیست.   
            # password = form.cleaned_data.get('password1')   
            user = User.objects.get(username=username)   
            login(request, user)   
            messages.success(request, "Account created successfully!")   
            return redirect('home')   
        else:   
            messages.error(request, "Invalid signup form. Please check your details.")    
 
    else:    
        form = CustomUserCreationForm()    
    return render(request, 'signup.html', {'form': form})


def logout_view(request):   
    if request.method == "POST":   
        logout(request)   
        return redirect('home')   
    else:   
        return redirect('home')
    

@login_required
def create_messaging(request):
    if request.method == 'POST':
        form = MessagingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MessagingForm()
    return render(request, 'messaging_form.html', {'form': form})


@login_required   
def create_consulting(request):
    if request.method == 'POST':
        form = ConsultingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ConsultingForm()
    return render(request, 'home.html', {'form': form})


@login_required    
def create_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsletterForm()
    return render(request, 'newsletter/', {'form': form})


def map_view(request):
    return render(request, 'contact.html')


def search(request):
    query = request.GET.get('query')
    if query:
        results = BlogPostModel.objects.filter(title__icontains=query) | BlogPostModel.objects.filter(content__icontains=query)
    else:
        results = BlogPostModel.objects.none()
    return render(request, 'search_results.html', {'results': results, 'query': query})


def blog_list(request):
    posts = BlogPostModel.objects.all().order_by('-published_date')
    return render(request, 'blog_list.html', {'posts': posts})


def blog_detail(request, post_id):
    post = get_object_or_404(BlogPostModel, id=post_id)
    return render(request, 'blog_detail.html', {'post': post})
