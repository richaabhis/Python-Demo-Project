from django.shortcuts import render, redirect

from CRUD.models import Employee


# Create your views here.
def INDEX(request):
    emp = Employee.objects.all()
    context = {'emp': emp}  # dictionary
    return render(request, 'Home.html', context)


def addEmployee(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Address = request.POST.get('Address')
        Phone = request.POST.get('Phone')

        employee = Employee(
            Name=Name,
            Email=Email,
            Address=Address,
            Phone=Phone
        )

        employee.save()
        return redirect('home')

    return render(request, 'Home.html')


def editEmployee(request):
    emp = Employee.objects.all()
    context = {'emp': emp}
    return redirect(request, 'Home.html', context)


def updateEmployee(request, id):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Address = request.POST.get('Address')
        Phone = request.POST.get('Phone')

        employee = Employee(
            id=id,
            Name=Name,
            Email=Email,
            Address=Address,
            Phone=Phone
        )

        employee.save()
        return redirect('home')

    return redirect(request, 'Home.html')


def deleteEmployee(request, id):
    emp = Employee.objects.filter(id=id)
    emp.delete()
    return redirect('home')
