from re import U
from django.shortcuts import render, redirect
from .models import Expense,MyUser
from django.http import HttpResponse
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as login_auth
from django.contrib.auth import authenticate, login, logout



# Create your views here.
# home

def home(request):
    print(request.user)
    expenses = Expense.objects.filter(userId=request.user)
    print(expenses)
    if request.POST:
        month = request.POST['month']
        year = request.POST['year']
        expenses = Expense.objects.filter(date__year=year, date__month=month)

   
    return render(request, 'index1.html', {'expenses': expenses})

# create
def add(request):
    if request.method == 'POST':
        item = request.POST['item']
        amount = request.POST['amount']
        category = request.POST['category']
        date = request.POST['date']

        expense = Expense(item=item, amount=amount, category=category, date=date,userId=request.user)
        
        expense.save()

    return redirect(home)

def update(request, id):
    id = int(id)
    expense_fetched = Expense.objects.get(id = id)
    if request.method == 'POST':
        item = request.POST['item']
        amount = request.POST['amount']
        category = request.POST['category']
        date = request.POST['date']

        expense_fetched.item = item
        expense_fetched.amount = amount
        expense_fetched.category = category
        expense_fetched.date = date

        expense_fetched.save()

    return redirect(home)

def delete(request, id):
    id = int(id)
    expense_fetched = Expense.objects.get(id = id)
    expense_fetched.delete()
    return redirect(home)


def signUp(request):
    userf = UserForm()

    if request.method == "POST":
        userf = UserForm(request.POST)
        if userf.is_valid():
            user=userf.save()
            user.set_password(user.password)
            user.save()
        return redirect(login)
    print(request.user)
    return render(request,'signup.html',{'form':userf})

def login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username,password=password)

        if user is not None:
            
            login_auth(request,user)
            return redirect(home)


    return render(request,'login.html')

# for logout
def logout_view(request):
    logout(request)
    return redirect(login)