# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Sgroup(models.Model):
	name = models.CharField(max_length=100)
	password = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Question(models.Model):
	sgroup = models.ForeignKey(Sgroup, on_delete=models.CASCADE)
	qText = models.CharField(max_length=200)
	answer = models.CharField(max_length=60)

	def __str__(self):
		return self.qText
