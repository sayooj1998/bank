from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.http import JsonResponse


#from .models import details, District, Branches, City

from django.http import JsonResponse
from django.contrib.auth import authenticate, login

from bankapp.forms import PersonCreationForm
from bankapp.models import City, Person


# Create your views here.
def index(request):
     return render(request,'base.html')


def reg(request):
    return render(request,'reg.html')


def login(request):
     return render(request,'login.html')

def new(request):
    return render(request,'new.html')




def logchech(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('new/')
        else:
            messages.info(request,"wrong credentials")
            return redirect('login/')
    return render(request,'new.html')


def regcheck(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name already taken")
                return redirect('/')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login/')
        return redirect('login')
    return render(request,'login.html')



def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'template_name.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'template_name.html', {'form': form})


# AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})
    return JsonResponse(list(cities.values('id', 'name')), safe=False)