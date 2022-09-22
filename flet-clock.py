# Flet Clock Demo App - Hololeo Labs
# imports Clock widget and displays instances
import flet
from flet import Page, Column, Row, Container, Text , UserControl, border_radius, padding
from flet import threading
import time 
from fletwidgets import Clock

def on_tick (page):
    while page.th.running is True:
        page.clock1.render()
        page.clock2.render()
        time.sleep (1)

def start_tick(page):
    page.th = threading.Thread (target=on_tick, args=[page], daemon= True)
    page.th.running = True
    page.th.start() 

def page_init (page):
    page.title = "Flet Clock"
    page.window_always_on_top = True
    page.window_width = 400 
    page.window_height = 200 
    page.vertical_alignment = "center" 
    page.horizontal_alignment = "center" 

def main(page: Page):
    page_init (page)
    # make two clocks
    page.clock1 = Clock ()
    page.clock2 = Clock ()
    page.clock2.text.color = "yellow"
    page.add (page.clock1, page.clock2 )
    # start thread to update clocks
    start_tick (page)      
    page.update()

flet.app(target=main, assets_dir="assets")
# flet.app(target=main, view=flet.WEB_BROWSER)
