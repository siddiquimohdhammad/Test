from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Form
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,"index.html")

def knowmore(request):
    return render(request,'knowmore.html')

def registration(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        startup_name = request.POST.get('startup_name')
        website_url = request.POST.get('website_url')
        startup_email = request.POST.get('startup_email')
        mobile = request.POST.get('mobile')
        founder_name = request.POST.get('founder_name')
        details = request.POST.get('details')
        company_type = request.POST.get('company_type')
        industry = request.POST.get('industry')
        title_startup  = request.POST.get('title_startup')
        description = request.POST.get('description')
        funding_type = request.POST.get('funding_type')
        more_info = request.POST.get('more_info')
        current_status = request.POST.get('current_status')
        pitch_deck = request.POST.get('pitch_deck')
      
        registration = Form(email=email, startup_name=startup_name, website_url=website_url,
                        startup_email=startup_email, mobile=mobile, founder_name=founder_name,
                        details=details, company_type=company_type, industry=industry,
                        title_startup=title_startup,description=description,
                        funding_type=funding_type, more_info=more_info,
                        current_status=current_status, pitch_deck=pitch_deck)
        registration.save()
        messages.success(request, 'Form Submitted Successfully!!')
       
        
    return render(request,"registration.html")