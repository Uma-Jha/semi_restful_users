# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['first_name']) < 2:
			errors['first_name'] = "First name should be more than 1 character"
		elif any(char.isdigit() for char in postData['first_name']) == True:
			errors['first_name'] = "First name shouldn't contain numbers"
		if len(postData['last_name']) < 2:
			errors['last_name'] = "Last name should be more than 1 character"
		elif any(char.isdigit() for char in postData['last_name']) == True:
			errors['last_name'] = "Last name shouldn't contain numbers"
		if len(postData['email']) < 1:
			errors['email'] = "Email should not be blank"
		elif not EMAIL_REGEX.match(postData['email']):
			errors['email'] = "Email is not valid!"
		return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
