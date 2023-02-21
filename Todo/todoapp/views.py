from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import Task
from django.shortcuts import  render,redirect
# from .forms import Registerform,Signinform
from django.contrib.auth.views import LoginView

# Create your views here.


class TaskView(ListView):
    model = Task
    context_object_name = 'items'
    template_name = 'list.html'



class Taskcreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('items')
    template_name = 'create.html'


class Taskupdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('items')
    template_name = 'create.html'

class Taskdelete(DeleteView):
    model = Task
    context_object_name = 'items'
    success_url = reverse_lazy('items')
    template_name = 'delete.html'

class Taskdetail(DetailView):
    model = Task
    field = '__all__'
    success_url = reverse_lazy('items')
    template_name = 'detail.html'


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)

        myuser.save()

        return redirect('signin')

    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.username
            return render(request, 'list.html', {'fname': fname})

        else:
            return redirect('signin')

    return render(request, 'signin.html')


def signout(request):
    logout(request)
    messages.success(request, 'Logged out Successfully!')
    return redirect('signin')


def home(request):
    return render(request,'home.html')