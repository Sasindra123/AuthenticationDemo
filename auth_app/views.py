from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .middlewares import auth
from django.contrib.auth.decorators import login_required
from .forms import AccountDeletionForm
# from django.views.decorators.csrf import csrf_protect

# @csrf_protect
# Create your views here.

def home(request):
  return render(request, "home.html")


def register_view(request):
  if request.method == 'POST':
    form=UserCreationForm(request.POST)
    if form.is_valid():
      user=form.save()
      login(request,user)
      return redirect('dashboard')
  else:
    initial_data={'username':'','password1':'','password2':''}
    form=UserCreationForm(initial=initial_data)
  return render(request, 'auth/register.html',{'form':form})

def login_view(request):
  if request.method == 'POST':
    form=AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      user=form.get_user()
      login(request,user)
      return redirect('dashboard')
  else:
    initial_data={'username':'','password':''}
    form=AuthenticationForm(initial=initial_data)
  return render(request, 'auth/login.html',{'form':form})



@auth
def dashboard_view(request):
  return render(request,'dashboard.html')  



def logout_view(request):
  logout(request)
  return redirect('login')

def about(request):
  return render(request, 'aboutus.html')

def contact(request):
  return render(request, 'contactus.html')

def service(request):
  return render(request, 'services.html')

def settings(request):
  return render(request, 'settings.html')

@login_required
def delete_account(request):
    if request.method == 'POST':
        form = AccountDeletionForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirmation']:
            request.user.delete()
            logout(request)
            return redirect('login')
    else:
        form = AccountDeletionForm()
    return render(request, 'delete.html', {'form': form})