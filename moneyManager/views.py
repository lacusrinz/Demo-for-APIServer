from django.http import HttpResponse
from moneyManager.models import User
from django.shortcuts import render_to_response

def login(request):
	if 'email' in request.POST:
		if 'password' in request.POST:
			email = request.POST['email']
			password = request.POST['password']
			user = User.objects.filter(email__icontains = email)
			if user[0].password == password:
				return render_to_response("hero2.html",{'name':email})
	return render_to_response("hero.html",{})

def register(request):
	return render_to_response("hero3.html",{})
