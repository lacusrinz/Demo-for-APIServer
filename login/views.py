# Create your views here.
from login.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response
import json
import hashlib

def login(request):
	name = request.POST['name']
	password = md5(request.POST['password'])
	user = User.objects.filter(name__icontains=name, password__exact=password)
	if not user:
		dumpResult = makeJSON(None, 'login', 0)
	else:
		dumpResult = makeJSON(user[0], 'login', 1)
	if 'callback' in request.GET:
		callback = request.GET['callback']
		dumpResult = '%s(%s)' % (callback,dumpResult)
	return HttpResponse(dumpResult)

def register(request):
	name = request.POST['name']
	print name
	IsExist = User.objects.filter(name__icontains=name)
	print IsExist
	password = md5(request.POST['password'])
	print password
	email = request.POST['email']
	if not IsExist:
		u = User(name = name, password = password, email = email)
		u.save()
		dumpResult = makeJSON(u, 'register', 1)
	else:
		dumpResult = makeJSON(None, 'register', 0)
	if 'callback' in request.GET:
		callback = request.GET['callback']
		dumpResult = '%s(%s)' % (callback,dumpResult)
	return HttpResponse(dumpResult)

def md5(str):
	m = hashlib.md5()
	m.update(str)
	return m.hexdigest()

def makeJSON(user, type, flag):
	dict = {}
	res = {}
	if flag == 1:
		dict['resultCode'] = 1
		dict['type'] = type
		dict['result'] = user.name
	else:
		dict['resultCode'] = -1
		dict['type'] = type
	print dict
	dumpResult = json.dumps(dict)
	return dumpResult


