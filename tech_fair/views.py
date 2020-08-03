from django.shortcuts import render
from .models import Announcement

# Create your views here.

def home(request):
    announcements = Announcement.objects.all()
    return render(request, 'tech_fair/home.html',{'announces':announcements})
def studenthelp(request):
    return render(request,'tech_fair/tips.html')
def staff(request):
    return render(request,'tech_fair/staff.html')