from django.shortcuts import render
from . models import UserData
# from .filters import OrderFilter

# Create your views here.

def index(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('url') and request.POST.get('phone'):
            post=UserData()
            post.name= request.POST.get('name')
            post.url= request.POST.get('url')
            post.phone= request.POST.get('phone')
            post.save()
            
            return render(request, 'index.html')  
    else:
        return render(request,'index.html')

# def Search(request):
#     myFilter = OrderFilter()
#     context = {

#     }



