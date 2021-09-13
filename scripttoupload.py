"""Script: Batch mint to OpenSea by DC"""
import pyautogui
import json
from time import sleep

pyautogui.PAUSE = 0.5
url = "https://opensea.io/collection/collectionnamehere/assets/create" #opensea collection create URL
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

#pyautogui.moveTo(screenWidth-1000, 60)
#pyautogui.click()
#pyautogui.moveTo(screenWidth-100, 200)
#pyautogui.click()

p = json.load(open('output.json', 'r'))
imagelocation = 'Path\\to\\image\\folder\\'
itemname = "#"
description = ""
supply = ''
numprop = 1 #number of properties

uploadbutton = None
urlbar = None
def finduploadbutton():
    print("Finding upload button")
    b = pyautogui.locateOnScreen('assets/upload.png')
    while not b:
        sleep(1)
        b = pyautogui.locateOnScreen('assets/upload.png')
    print("Using upload at " + str(b))
    return(b)

def checkifpageloaded():
    pyautogui.moveTo(screenWidth-1000, 60)
    print("Checking if page loaded")
    b = pyautogui.locateOnScreen('assets/collectionactive.png')
    while not b:
        sleep(1)
        b = pyautogui.locateOnScreen('assets/collectionactive.png')
    return True

def findURLbar():
    print("Finding url bar")
    b = pyautogui.locateOnScreen('assets/urlbar.png')
    while not b:
        sleep(1)
        b = pyautogui.locateOnScreen('assets/urlbar.png')
    print("Using url bar at " + str(b))
    return(b)


def clickItem(r):
    x = pyautogui.locateOnScreen(r)
    pyautogui.click(r)

def Tab(n=1):
    pyautogui.press('tab', n)

def Enter():
    pyautogui.press('enter')

    
def collection():
    clickItem('assets/collection.png')

def addItem():
    global urlbar
    if not urlbar:
        urlbar = findURLbar()
    pyautogui.click(urlbar)
    
    pyautogui.write(url)
    Enter()
    #clickItem('additem.png')

def upload(item):
    global uploadbutton
    checkifpageloaded()
    if not uploadbutton:
        uploadbutton = finduploadbutton()
    pyautogui.click(uploadbutton)
    url = imagelocation + str(item) + '.png' #eg. 1.png, 2.png
    print("Typing in the location of file")
    pyautogui.write(url)
    Enter()
    sleep(1)
    Tab()
    name = itemname + str(item)
    print("Writing Item name as " + name)
    pyautogui.write(name)
    Tab(3)
    print("Writing description")
    pyautogui.write(description)
    Tab()
    #y = pyautogui.locateOnScreen('collectionimg.png')
    pyautogui.click()
    print("Opening Properties")
    Tab()
    Enter()
    print("Writing type")
    pyautogui.write('Color')
    Tab()
    colorname = p[str(item)]['name']
    print("Writing Name: " + colorname)
    pyautogui.write(colorname)
    Tab(2)
    Enter()
    Tab(6+numprop)
    print("Writing Supply: " + supply)
    pyautogui.write(supply)
    Tab()
    #z = pyautogui.locateOnScreen('polygon.png') #to use specific blockchain
    #pyautogui.click(z)
    Tab(2)#this to skip blockchain selection if collection is already selected
    Enter()
    x = pyautogui.locateOnScreen('urlbar.png')
    while not x:
        sleep(1)
        x = pyautogui.locateOnScreen('urlbar.png')
    print("Created!!" + str(item))

