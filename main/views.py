from django.shortcuts import render, HttpResponse
from .models import employee_data

# Create your views here.
def home(request):
    all_emp = employee_data.objects.all().order_by("-emp_created_at")
    context = {
        "all_emp": all_emp 
    }
    return render(request, "main/home.html", context)

def about_us(request):
    return HttpResponse("About Page")