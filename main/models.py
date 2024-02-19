from django.db import models
from  django.utils import timezone

# Create your models here.
class employee_data(models.Model):
    emp_first_name = models.CharField(max_length=100)
    emp_last_name = models.CharField(max_length=100)
    emp_role = models.IntegerField(default=0)
    emp_id = models.CharField(max_length=150)
    emp_id = models.CharField(max_length=200)
    emp_created_at = models.DateTimeField(auto_now_add=True)
    emp_updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.emp_created_at = timezone.now()
        self.emp_created_at = timezone.now()
        super().save(*args, **kwargs)