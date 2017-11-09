# -*- coding: utf-8 -*-
"""
Project: Hexon
Created on: Sun Nov 05 20:36:23 2017
@author: dualstream799
GitHub: 
"""

# ------------------ IMPORTING LIBRARIES ------------------- #
# Kivy stuff
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
# Other stuff
import json


from kivy.uix.progressbar import ProgressBar

class HexonConsole(GridLayout):
	pass
# ----------------------- MAIN CLASS ----------------------- #

class HexonApp(App):
	def build(self):
		return GridLayout()


# ----------------------- EXECUTING ------------------------ #
HexonApp().run()
