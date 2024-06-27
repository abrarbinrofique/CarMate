from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from users.forms import adduser
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from Carmodel.models import car,Purchace


# Create your views here.
def signupform(request):
  if not request.user.is_authenticated:
    if request.method=='POST':
        form=adduser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'you successfully add your account,now login here!')
            return redirect('login')
        
    
    else:
        form=adduser()
    return render (request,'signup.html',{'form':form})
  else:
      return redirect('profile')



class loginform(LoginView):
  
    template_name='login.html'

    def form_valid(self, form):
        username=form.cleaned_data.get('username')
        messages.success(self.request,f'Welcome mr.{username}')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request,'Logged in information incorrect')
        return super().form_invalid(form)
    

    def get_context_data(self, **kwargs) :
        context=super().get_context_data(**kwargs)
        context['type']='Login'
        return context
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
def profile(request):
  if request.user.is_authenticated:
    usercar=Purchace.objects.filter(user=request.user)
    print(usercar)
    return render (request,'profile.html',{'choicecar':usercar})
  else:
      return redirect('login')



class logoutform(LogoutView):
  
    template_name='logout.html'

    def get_success_url(self):
      messages.success(self.request,'Logout Successfully')
      return reverse_lazy('login')
    



def modelbuy(request,id):
  if request.user.is_authenticated:
    choicecar=car.objects.get(pk=id)
    if (choicecar.Quantity>0):
        choicecar.Quantity=choicecar.Quantity-1
        choicecar.save()
        # print(choicecar)
          #    if choicecar.userquantity>0 :
    #         choicecar.userquantity=+1
    #         # print(choicecar.user.Quantity)
    #         choicecar.save()
           
    #    else:
    #     choicecar.user.add(request.user)
        
    #     choicecar.save()
    #     return redirect('profile') 
    # else:
    #     messages.warning(request,'The car isn''t available right now')
    # return redirect('home')
        purchasecar,created=Purchace.objects.get_or_create(user=request.user,car=choicecar)
        if created:
            purchasecar.Purchace_count=1
            purchasecar.save()
            

        else:
             purchasecar.Purchace_count=purchasecar.Purchace_count+1
             purchasecar.save()
        messages.success(request,f'congratulations mr {request.user.username}! you purchase the car successfully')
        return redirect('profile') 
    else:
        messages.warning(request,'The car isn''t available right now')
    return redirect('home')
  else:
        return redirect('signup')
      