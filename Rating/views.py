# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
#from django.core import serializers
from Rating.models import Player, Game
import json
from django.core import serializers



def getall(request):
	players = Player.objects.all()
	dumpResult = makeJSON(players)
	if 'callback' in request.GET:
		callback = request.GET['callback']
		dumpResult = '%s(%s)' % (callback,dumpResult)
	return HttpResponse(dumpResult)

def search(request):
	name = request.GET['name']
	players = Player.objects.filter(name__icontains=name)
	print players
	dumpResult = makeJSON(players)
	if 'callback' in request.GET:
		callback = request.GET['callback']
		dumpResult = '%s(%s)' % (callback,dumpResult)
	return HttpResponse(dumpResult)

def postsearch(request):
	name = request.POST['name']
	print name
	players = Player.objects.filter(name__icontains=name)
	dumpResult = makeJSON(players)
	if 'callback' in request.GET:
		callback = request.GET['callback']
		dumpResult = '%s(%s)' % (callback,dumpResult)
	return HttpResponse(dumpResult)

def makeJSON(players):
	dict = {}
	list = []
	if not players:
		dict['resultCode'] = -1
	else:
		dict['resultCode'] = 1
		for player in players:
			res = {}
			res['name'] = player.name
			res['game'] = player.game.name
			res['rating'] = player.rating
			list += [res]
			print list
	dict['result'] = list
	dumpResult = json.dumps(dict)
	return dumpResult

