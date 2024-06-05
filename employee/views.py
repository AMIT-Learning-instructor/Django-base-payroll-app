from django.shortcuts import redirect, render

from .forms import EmployeeForm
from .models import *
# Create your views here.
from django.views.decorators.http import require_http_methods
from django.views import View 


def job_list(request):
    jobs = Jobs.objects.all()
    context = {
        'jobs': jobs
    }
    return render(request,'jobs/list.html',context=context)


def employee_list(request):
    employees = Employee.objects.all().order_by('created_at')
    context = {
        'employees': employees
    }
    return render(request,'employees/list.html',context=context)


class EmployeeCreateStoreView(View):
    def get(self, request):
        context = {
        'form' : EmployeeForm()
        }
        return render(request,'employees/create.html',context=context)

    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('employee_list')
# def employee_create(request):
#     context = {
#        'form' : EmployeeForm()
#     }
#     return render(request,'employees/create.html',context=context)

# @require_http_methods(['POST'])
# def employee_store(request):
#     # name = request.POST.get('name')
#     # ssn = request.POST.get('ssn')
#     # salary = request.POST.get('salary')
#     # job_id = request.POST.get('job')
#     # job = Jobs.objects.get(id=job_id)
#     # emp = Employee.objects.create(name=name,ssn=ssn,salary=salary,job=job)
#         # Employee.objects.create(**form.cleaned_data)
#     form = EmployeeForm(request.POST)
#     if form.is_valid():
#         form.save()
#     return redirect('employee_list')

def employee_edit(request,id):
    employee = Employee.objects.get(id=id)
      
    context = {
       'form' : EmployeeForm(instance=employee),
       'is_edit' : True
    }
    # print(context['form'])
    return render(request,'employees/create.html',context=context)


@require_http_methods(['POST'])
def employee_update(request,id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(data=request.POST,instance=employee)
    if form.is_valid():
        form.save()
    return redirect('employee_list')

class UpdateDeleteEmployeeView(View):
    def get(self, request, id):
        employee = Employee.objects.get(id=id)
        context = {
        'form' : EmployeeForm(instance=employee),
        'is_edit' : True
        }
        # print(context['form'])
        return render(request,'employees/create.html',context=context)
    def post(self, request, id):
        employee = Employee.objects.get(id=id)
        form = EmployeeForm(data=request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('employee_list')
@require_http_methods(['POST'])
def employee_delete( request, id):
    Employee.objects.get(id=id).delete()
    return redirect('employee_list')
        
from django.views.generic.detail import DetailView
from django.db.models import Sum

class EmployeeDetailView(DetailView):
    model = Employee
    template_name ='employees/info.html'
    context_object_name = 'employee'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_increases = context["employee"].increases.aggregate(total=Sum('amount'))['total'] or 0
        total_deductions = context["employee"].deductions.aggregate(total=Sum('amount'))['total'] or 0
        total_salary = context["employee"].salary + (total_increases - total_deductions)
        context.update({
            'total_increases' : total_increases,
            'total_deductions' : total_deductions,
            'total_salary' : total_salary
        })
        print(context)
        return context
    
