from django.shortcuts import render,redirect
from .form import PortfolioForm


def home_page(request):

    form=PortfolioForm(request.POST or None)

    if form.is_valid():
     
        form.save()
       
        return redirect("home")

    context={
        "form":form
    }




    return render(request,"index.html",context)
# Create your views here.
