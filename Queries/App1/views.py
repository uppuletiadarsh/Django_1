from django.shortcuts import render

# Create your views here.
def insert(request):
    return render(request,'insert.html')


from django.shortcuts import render, redirect
from .models import Employee


def save(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        department_id = request.POST.get('department_id')
        gender = request.POST.get('gender')

        salary = request.POST.get('salary')

        # Fetch or create Language objects for selected languages

        # Create Employee object
        employee = Employee.objects.create(
            employee_id=employee_id,
            name=name,
            email=email,
            department_id=department_id,
            gender=gender,
            salary=salary
        )
        # Redirect to some success page or do something else
        return redirect('insert')  # Change 'success_page' to your desired URL
    # If request method is not POST, render the form template
    return render(request, 'insert.html')
def q1(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        try:
            det = Employee.objects.filter(employee_id=id)
            return render(request, 'q1.html', {'det': det,'id': id })
        except Employee.DoesNotExist:
            return render(request, 'q1.html', {'message': 'Record Not Found'})


    return render(request, 'q1.html')

def q2(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        try:
            det = Employee.objects.filter(salary__gte=id)
            return render(request, 'q2.html', {'det': det,'id': id })
        except Employee.DoesNotExist:
            return render(request, 'q2.html', {'message': 'Record Not Found'})

    return render(request, 'q2.html')
def q3(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        try:
            det = Employee.objects.exclude(department_id=id)
            return render(request, 'q3.html', {'det': det,'id': id })
        except Employee.DoesNotExist:
            return render(request, 'q3.html', {'message': 'Record Not Found'})

    return render(request, 'q3.html')
def q4(request):
    if request.method=="POST":
        id = request.POST.get('id')
        try:
            det = Employee.objects.filter(name__startswith=id)
            return render(request,'q4.html',{'det':det,'id':id})
        except Employee.DoesNotExist:
            return render(request,'q4.html')
    return render(request,'q4.html')
