from django.urls import path
from .views import * #ดึง function homepage มาทำงาน

urlpatterns = [
	#localhost:8000/
	
	path('',LoginPage,name='login-page'),
	path('home/',Homepage,name='home-page'),
	path('about/', AboutPage,name='about-page'),
	path('contactus/',ContactPage,name='contact-page'),
	path('score/',ShowScore,name='score-page'),
	path('register/',Register,name='register-page')
]
