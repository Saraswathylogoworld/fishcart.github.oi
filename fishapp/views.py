from django.shortcuts import render,redirect
from .models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from webFishapp.models import Fview_contact
from webFishapp.models import FCheckout
from webFishapp.models import Fwcart

# Create your views here.
def fun(request):
    return render(request,'index.html')

def cat(request):
    return render(request,'category.html')   

def display(request):
    if request.method=='POST':
        fname = request.POST.get('name')
        descpshn = request.POST.get('descpstn')
        img = request.FILES['img']
        data = fish(fname=fname,descpshn=descpshn,img=img)
        data.save()
        return redirect('tablec1')
        
def tablec1(request):
    data = fish.objects.all()
    return render(request,'tablecat.html',{'data':data})   

def catedit(request,cpid):
    data = fish.objects.filter(id=cpid)
    return render(request,'catedit.html',{'data':data})    

def catupdate(request,cuid):   
    if request.method=='POST':
        fname = request.POST.get('name')
        descpshn = request.POST.get('descpstn')
        try:
            img = request.FILES['img']
            fs = FileSystemStorage() 
            file = fs.save(img.name, img)
        except MultiValueDictKeyError :
            file=fish.objects.get(id=cuid).img
        data = fish.objects.filter(id=cuid).update(fname=fname,descpshn=descpshn,img=file)
    return redirect('tablec1')

def catdelete(request,cdid):
    data = fish.objects.filter(id=cdid)
    data.delete()
    return redirect('tablec1')    

def pro(request):
    data= pfish.objects.all()
    data1 = fish.objects.all()
    return render(request,'product.html',{'data':data,'data1':data1})

def display1(request):
    if request.method=='POST':
        pname = request.POST.get('pname')
        weight = request.POST.get('weight')
        cate = request.POST.get('cate')
        price = request.POST.get('pri')
        img = request.FILES['img']
        data = pfish(pname=pname,cate=cate,weight=weight,price=price,img=img)
        data.save()
    return redirect('ptable')

def ptable(request):
    data = pfish.objects.all()
    return render(request,'protable.html',{'data':data}) 

def edit(request,pid):
    data = pfish.objects.filter(id=pid)
    return render(request,'edit.html',{'data':data})    

def update(request,uid):   
    if request.method=='POST':
        pname = request.POST.get('pname')
        weight = request.POST.get('weight')
        cate = request.POST.get('cate')
        price = request.POST.get('pri')
        try:
            img = request.FILES['img']
            fs = FileSystemStorage() 
            file = fs.save(img.name, img)
        except MultiValueDictKeyError :
            file=pfish.objects.get(id=uid).img
        data = pfish.objects.filter(id=uid).update(pname=pname,cate=cate,weight=weight,price=price,img=file)
    return redirect('ptable')

def delete(request,did):
    data = pfish.objects.filter(id=did)
    data.delete()
    return redirect('ptable')    

def alogin(request):
        return render(request,'login.html')

def adlogin(request):
    username = request.POST.get('uname')
    password = request.POST.get('pswd')
    if User.objects.filter(username__contains=username).exists():
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            print(user)
            request.session['username']=username
            request.session['password']=password
            return redirect('fun')
        else:
            return render(request,'login.html',{'msg':"Sorry... Invalid username or password"})
    else:
        return redirect('alogin')

def Flogout(request):
    del request.session['username']
    del request.session['password']
    return redirect('alogin')        

def recipe(request):
    return render(request,'recipe.html')

def display2(request):
    if request.method=='POST':
        rname = request.POST.get('rname')
        instshn = request.POST.get('instshn')
        ingds = request.POST.get('ingds')
        img = request.FILES['img']
        data = rfish(rname=rname,instshn=instshn,ingds=ingds,img=img)
        data.save()
    return redirect('rtable')

def rtable(request):
    data = rfish.objects.all()
    return render(request,'rtable.html',{'data':data}) 

def redit(request,rid):
    data = rfish.objects.filter(id=rid)
    return render(request,'redit.html',{'data':data})    

def rupdate(request,ruid):   
    if request.method=='POST':
        rname = request.POST.get('rname')
        instshn = request.POST.get('instshn')
        ingds = request.POST.get('ingds')
        try:
            img = request.FILES['img']
            fs = FileSystemStorage() 
            file = fs.save(img.name, img)
        except MultiValueDictKeyError :
            file=rfish.objects.get(id=ruid).img
        data = rfish.objects.filter(id=ruid).update(rname=rname,instshn=instshn,ingds=ingds,img=file)
    return redirect('rtable')

def rdelete(request,rdid):
    data = rfish.objects.filter(id=rdid)
    data.delete()
    return redirect('rtable')


def tablecontact(request):
    data6 =Fview_contact.objects.all()
    return render(request,'contacttable.html',{'data6':data6}) 

def cdelete(request,coid):
    data6=Fview_contact.objects.filter(id=coid)
    data6.delete()
    return redirect('tablecontact')    

def Messagebox(request):
    return render(request,'messagebox.html')    

def tablecheckout(request):
    data7 =FCheckout.objects.all()
    return render(request,'Checkouttable.html',{'data7':data7}) 

def cartview(request):
    data9=Fwcart.objects.all()  
    return render(request,'cartid.html',{'data9':data9})      

