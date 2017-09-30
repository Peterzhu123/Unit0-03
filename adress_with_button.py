# Created by: Peter Zhu
# Created on: Aug 2016
# Created for: ICS3U
# This program is the Address progran, but with a button

import ui

def show_address_touch_up_inside(sender):
    #print ('Hello, World!')
    view['name_label'].text = ("Scarlett Gao")
    view['city_label'].text = ("Ottawa")
    view['country_label'].text = ("Canada")
    
view = ui.load_view()
view.present('sheet')
