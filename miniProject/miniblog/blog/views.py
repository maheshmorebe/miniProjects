from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from .models import Post
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user                         # to create a profile on dashboard
        full_name = user.get_full_name()            # inbuld method to get a full name of the user
        gps = user.groups.all()                     # to get all the groups of the specific user
        return render(request,'blog/dashboard.html', {'posts':posts,
                                                      'full_name':full_name, 'groups':gps})
    else:
        return render(request,'/login/')


def user_signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! You have become an Author.')
            user = form.save()                          # save the form data in the user variable
            group = Group.objects.get(name='Author')        # after signup we have to add user into specific group
                                                            # inside admin panel i.e for giving some permissions to the specific user
            user.groups.add(group)                      # predefined to add user in the group

    else:
        form = SignUpForm()
    return render(request,'blog/signup.html',{'form':form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title,desc=desc)
                pst.save()
                form = PostForm()
        else:
            form = PostForm()
        return render(request,'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def update_post(request,pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = Post.objects.get(pk=pk)
            form = PostForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
        else:
            obj = Post.objects.get(pk=pk)
            form = PostForm(instance=obj)
        return render(request,'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def delete_post(request,pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = Post.objects.get(pk=pk)
            obj.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')



