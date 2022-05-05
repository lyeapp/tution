from django.shortcuts import redirect, render
import django
from django.contrib.auth.models import User
from tuitionapp.forms import userC,Stud,Tut
from tuitionapp.models import userClass,Student,Tutor
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')
def signup(request):
    return render(request,'signup.html')

def loginpage(request):
    return render(request,'login.html')

@login_required(login_url='userlogin')
def about(request):
  return render(request,'enter.html')

def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This usernae already exists!!!')
                print("Username already taken..")
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username= username,
                    password= password,
                    email= email)
                user.save()
                print("successed")
                return redirect('addstud')
        else:
            messages.info(request,'Password doesnt match!!!!')
            print("password is not matching...")
            return redirect('signup')
    
    else:
        return render(request,'signup.html')

def userlogin(request):
   if request.method == 'POST':
       username=request.POST['username']
       password=request.POST['password']
       user=auth.authenticate(username=username,password=password)
       if user is not None:
           auth.login(request,user)
           messages.info(request, f'Welcome {username}')
           return redirect('about')
       else:
           messages.info(request,'Invalid Username or Password.Try Again.')
           return redirect('loginpage')
   else:
       return redirect('loginpage')

@login_required(login_url='userlogin')
def userlogout(request):
   auth.logout(request)
   return redirect('home')
#enter class details
@login_required(login_url='userlogin')
def addc(request):
    form=userC()   
    return render(request,'addc.html',{'form':form})
@login_required            
def addclass(request):
    print('f9')
    if request.method=='POST':
        print('10')
        form=userC(request.POST,request.FILES)
        if form.is_valid():
            print('12')
            form.save()
            return redirect ('show_c')
    form=userC()
    return render(request,'addc.html',{'form':form})  

#Show Employee
@login_required
def show_c (request): 
    emp=userClass.objects.all()
    return render(request, 'showc.html',{'emp':emp})
#edit
@login_required
def edit_c (request,pk): 
    fo=userClass.objects.get(id=pk)
    form=userC(instance=fo)
    if request.method=='POST':
        form=userC(request.POST,request.FILES,instance=fo)
        if form.is_valid():
            form.save()
            return redirect('show_c')
    return render(request, 'editc.html',{'form':form})

#delete
@login_required
def delete_c(request,pk):
    form=userClass.objects.get(id=pk)
    form.delete()
    return redirect('show_c')

#ADD Student
# def adds(request):
#     form=Stud()   
#     return render(request,'adds.html',{'form':form})
            
# def addstud(request):
#     print('f9')
#     if request.method=='POST':
#         print('10')
#         form=Stud(request.POST,request.FILES,)
#         if form.is_valid():
#             print('12')
#             form.save()
#             img_object = form.instance 
#             return redirect ('userlogin')
#     form=()
#     return render(request,'adds.html',{'form':form,'img_obj': img_object})  

# #Show Employee
# def show_s (request): 
#     emp=Student.objects.all()
#     return render(request, 'shows.html',{'emp':emp})
# #edit
# def edit_s (request,pk): 
#     fo=Student.objects.get(id=pk)
#     form=Stud(instance=fo)
#     if request.method=='POST':
#         form=Stud(request.POST,request.FILES,instance=fo)
#         if form.is_valid():
#             form.save()
#             return redirect('show_s')
#     return render(request, 'edits.html',{'form':form})

# #delete
# def delete_s(request,pk):
#     form=Student.objects.get(id=pk)
#     form.delete()
#     return redirect('show_s')

# add product
@login_required
def adds(request):
    if request.user.is_authenticated:
        
        e=userClass.objects.all()
        context= {'we':e}
        return render(request,'adds.html',context)
    return redirect('login')
@login_required
def addstud(request):
    if request.method == 'POST':
        sname=request.POST['student']
        dob=request.POST['dob']
        gender=request.POST['gender']
        gnam=request.POST['grade']
        gnam=userClass.objects.get(id=gnam)
        pnam=request.POST['Pname']
        email=request.POST['email']
        cn=request.POST['Contactno']
        pimage = request.FILES['image']
        stu=Student(Studentname=sname,
            DOB=dob,
            Gender=gender,
            Grade=gnam,
            Parentname=pnam,
            email=email,
            contactno=cn,
            simage=pimage,
            )
        stu.save()
        print('success')
        return redirect('userlogin')
    ve=userClass.objects.all()
    return render(request,'adds.html',{'e':ve} )

# #Show Employee
@login_required
def show_s (request):
    emp=Student.objects.all()
    return render(request, 'shows.html',{'emp':emp})




@login_required
def edit (request,pk): 
    stud=Student.objects.get(id=pk)
    std=userClass.objects.get(id=pk)
    return render(request, 'edits.html', {'stud': stud,'std':std})
@login_required
def edit_s(request,pk):
    if request.method=='POST':
        stud=Student.objects.get(id=pk)
        stud.Studentname = request.POST.get('student')
        stud.DOB = request.POST.get('dob')
        stud.Gender = request.POST.get('gender')
        stud.Grade = request.POST.get('grade')
        stud.Parentname = request.POST.get('Pname')
        stud.email=request.POST.get('email')
        stud.contactno = request.POST.get('Contactno')
        stud.simage=request.POST.get('image')
        stud.save() 
        print("successfully updated")
        return redirect('show_s')
    return render(request,'edits.html')
@login_required
def delete_s(request,pk):
     stu=Student.objects.get(id=pk)
     stu.delete()  
     print("successfully deleted")
     return redirect('show_s')

#ADD TUTOR
@login_required
def addt(request):
    form=Tut()   
    return render(request,'addt.html',{'form':form})
@login_required           
def addtutor(request):
    print('f9')
    if request.method=='POST':
        print('10')
        form=Tut(request.POST,request.FILES)
        if form.is_valid():
            print('12')
            form.save()
            return redirect ('show_t')
    form=()
    return render(request,'addt.html',{'form':form})  

#Show Employee
@login_required
def show_t (request): 
    emp=Tutor.objects.all()
    em=userClass.objects.all()
    return render(request, 'showt.html',{'emp':emp},{'em':em})
#edit
@login_required
def edit_t (request,pk): 
    fo=Tutor.objects.get(id=pk)
    form=Tut(instance=fo)
    if request.method=='POST':
        form=Tut(request.POST,request.FILES,instance=fo)
        if form.is_valid():
            form.save()
            return redirect('show_t')
    return render(request, 'editt.html',{'form':form})

#delete
@login_required
def delete_t(request,pk):
    form=Tutor.objects.get(id=pk)
    form.delete()
    return redirect('show_t')



@login_required
def profile(request):
    addresses = User.objects.filter(first_name=request.user)
    return render(request, 'profile.html',{'addresses':addresses})