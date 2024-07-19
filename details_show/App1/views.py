from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,'register.html')
def submit(request):
    if request.method == 'POST':
        person_id = request.POST.get('person_id')
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        hobbies = request.POST.getlist('hobbies')

        details={'person_id': person_id,
            'name': name,
            'age': age,
            'gender': gender,
            'city': city,
            'hobbies': hobbies,}

        return render(request,'details.html',details)
    else:
        return render(request, 'register.html')