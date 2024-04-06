from django.db import models
from  django.utils import timezone

# Create your models here.
class employee_data(models.Model):
    emp_first_name = models.CharField(max_length=100)
    emp_last_name = models.CharField(max_length=100)
    emp_role = models.CharField(max_length=150)
    emp_id = models.CharField(max_length=150, unique=True)
    emp_created_at = models.DateTimeField(auto_now_add=True)
    emp_updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.emp_updated_at = timezone.now()
        super().save(*args, **kwargs)