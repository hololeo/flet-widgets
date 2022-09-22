# Flet Widgets - Hololeo Labs

import flet
from flet import Page, Column, Row, Container, Text , UserControl, border_radius, padding
from flet import threading
import time 

class Clock (UserControl):
  
    def __init__(self, text=''):
        super().__init__()
        self.text = Text(value=text, size = 30)
        self.text.value = self.currentTime
        self.container = Container ()
        self.container.bgcolor = "blue"
        self.container.border_radius=border_radius.all(20)
        self.container.padding = padding.only (left=20, right=20)
        self.container.content = self.text
        
    @property
    def currentTime (self):
        # http://docs.python.org/library/time.html
        s = time.strftime ('%l:%M:%S') 
        return s

    def build(self):
        return self.container

    def render (self):
        self.text.value = self.currentTime
        self.update()
    
    # page.clock1 = Clock ()
    # page.clock2 = Clock ()
    # page.clock2.text.color = "yellow"
    # page.add (page.clock1, page.clock2 )
