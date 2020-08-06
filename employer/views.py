from django.shortcuts import render
from .models import Company
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Q
from django.core.mail import BadHeaderError, send_mail
from django.template.loader import get_template
from django.conf import settings
from tech_career_fair.settings import EMAIL_HOST_USER

# Create your views here.
def list_of_companies(request):
    YEAR_LEVEL = (
        (1,'Freshman'),
        (2,'Sophomore'),
        (3,'Junior'),
        (4,'Senior'),
        (5,'Graduate'),
        (6,'Working Experience'),
    )

    MAJOR_TYPES = (
        (1,'Computer Animation & Game Development'),
        (2,'Civil Engineering'),
        (3,'Computer Engineering'),
        (4,'Computer Information Systems'),
        (5,'Computer Science'),
        (6,'Construction Industry Management'),
        (7,'Concrete Industry Management'),
        (8,'Contstruction Management'),
        (9,'Electrical Engineering'),
        (10,'Mechanical Engineering'),
        (11,'Mechatronic Engineering'),
        (12,'Sustainable Manufacturing'),
    )

    q = request.GET.get('q')
    edu = request.GET.get('education_level_select')
    mjr= request.GET.get('major_select')
    companies = Company.objects.all()
    content = dict()
    search_results=companies
    if edu :
        search_results = search_results.filter(Q(education_level__contains=edu))
    if q :
        search_results = search_results.filter(Q(name__contains=q))
    if mjr:
        search_results = search_results.filter(Q(major__contains=mjr))
    
    
    return render(request, 'employer/list_of_companies.html',{'companies':search_results })

    
    

def previous(request):
    return render(request, 'employer/prev_list.html')
def registration(request):
    return render(request, 'employer/registration.html')
def add_company(request):
    if request.method == "POST":
        data = request.POST.copy()
        company_name = data.get('name')
        if Company.objects.filter(name=company_name).exists():
            return render(request, 'employer/registration.html',{'Error': 'Error: Name used already'})
        desc = data.get('description')
        link = data.get('url')
        contact = data.get('email')
        businesscontact = data.get('bus_email')
        img = request.FILES['logo']
        majors = data.getlist('major')
        edulevel = data.getlist('education_level')
        create_obj = Company.objects.create( business_email =businesscontact, name = company_name,description=desc,logo =img,email=contact,education_level = edulevel,major =majors,url=link)
        recepient = str(contact)
     
        create_obj.save()
        print(recepient)
        send_mail('invoice','thank you for registering', EMAIL_HOST_USER, ['mamejia@csuchico.edu','mariomejia4263@yahoo.com'], fail_silently = False)        
        print(create_obj)
        print(create_obj.business_email)
        print(create_obj.url)

        return render(request, 'tech_fair/home.html',{'thankyou':'Thank you for registering. Please refer to our list of companies and confirm information.'})
    return render(request, 'employer/registration.html')

def parkinginfo(request):
    return render(request,'employer/parking_info.html')
def roomreservation(request):
    return render(request,'employer/roomreserv.html')
