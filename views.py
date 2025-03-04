from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import CustomLoginForm,TransactionForm
from django.contrib import messages
from .models import Student,Transaction
# Create your views here.
def index(request):
    if request.method=="POST":
        form=CustomLoginForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)

            if user is not None and user.is_superuser:
                login(request,user)
                return redirect("home")
            else:
                messages.error(request, 'Invalid login credentials for superuser.')
    else:
        form=CustomLoginForm()
        return render(request,"index.html",{'form':form})
@login_required
def home(request):
    data=Student.objects.all()
    return render(request,"home.html",{'data':data})
def logout_user(request):
    logout(request)
    return redirect("index")
@login_required
def details(request,data):
    x=Student.objects.filter(Name=data)
    return render(request,"details.html",{"data":x[0]})
@login_required
def reciepts(request):
    if request.method=="POST":
        roll=request.POST.get("roll")
        transactions=Transaction.objects.filter(Roll=roll)
        if transactions.exists():
            return render(request,"reciepts.html",{'transactions':transactions})
        else:
            return render(request,"reciepts.html",{'data':'No Data Found'})
    else:
        return render(request,"reciepts.html")
def fee_dues(request):
    if request.method=="POST":
        transaction=TransactionForm(request.POST)
        if transaction.is_valid():
            transaction.save()
            form=TransactionForm()
            return redirect('feepay')
        else:
            form=TransactionForm()
            return render(request,'feepay.html',{'data':'Please Try Again','form':form})
    else:
        form=TransactionForm()
        return render(request,'feepay.html',{'form':form})
