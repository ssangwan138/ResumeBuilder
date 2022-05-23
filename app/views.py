from operator import imod
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import resume_info

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        # Redirect to a success page.
        else:
            messages.success(request, "There was an error logging in")
            return redirect('login')
    return render(request, 'resumecreator/login_user.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        user = authenticate(username=username, password=password, email=email)
        login(request, user)
        messages.success(request, ("Registration Successful"))
        return redirect('index')
    else:
        return render(request, 'resumecreator/register.html')


def index(request):
    return render(request, 'resumecreator/index.html')


def create_resume(request):
    if request.method=="POST":
        full_name=request.POST.get("name")
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        about_you=request.POST.get("about")
        education=request.POST.get("education")
        career=request.POST.get("career")
        job_1__start=request.POST.get("job-1__start")
        job_1__end=request.POST.get("job-1__end")
        job_1__details=request.POST.get("job-1__details")
        job_2__start=request.POST.get("job-2__start")
        job_2__end=request.POST.get("job-2__end")
        job_2__details=request.POST.get("job-2__details")
        job_3__start=request.POST.get("job-3__start")
        job_3__end=request.POST.get("job-3__end")
        job_3__details=request.POST.get("job-3__details")
        references=request.POST.get("references")
        new_resume = resume_info(
            full_name=full_name,
            address=address,
            phone=phone,
            email=email,
            about_you=about_you,
            education=education,
            career=career,
            job1details=job_1__details,
            job1start=job_1__start,
            job1end=job_1__end,
            job2details=job_2__details,
            job2start=job_2__start,
            job2end=job_2__end,
            job3details=job_3__details,
            job3start=job_3__start,
            job3end=job_3__end,
            references=references,
        )
        new_resume.save()
        messages.add_message(request, messages.INFO, 'Resume Info Saved Successfully. Download Resume Now')
        return redirect("resume")
    return render(request, 'resumecreator/create_resume.html')

def resume(request):
    try:
        resume_information = resume_info.objects.get(id=2)
        print(resume_information)
        context={"resume_info":resume_information}
        return render(request,"resumecreator/resume.html",context)
    except:
        return render(request,"resumecreator/resume.html")