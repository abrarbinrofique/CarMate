from typing import Any
from django.shortcuts import render,redirect
from Carmodel.forms import carform,commentform
from Carmodel.models import car
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
# Create your views here.
def modelcatagory(request):
  if request.user.is_superuser:
    if request.method=='POST':
        form=carform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form=carform()
    return render(request,'model.html',{'form':form})
  else:
      return redirect ('login')
 


class cardetails(DeleteView):
    model=car
    pk_url_kwarg='id'
    template_name='car_detail.html'
    def post(self,request,*args, **kwargs):
        comment_form=commentform(data=request.POST)
        post=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.carmodel=post
            new_comment.save()
            return self.get(request,*args, **kwargs)
    

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            post=self.get_object()
            comments=post.comments.all()
            commentsform=commentform()
            context["comments"] =comments
            context["commentsform"] =commentsform
            return context
        



    
