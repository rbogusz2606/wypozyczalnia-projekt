from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cars, caravailability
from django.views.generic import DetailView, CreateView
from django.views.generic.base import TemplateView
from .forms import carquery 
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

def registration(request):
    form = RegisterForm()
    if request.method =='POST':                               #REJESTRACJA
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f"User {user} created")
            return redirect("login")

        
    context = {'form': form}
    return render(request, 'docs/register.html', context)
         



def sign_in(request):
    if request.method == "POST":
        form = LoginForm(request , data=request.POST)                   #LOGOWANIE
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
            return redirect("cars-list")
    else:
        form = LoginForm()
    
    return render(request, "docs/login.html", {
        'form': form,})

def logoutuser(request):
    logout(request)                        #WYLOGOWANIE
    return redirect('login')


@login_required(login_url="login")
def cars_view(request):
        osobowe_cars = Cars.objects.filter(category="Osobowe")
        towarowe_cars = Cars.objects.filter(category="Towarowe")            #STRONA GŁÓWNA
        context = {
        'osobowe_cars': osobowe_cars,
        'towarowe_cars': towarowe_cars
        }
    
        return render(request, 'docs/index.html', context)
   
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class carview(DetailView):
    model = Cars
    template_name = "docs/individual_car.html"
    context_object_name = "car"                         #WIDOK Z INFORMACJAMI O SAMOCHODZIE
    




@method_decorator(login_required(login_url='login'), name='dispatch')
class Sendmessage(CreateView):
    model = caravailability
    form_class = carquery                               #INFORMACJA O UŻYTKOWNIKU SKŁADAJĄCYM ZAMÓWIENIE
    template_name = "docs/carsend.html"
    success_url = "success"






@method_decorator(login_required(login_url='login'), name='dispatch')
class SuccessView(TemplateView):                    #PODZIĘKOWANIE ZA SKORZYSTANIE ZE STRONY
    template_name = "docs/succescarquery.html"      
    
   

    
    

# Create your views here.
