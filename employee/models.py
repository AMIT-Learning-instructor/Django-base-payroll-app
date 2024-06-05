from django.db import models

# Create your models here.



class Jobs(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    ssn = models.CharField( max_length=14)
    job = models.ForeignKey(Jobs , on_delete=models.CASCADE,related_name='employees')
    salary = models.FloatField()
    
    
    def __str__(self):
        return f"{self.name} - {self.ssn}"