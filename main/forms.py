from django import forms
from .models import employee_data

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = employee_data
        fields = ['emp_first_name', 'emp_last_name', 'emp_role', 'emp_id']