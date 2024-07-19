from django.shortcuts import render

# Create your views here.
def count(request):
    if request.method == "POST" :
        if 'count' in request.COOKIES :
            newcount = int(request.COOKIES['count'])+1
        else :
                newcount = 0
        response = render(request,'count.html',{'count': newcount })
        response.set_cookie('count',newcount,max_age=60)
        return response
    return render(request,'count.html')