# Flet Clock Widget - Hololeo Labs
import flet
from flet import Page, Text 
from flet import threading
import time

def getTime ():
    #s = time.ctime() # 'Mon Oct 18 13:35:29 2010'
    s = time.strftime ('%l:%M:%S') 
    return s

def on_tick (page):
    while page.th.running is True:
        page.clock.value = getTime()
        page.update()
        time.sleep (1)
def main(page: Page):
    page.title = "Flet Clock"
    page.window_always_on_top = True
    page.window_width = 400 
    page.window_height = 200 
    page.vertical_alignment = "center" 
    page.horizontal_alignment = "center"  
    # display clock ui
    page.clock = Text ("", size=40)
    page.clock.value = getTime()
    page.add (page.clock)
    # start clock thread
    page.th = threading.Thread (target=on_tick, args=[page], daemon= True)
    page.th.running = True
    page.th.start()    
    page.update()

flet.app(target=main, assets_dir="assets")
# flet.app(target=main, view=flet.WEB_BROWSER)
