from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from MasterStudentApp.code import *
from MasterStudentApp.models import Master, Student, Task


# Create your views here.
def index_fun(request):
    return render(request,'index.html')


def masterlog_fun(request):
    if request.method=='POST':
        s = Student.objects.all()
        email = request.POST['txtemail']
        password = request.POST['txtpwd']
        if Master.objects.filter(Q(M_Email=email) & Q(M_Password=password)).exists():
            return render(request,'Master_Home.html')
        else:
            return render(request,'MasterLog.html',{'data':'Invalid user Name or Password'})


    return render(request,'MasterLog.html',{'data':''})


def masterreg_fun(request):

    if request.method=="POST":
        m = Master()
        m.M_Name=request.POST['txtname']
        m.M_Mobile=request.POST['txtmobile']
        m.M_Email=request.POST['txtemail']
        m.M_Password=request.POST['txtpwd']
        m.save()
        return redirect('mlog')
    return render(request,'MasterReg.html')


def studentlog_fun(request):
    return render(request,'StudentLog.html')

def stddata_fun(request):
    email = request.POST['txtemail']
    password = request.POST['txtpwd']
    if Student.objects.filter(Q(S_Email=email) & Q(S_Password=password)).exists():
        s = Student.objects.get(S_Email=email)
        t = Task.objects.filter(Q(Students_id=s.id))
        # std_pnd_task = globals()[t]
        return render(request, 'StdTask.html', {'data': t})
    else:
        return render(request,'StudentLog.html',{"data":'Invalid User Name Or Password'})

def studentreg_fun(request):

    if request.method=="POST":
        s = Student()
        s.S_Name=request.POST['txtname']
        s.S_Mobile=request.POST['txtmobile']
        s.S_Email=request.POST['txtemail']
        s.S_Password=request.POST['txtpwd']
        s.save()
        return redirect('slog')
    return render(request,'StudentReg.html')


def taskdata_fun(request):
    t = Task()
    t.Left = request.POST['ddlfno']
    t.Right = request.POST['ddlsno']
    t.Operation = request.POST['ddlop']
    t.Students = Student.objects.get(S_Name=request.POST['ddlstd'])
    t.Status = False
    t.save()

    return redirect('m_home')


def slove_fun(request,id):
    task = Task.objects.get(id=id)
    left = task.Left
    left = globals()[left]
    right = task.Right
    right = globals()[right]
    op = task.Operation
    op = globals()[op]
    res = left(op(right()))
    task.Status=True
    task.save()


    return render(request,'res.html',{'res':res } )


def viewalltask_fun(request):
    t = Task.objects.all()
    return render(request,'taskstatus.html',{'data':t})


def a_task_fun(request):
    s = Student.objects.all()
    return render(request,'task.html',{'data':s})


def m_home_fun(request):
    return render(request,'Master_Home.html')