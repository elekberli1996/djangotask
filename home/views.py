from django.shortcuts import get_object_or_404, render,redirect
from .form import PortfolioForm
from .models import Portfolio
from django.http import HttpResponse
from django.template.loader import render_to_string
import pdfkit




def add_page(request):

    form=PortfolioForm(request.POST or None)

    if form.is_valid():
     
        form.save()
       
        return redirect("home")

    context={
        "form":form
    }
    return render(request,"add.html",context)
# Create your views here.

def list_page(request):
    users=Portfolio.objects.all()
    return render(request,"list.html",{'users':users})


def home_page(request):
    return render(request,"index.html")

def detail_page(request,id):
    user=get_object_or_404(Portfolio,id=id)
    context={
        "user":user,
        
    }

    return render(request,"detail.html",context)

def download_pdf(request,id):
    user=get_object_or_404(Portfolio,id=id)
    context={
        "user":user,
        
    }
    # Render HTML template as string
    html_template = render_to_string('detail.html',context)

    # Create PDF
    pdf = pdfkit.from_string(html_template, False)

    # Prepare HTTP response with PDF
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="etrafli_melumat.pdf"'

    return response
