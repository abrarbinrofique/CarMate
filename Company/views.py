from django.shortcuts import render,redirect

# Create your views here.
from Company.forms import companyform
from django.contrib import messages

def companycatagory(request):
  if request.user.is_superuser:
    if request.method=='POST':
        form=companyform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form=companyform()
  else:
    messages.warning(request,'only admin can access this page]')
    return redirect('profile')

  return render(request,'company.html',{'form':form})