from django import forms
from .models import Jobs , Employee
# class EmployeeForm(forms.Form):
#     name = forms.CharField()
#     ssn = forms.CharField(max_length=14)
#     salary = forms.FloatField()
#     job = forms.ModelChoiceField(queryset=Jobs.objects.all())

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'