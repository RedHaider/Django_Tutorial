from django.shortcuts import render, redirect

from django.views import View
from .models import Employee
from .forms import AddEmployeeForm

# Create your views here.

class Home(View):
    def get(self, request):
        emp_data = Employee.objects.all()
        return render(request, 'core/home.html',{'empdata':emp_data})
    
class AddEmployee(View):
    def get(self, request):
        form = AddEmployeeForm()
        return render(request, 'core/addemployee.html', {'form':form})
    
    def post(self, request):
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request,'core/addemployee.html', {'form':form} )
        
class Delete_Employee(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        emp_data = Employee.objects.get(id=id)
        emp_data.delete()
        return redirect('/')

    
class EditEmployee(View):
    def get(self, request, id):
        emp_data = Employee.objects.get(id=id)
        form = AddEmployeeForm(instance=emp_data)
        return render(request, 'core/editemployee.html', {'form':form} )
    
    def post(self, request, id):
        emp_data = Employee.objects.get(id=id)
        form = AddEmployeeForm(request.POST, instance=emp_data)
        if form.is_valid:
            form.save()
            return redirect('/')