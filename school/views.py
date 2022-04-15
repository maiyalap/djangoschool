from django.shortcuts import render, redirect #ดึงมาจาก template
from django.http import HttpResponse #เขียนบนกระดานเอง
from .models import ExamScore
from django.contrib.auth.models import User

def Homepage(request):
	#return HttpResponse('<h1>Hello Da</h1>')
	return render(request,'school/home.html')

def AboutPage(request):
	return render(request,'school/about.html')	

def ContactPage(request):
	return render(request,'school/contactus.html')	

def ShowScore(request):
	score = ExamScore.objects.all() #ดึงค่ามาจาก database ทั้งหมด

	context = {'score':score}

	return render(request,'school/showscore.html',context)	

def Register(request):

	if request.method == "POST":
		data = request.POST.copy()
		first_name = data.get('first_name')
		last_name = data.get('last_name')
		email = data.get('email')
		password = data.get('password')

		newuser = User()
		newuser.username = email
		newuser.first_name = first_name
		newuser.last_name = last_name
		newuser.email = email
		newuser.set_password(password)
		newuser.save()

		#from django.shortcuts import render, redirect #ดึงมาจาก template
		return redirect('home-page')

	return render(request,'school/register.html')	

def LoginPage(request):
	return render(request,'school/login.html')
	