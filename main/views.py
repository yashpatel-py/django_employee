from django.shortcuts import render, redirect, get_object_or_404
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

def emp_update(request, pk):
    employee = get_object_or_404(employee_data, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'main/emp_update.html', {'form': form})