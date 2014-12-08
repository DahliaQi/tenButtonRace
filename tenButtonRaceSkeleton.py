#! /usr/bin/evn python

import wx # import the graphical library
import time # import the time module
from random import randint
from specialInput import *

class TenButtonFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Button Race")
		
		#Make a new Panel
		self.panel = wx.Panel(self)
		
		#Make the start button
		self.startButton = wx.Button(self.panel, label = "start", pos = (111, 131))
		self.startButton.Bind(wx.EVT_BUTTON, self.OnStart)		

		#Make the other ten buttons
		self.buttons = []
		
		for i in range(10):
			a = randint(0, 233)
			b = randint(0, 111)
			self.buttons.append(wx.Button(self.panel, label = "button" + str(i + 1), pos =(a, b)))
			self.buttons[i].Show(False)
			self.buttons[i].Bind(wx.EVT_BUTTON, self.onButtons)
		 
		#Hide the other ten buttons
		
		#Bind all the buttons to their event handlers
		
	# Event handler for the start button
	def OnStart(self, e):
		self.startButton.Show(False)
		#Make the start button disappear
		
		self.startTime = time.time()
		self.buttons[0].Show(True)
		#Make Button One appear
		
	def onButtons(self, e):
		clickButton = e.GetEventObject()
		clickButton.Show(False)
		
		for i in range(10):
			if clickButton == self.buttons[i]:
				if i <= 8:
					self.buttons[i + 1].Show(True)
				
				elif i == 9:
					self.endTime = time.time()
					actualTime = self.endTime - self.startTime
					actualTime = round(actualTime, 2)
					self.result = wx.StaticText(self.panel, label = "It takes you {}s to finish clicking.".format(actualTime), pos = (88, 11))
					 
		
	#Other event handlers here
	
	#Remember the last event handler needs to print the final time.
	
	
# -------- Main Program Below ------------

app = wx.App(False)
frame = TenButtonFrame(None)
frame.Show()
app.MainLoop()