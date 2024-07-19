from django.shortcuts import render,redirect
from . models import Details
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def insert(req):
    return render(req,'insert.html')
def save(req):
    if req.method == "POST":
        htno = req.POST.get('htno')
        name = req.POST.get('name')
        sub1 = int(req.POST.get('sub1'))
        sub2 = int(req.POST.get('sub2'))
        sub3 = int(req.POST.get('sub3'))
        avg = float((sub1 + sub2 + sub3) / 3)
        total = float(sub1 + sub2 + sub3)
        if avg >= 40:
            status = "Pass"
        else:
            status = "Fail"
        details = Details(Htno=htno, Name=name, sub1=sub1, sub2=sub2, sub3=sub3, Avg=avg, total=total)
        details.save()
        return redirect('insert',status=status)


def search(request):
    if request.method == 'POST':
        htno = request.POST.get('htno')
        try:
            det = Details.objects.filter(Htno=htno)
            return render(request, 'search.html', {'det': det,'id':htno })
        except Details.DoesNotExist:
            return render(request, 'search.html', {'message': 'Record Not Found'})
    return render(request, 'search.html')