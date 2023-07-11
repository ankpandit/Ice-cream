from django.shortcuts import render,HttpResponse
from home.models import Contact
from home.models import emailSubscribe
from datetime import datetime 
from django.contrib import messages

# Create your views here.

def index(request):
    # return HttpResponse("this is Home Page")

    """context variable is a set of variable which are sended to templates
    access it by putting it in index.html
    {{<variable name }} == {{variable}}
    """
    context = {                                                         
        "variable" : "This String is sent through views.py" 
    }
    if(request.method=='POST'):
        email = request.POST.get('email')
        subs = emailSubscribe(email=email)
        subs.save()
        messages.success(request, 'Subscribed Successfully', extra_tags="subscribe")

    
    return render(request,'index.html' ,context) 

def about(request):
    return render(request , 'about.html')
    # return HttpResponse("<h1>this is about Page</h1>")
 
def contact(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        phone = request.POST.get('phone')
        # print(f"name{name} email{email}\ndesc={desc} phone={phone}")
        con= Contact(name=name,email=email,phone=phone,desc= desc,date=datetime.today())
        con.save()
        messages.success(request,"Message sent successfully !",extra_tags="contact")
        messages
        # messages.warning(request, "Message not sent ! Try Again ")

    return render(request , 'contact.html')
    # return HttpResponse("this is contact Page")
    
def services(request):
    return render(request , 'services.html')
    # return HttpResponse("this is services Page")


