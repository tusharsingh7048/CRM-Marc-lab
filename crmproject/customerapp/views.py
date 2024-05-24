from django.shortcuts import render,redirect
from crmapp.models import Customer,Login
from django.views.decorators.cache import cache_control
from.models import Response,Orders
import datetime
from adminapp.models import Product


# Create your views here.
@cache_control(no_cache=True,must_revalidate=True, no_store=True)
def customerhome(request):
    try:
        if request.session["userid"]!=None:
            cust=Customer.objects.get(emailaddress=request.session["userid"])
            return render(request,"customerhome.html",locals())
    except KeyError:
        return redirect('crmapp:login')
    
def logout(request):
    try:
        del request.session["userid"]

    except KeyError:
        return redirect('crmapp:login')
    return redirect('crmapp:login')

@cache_control(no_cache=True,must_revalidate=True, no_store=True)
def response(request):
    try:
        if request.session["userid"]!=None:
            cust=Customer.objects.get(emailaddress=request.session["userid"])
            if request.method=="POST":
                name=cust.name
                contactno=cust.contactno
                emailaddress=cust.emailaddress
                responsetype=request.POST["responsetype"]
                subject=request.POST["subject"]
                responsetext=request.POST["responsetext"]
                posteddate=datetime.datetime.today()
                res=Response(name=name,contactno=contactno,emailaddress=emailaddress,responsetype=responsetype,subject=subject,responsetext=responsetext,posteddate=posteddate)
                res.save()
                msg="Response is submitted"
                return render(request,"response.html",locals())
            return render(request,"response.html",locals())
    except KeyError:
        return redirect('crmapp:login')
    

@cache_control(no_cache=True,must_revalidate=True, no_store=True)
def changepassword(request):
    try:
        if request.session['userid']!=None:
            if request.method=='POST':
                cust=Login.objects.get(userid=request.session['userid'])
                oldpassword=request.POST['oldpassword']
                newpassword=request.POST['newpassword']
                conpassword=request.POST['conpassword']
                if cust.password==oldpassword:
                    if oldpassword==newpassword:
                        msg="old and new password are same!!!"
                    else:
                        if newpassword==conpassword:
                            cust.password=newpassword
                            cust.save()
                            msg="Passwors changes successfully"

                        else:
                            msg="confirm Password didnt Matched"
                else:
                    msg="old Paaword not matched"

            return render(request,'changepassword.html',locals())
    except:
        return redirect('crmapp:login')
    return render(request,'changepassword.html')
@cache_control(no_cache=True,must_revalidate=True, no_store=True)
def viewprofile(request):
    try:
        if request.session["userid"]!=None:
            cust=Customer.objects.get(emailaddress=request.session["userid"])
            if request.method=="POST":
                 name=request.POST["name"]
                 gender=request.POST["gender"]
                 address=request.POST["address"]
                 contactno=request.POST["contactno"]
                 emailaddress=request.POST["emailaddress"]
                 Customer.objects.filter(emailaddress=emailaddress).update(name=name,gender=gender,address=address,contactno=contactno)
                 return redirect("customerapp:customerhome")
            return render(request,"viewprofile.html",locals())
    except KeyError:
        return redirect('crmapp:login')
    
@cache_control(no_cache=True,must_revalidate=True, no_store=True)
def products(request):
    try:
        if request.session["userid"]!=None:
            cust=Customer.objects.get(emailaddress=request.session["userid"])
            prod=Product.objects.filter(avail='true')
            return render(request,"products.html",locals())
    except KeyError:
        return redirect('crmapp:login')
    
def buy(request,id):
    try:
        if request.session["userid"]!=None:
            cust=Customer.objects.get(emailaddress=request.session["userid"])
            prod=Product.objects.get(id=id)
            productname=prod.productname
            price=prod.price
            name=cust.name
            contactno=cust.contactno
            emailaddress=cust.emailaddress
            buydate=datetime.datetime.today()
            ord=Orders(productname=productname,name=name,price=price,contactno=contactno,emailaddress=emailaddress,buydate=buydate)
            ord.save()
            Product.objects.filter(id=id).update(avail='false')
            return redirect('customerapp:vieworders')
    except KeyError:
        return redirect('crmapp:login')

@cache_control(no_cache=True,must_revalidate=True, no_store=True)
def vieworders(request):
    try:
        if request.session["userid"]!=None:
            cust=Customer.objects.get(emailaddress=request.session["userid"])
            ord=Orders.objects.filter(emailaddress=cust.emailaddress)
            return render(request,"vieworders.html",locals())
    except KeyError:
        return redirect('crmapp:login')