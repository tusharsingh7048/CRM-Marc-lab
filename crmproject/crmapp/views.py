from django.shortcuts import render,redirect,reverse
from.models import Enquiry,Customer,Login
import datetime
from django.core.exceptions import ObjectDoesNotExist
from .smssender import sendsms

# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def registration(request):
 
    if request.method=='POST':
        name=request.POST['name']
        contactno=request.POST['contactno']
        email=request.POST['email']
        address=request.POST['address']
        gender=request.POST['gender'] 
        password=request.POST['password'] 
        copassword=request.POST['copassword'] 
        regdate=datetime.datetime.today()
        usertype='customer'
        if password==copassword:
            cust=Customer(name=name,gender=gender,address=address,emailaddress=email,contactno=contactno,regdate=regdate)
            valid=Login(userid=email,password=password,usertype=usertype)
            cust.save()
            valid.save()
            return render(request,'registration.html',
                          {'msg':'registration successful'})
        else:
           return render(request,"registration.html",
           {'msg':'password and copassowrd does not match'})    
    return render(request,"registration.html")
    
def login(request):
    if request.method=="POST":
        userid=request.POST['userid']
        password=request.POST['password']
        
        try:
            obj=Login.objects.get(userid=userid,password=password)
            if obj is not None:
                if obj.usertype=="customer":
                    request.session["userid"]=userid
                    return redirect(reverse("customerapp:customerhome"))
                elif obj.usertype=="admin":
                    request.session["adminid"]=userid
                    return redirect(reverse("adminapp:adminhome"))
        except ObjectDoesNotExist:
            msg="invalid user"
        return render(request,"login.html",{"msg":msg})
    return render(request,"login.html")
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']
        subject=request.POST['subject']
        message=request.POST['message']
        posteddate=datetime.datetime.today()
        enq=Enquiry(name=name,contactno=contactno,emailaddress=emailaddress,subject=subject,message=message,posteddate=posteddate)
        enq.save()
        sendsms(contactno)
        return render(request,"contact.html",{"msg":"Enquiry is saved"})
    return render(request,"contact.html")