from django.shortcuts import render


def count_view(request):
    count=int(request.COOKIES.get('count',0))
    newcount=count+1
    response=render(request,'a2/home.html',{'count':newcount})
    response.set_cookie('count',newcount,max_age=10)
    return response

# Create your views here.
