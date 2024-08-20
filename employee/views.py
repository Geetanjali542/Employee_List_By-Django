
from django.shortcuts import get_object_or_404, render, redirect
from employee.forms import AddEmployee
from employee.models import Employee

# Create your views here.
# def add_employee(request):    
#     if request.POST:
#         form = AddEmployee(request.POST, request.FILES)  #request.FILES is for images
#         if form.is_valid():
#             form.save()
#         return redirect('home') 
#     return render(request, 'emloyee/add.html', {"form":AddEmployee})

def add_employ(request):
    if request.method == 'POST':
        name = request.POST['name']
        designation = request.POST['designation']
        email = request.POST['email']
        image = request.FILES['image']
        print(request)

        Employee.objects.create(name=name, designation=designation, email=email, image=image)
        return redirect('home') #reverse path name=home
    return render(request, 'emloyee/add_emp.html')
  
def delete_emp(request, pk):  #pk is the primary key that we passed as an url and is accessed here 
    objDelete = get_object_or_404(Employee, pk = pk)
    objDelete.delete()
    return redirect('home')

def edit_emp(request, pk):
    objEdit = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        objEdit.name = request.POST.get('name')
        # objEdit.name = request.POST.['name']
        objEdit.designation = request.POST.get('designation')
        objEdit.email = request.POST.get('email')
        objEdit.image = request.FILES.get('image')
        objEdit.save()
        return redirect('home')
    else:
        context = {
            'objEdit' : objEdit,

            
        }
        return render(request, 'emloyee/edit_emp.html', context)



#
