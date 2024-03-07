from django.shortcuts import render,HttpResponse,redirect
from msgapp.models import Msg

# Create your views here.
def create(request):
    if request.method=="GET":
        #print("Request is :",request.method)
        return render(request,'create.html')
    else:
        n=request.POST['uname']
        mail=request.POST['email']
        mob=request.POST['mob']
        msg=request.POST['msg']

        print("Username is :",n)
        print("Email is :",mail)
        print("Mobile Number is :",mob)
        print("Message is :",msg)
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        m.save()
        #return HttpResponse("Data inserted")
        return redirect("/dashboard")

def dashboard(request):
    m=Msg.objects.all()
    #print(m)
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)

def delete(request,rid):
    #print("ID to be deleted:",rid)
    m=Msg.objects.filter(id=rid)
    m.delete()
    return redirect('/dashboard')

def edit(request,rid):
    if request.method=="GET":
        m=Msg.objects.get(id=rid)
        context={}
        context['data']=m
        return render(request,'edit.html',context)
    else:
        n=request.POST['uname']
        mail=request.POST['email']
        mob=request.POST['mob']
        msg=request.POST['msg']
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        m.save()

        m=Msg.objects.filter(id=rid)
        m.delete()
        #return HttpResponse("Data inserted")
        return redirect("/dashboard")