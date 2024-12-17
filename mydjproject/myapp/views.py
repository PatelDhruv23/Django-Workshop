from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import student
from .forms import StudentForm

def homepage(request):
    return render(request,'home.html')

def homepageahmedabad(request):
    return render(request,'homeahm.html')

def homepagesurat(request):
    return render(request,'homesurat.html')


def aboutpage(request):
    return render(request,'about.html')

def contactpage(request):
    return render(request,'contact.html')

def testpage(request):
    return render(request,'test.html')

def formpageview(request):
    return render(request,'form.html')

def formpageprocess(request):
    a=int(request.POST["txt1"])
    b=int(request.POST["txt2"])
    c=a+b
    return render(request,"ans.html",{'mya':a,'myb':b,'sum':c})

def marksheetview(request):
    return render(request,'marksheet.html')

def marksheetprocess(request):
    s1=int(request.POST["txt1"])
    s2=int(request.POST["txt2"])
    s3=int(request.POST["txt3"])
    s4=int(request.POST["txt4"])
    avg = (s1 + s2 + s3 + s4) /4
    return render(request,"marksoutput.html",{'mys1':s1, 'mys2':s2, 'mys3':s3, 'mys4':s4, 'myavg':avg})


def addstudent(request):
    if request.method == 'GET':
        context = {'form':StudentForm()}
        return render(request,'add.html',context)
    
    elif request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(addstudent)
        else:
            return render(request, 'add.html',{'form': form})
        
def displaystudent(request):
    dbdata = student.objects.all()
    context = {'mydata':dbdata}
    return render(request,'display.html',context)
    
# Create your views here.+

