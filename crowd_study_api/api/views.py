# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# For the sake of api stuff:
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

# Create your views here.
@api_view(['GET'])
@csrf_exempt
def index(request):
	return HttpResponse("Hmm")

@api_view(['GET'])
def allGroups(request):
	ag = []
	for sg in Sgroup.objects.all():
		print objToDictG(sg)
		ag.append(objToDictG(sg))
	return Response(ag)

@api_view(['GET'])
def groupById(request, group_id):
	# you take the zero just cause the query set will only respond with just a zero
	sg = objToDictG(Sgroup.objects.filter(id=group_id)[0])
	return Response([sg])

@api_view(['GET'])
def questionById(request, question_id):
	q = objToDictQ(Question.objects.filter(id=question_id)[0])
	return Response(q)

def objToDictG(group):
	dgroup = {
		"name": group.name,
		"password": group.password,
		"questions": [],
		"id": group.id
	}
	questions = Question.objects.filter(sgroup=group)

	for q in questions:
		dgroup["questions"].append(objToDictQ(q))

	return dgroup

def objToDictQ(question):
	dquestion = {
		"group": question.sgroup.id,
		"text": question.qText,
		"answer": question.answer,
		"id": question.id
	}

	return dquestion

@api_view(['POST'])
@parser_classes((JSONParser,))
@csrf_exempt
def makeGroup(request, format=None):
	print 'MAKING GROUP'
	sgN = Sgroup(name=request.GET.get('name'), password=request.GET.get('password'))
	sgN.save()
	return Response("all clear")

@api_view(['POST'])
@parser_classes((JSONParser,))
@csrf_exempt
def makeQuestion(request, format=None):
	print 'MAKING QUESTION'
	sg = Sgroup.objects.get(id=int(request.GET.get('sgid')))
	qN = Question(qText=request.GET.get('txt'), answer=request.GET.get('answer'), sgroup=sg)
	qN.save()
	return Response("all clear")
