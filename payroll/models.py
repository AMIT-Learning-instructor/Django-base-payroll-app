from django.db import models

# Create your models here.
from employee.models import * 

class Deduction(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE , related_name="deductions")
    amount = models.FloatField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.employee.name} - {self.amount}"
    

class Increase(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE , related_name="increases")
    amount = models.FloatField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.employee.name} - {self.amount}"


class Payment(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE , related_name="payments")
    total_salary = models.FloatField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.employee.name} - {self.total_salary}"