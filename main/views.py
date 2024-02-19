from django.shortcuts import render, redirect
from .models import employee_data
from .forms import EmployeeForm

# Create your views here.
def home(request):
    all_emp = employee_data.objects.all().order_by("-emp_created_at")
    context = {
        "all_emp": all_emp 
    }
    return render(request, "main/home.html", context)

def emp_detail(request, pk):
    emp = employee_data.objects.get(pk=pk)

    context = {
        'emp': emp
    }
    return render(request, 'main/emp_detail.html', context)

def emp_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('emp_detail', pk=form.instance.pk)
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, 'main/create_employee.html', {'form': form})