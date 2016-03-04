#!/usr/bin/env python
# encoding: utf-8
from datetime import datetime
import npyscreen
import curses

global ft1

class mode(npyscreen.TitleSelectOne):
      def when_value_edited(self):
          if self.value[0]==0:
             print("Mode Changed")
             curses.beep()
             self.parent.parentApp.application_logic.label(self.parent.ft1.value)
             #self.parent.getForm('P3').value =1000 
             #self.parent.getForm('P3').update() 
             self.update()              
          else:
             print("Val is "+str(self.value[0]))

#Supercede the TitleText class and add my own call back when values are edited
class callsign(npyscreen.TitleText):

      def when_value_edited(self):
          print("callsign class")

class TestApp(npyscreen.NPSApp):

    def when_value_edited(self):
        print("Form Value Edited")
        curses.beep()

    def while_Waiting(self):
        print("waiting")

    def actionHighlighted(self, act_on_this, key_press):
        print("ActionHighlighted")
        
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F  = npyscreen.Form(name = "K3_P3")
        ms= F.add(mode, max_height=4, value = [1,], name="Mode",
                values = ["Cw","SSB","Data"], scroll_exit=True, width=30)
        ft1 = F.add(npyscreen.FixedText,value="P3 Bandwidth",editable=False)
        s = F.add(npyscreen.Slider, value=2500,step=250,lowest=1000,out_of=10000, block_color='SAFE', name = "P3")
        ft2 = F.add(npyscreen.FixedText,value="Carrier Offset (From LHS of P3)",editable=False)
        s2 = F.add(npyscreen.Slider, value=100,step=25,lowest=25,out_of=5000, block_color='IMPORTANT', name = "Bandwidth")
        ms2= F.add(npyscreen.MultiSelect, max_height=4, value = [1,],
                values = ["Option1","Option2","Option3"], scroll_exit=True, width=20)
        bn = F.add(npyscreen.MiniButton, name = "Button",)
        
        # This lets the user play with the Form.
        F.edit()
        
if __name__ == "__main__":
    App = TestApp()
    App.run()   
