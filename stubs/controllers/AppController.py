#
#
# DO NOT EDIT THIS FILE.
# This file was autogenerated by python_on_wheels.
# Any manual edits may be overwritten without notification.
#
# 

# date created: 	2011-06-21

import sys
import os
from mako.template import Template
from mako.lookup import TemplateLookup
import datetime

sys.path.append( os.path.abspath(os.path.join( os.path.dirname(os.path.abspath(__file__)), "../lib" )))
sys.path.append( os.path.abspath(os.path.join( os.path.dirname(os.path.abspath(__file__)), "../models" )))
sys.path.append( os.path.abspath(os.path.join( os.path.dirname(os.path.abspath(__file__)), "../models/powmodels" )))
sys.path.append( os.path.abspath(os.path.join( os.path.dirname(os.path.abspath(__file__)), "../controllers" )) )

import powlib
import PowObject
import BaseController
import App

class AppController(BaseController.BaseController):
	
	def __init__(self):
		self.modelname = "App"
		BaseController.BaseController.__init__(self)
		self.login_required = []
		self.locked_actions = [ "login", "do_login", "logout"]
	
	def welcome( self,powdict ):
		return self.render(model=self.model, powdict=powdict)

	
	def login( self, powdict):
		self.model.__init__()
		return self.render(model=self.model, powdict=powdict)
	
	def do_login( self, powdict ):
		user = User.User()
		session = powdict["SESSION"]
		try:
			user = self.model.find_by("loginname",powdict["PARAMETERS"]["loginname"])
			if user.password == powdict["PARAMETERS"]["password"]:
				#login ok
				session["user.id"] = user.id
				session.save()
				return self.redirect("list",powdict=powdict)
			else:
				return self.redirect("login",powdict=powdict)
		except:
			return self.redirect("login", powdict=powdict)
	
	def logout( self, powdict):
		session = powdict["SESSION"]
		session["user.id"] = 0
		return self.redirect("list", powdict=powdict)
		
	
