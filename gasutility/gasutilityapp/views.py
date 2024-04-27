from django.shortcuts import render,HttpResponse, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from gasutilityapp.models import Connections,BookingGass
from django.utils import timezone

# Create your views here.
'''
def about(request):
    return HttpResponse("Hello")
'''
'''
createsuperuser
username = Admin123
Email Address = admin123@gmail.com
password = Admin123@

'''

def register(request):
    context={}
    if request.method=="GET":
        return render(request, 'register.html')
    else:
        n = request.POST.get('uname')
        p = request.POST.get('upass')
        cp = request.POST.get('ucpass')

        if n=='' or p=='' or cp=='':
            context['errmsg']="Fields Cannot be blank"
            return render(request,'register.html',context)
        
        elif p!=cp:
            context['errmsg']="Password & Confirm password didn't match"
            return render(request,'register.html',context)
        
        elif len(p)<8 or len(p)>15:
            context['errmsg']="Password must be minimum 8 & Maximum 15"
            return render(request,'register.html',context)
        
        else:
            try:
                u=User.objects.create(username=n)
                u.set_password(p)
                u.save()
                context['success']="User Created Successfully..!!"
                return render(request,'register.html',context)
            except Exception:
                context['errmsg']="User Already exist. Please Login"
                return render(request,'register.html',context)


def user_login(request):
    if request.method=="GET":
        return render(request,'login.html')
    else:
        n=request.POST['uname']
        p=request.POST['upass']
        u=authenticate(username=n,password=p)

        if u is not None:
            login(request,u)
            return redirect('/home')
        
        else:
            context={}
            context['errmsg']="Invalid username or password."
            return render(request,'login.html',context)

@login_required
def user_logout(request):
    logout(request)
    return redirect('/home')

@login_required
def connection(request):
    context={}
    if request.method=="GET":
        return render(request,'connection.html')
    else:
        cnm = request.POST['cname']
        cmail = request.POST['cemail']
        cmob = request.POST['cmobile']
        cgen = request.POST['cgender']
        cstat = request.POST['cstatus']
        cadhar = request.POST['caadhar']
        cadd = request.POST['caddress']
        cpin = request.POST['cpincode']
        cdob = request.POST['cdob']
       
        if cnm=='' or cmail=='' or cmob=='' or cgen=='' or cstat=='' or cadhar=='' or cadd=='' or cpin=='' or cdob=='':
            context['errmsg']="Fields Cannot be blank"
            return render(request,'connection.html',context)
        
        elif len(cmob)!=10:
            context['errmsg']="Invalid Mobile Number..Please enter valid mobile number..!"
            return render(request,'connection.html',context)
        
        elif len(cpin)!=6:
            context['errmsg']="Invalid Pincode..Please enter valid pincode..!"
            return render(request,'connection.html',context)

        elif len(cadhar)!=12:
            context['errmsg']="Invalid aadhar card number..!!"
            return render(request,'connection.html',context)

        else:
            c=Connections.objects.create(cname=cnm,cemail=cmail,cmobile=cmob,cgender=cgen,cstatus=cstat,caadhar=cadhar,caddress=cadd,cpincode=cpin,cdob=cdob)
            c.save()
            context['success']="Connection Created Successfully..!!"
            return render(request,'connection.html',context)

@login_required
def viewconnection(request):
    c=Connections.objects.all()
    context={}
    context['data']=c
    return render(request,'viewconnection.html',context)

@login_required
def editconnection(request,rid):
    context={}
    if request.method=="GET":
        c=Connections.objects.filter(id=rid)
        context['data']=c
        return render(request,'editconnection.html',context)

    else:
        cnm = request.POST['cname']
        cmail = request.POST['cemail']
        cmob = request.POST['cmobile']
        cgen = request.POST['cgender']
        cstat = request.POST['cstatus']
        cadhar = request.POST['caadhar']
        cadd = request.POST['caddress']
        cpin = request.POST['cpincode']
        cdob = request.POST['cdob']

        #c=Connection.objects.create(cname=cnm,cemail=cmail,cmobile=cmob,cgender=cgen,cstatus=cstat,caadhar=cadhar,caddress=cadd,cpincode=cpin,cdate=cdt)
        c=Connections.objects.filter(id=rid)
        c.update(cname=cnm,cemail=cmail,cmobile=cmob,cgender=cgen,cstatus=cstat,caadhar=cadhar,caddress=cadd,cpincode=cpin,cdob=cdob)
        context['success']="Connection Updated Successfully..!!"
        return redirect('/viewconnection')

@login_required
def deleteconnection(request,rid):
    context={}
    c=Connections.objects.filter(id=rid)
    c.delete()
    context['success']="Connection Deleted Successfully..!!"
    return redirect('/viewconnection')

@login_required  
def booking(request,rid):
    context={}
    if request.method=="GET":
        c=get_object_or_404(Connections, id=rid)
        context['data']=c
        return render(request,'booking.html',context)
    else:
        bnm = request.POST['name']
        bmail = request.POST['email']
        bmob = request.POST['mobile']
        badd = request.POST['address']
        bref = request.POST['ref']
        #bstat = request.POST['status']
       
        if bnm=='' or bmail=='' or bmob=='' or badd=='' or bref=='':
            context['errmsg']="Fields Cannot be blank"
            return render(request,'booking.html',context)

        else:
            c=get_object_or_404(Connections, id=rid)
            b=BookingGass.objects.create(connection=c,name=bnm,email=bmail,mobile=bmob,address=badd,ref=bref)
            b.save()
            context['success']="Cylinder Booked Successfully..!!"
            return render(request,'booking.html',context)

@login_required
def viewbooking(request):
    b=BookingGass.objects.all()
    context={}
    context['data']=b
    return render(request,'viewbooking.html',context)

@login_required
def deletebooking(request,rid):
    context={}
    b=BookingGass.objects.filter(id=rid)
    b.delete()
    context['success']="Booking Deleted Successfully..!!"
    return redirect('/viewbooking')

def home(request):
    return render(request,'home.html')

