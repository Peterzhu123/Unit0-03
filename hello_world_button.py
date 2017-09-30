# Created by: Peter Zhu
# Created on: 14-sep-2017
# Created for: ICS3U
# Daily Assignment - Unit0-03
# This program displays Hello, World!, but with "Click me"

import ui

def hello_world_touch_up_inside(sender):
	#print('Hello, World!')
  view['hello_world_label'].text = ("Hello, world!")
  
view = ui.load_view()
view.present('sheet')
