mainurl = "https://opensea.io/collection/bringbacktheegg?collectionSlug=bringbacktheegg&search[sortAscending]=false&search[sortBy]=CREATED_DATE"
import pyautogui
from time import sleep
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.PAUSE = 0.5

sellbtn = None

def findsellbutton():
    s = pyautogui.locateOnScreen('sellbutton.png')
    while not s:
        sleep(1)
        s = pyautogui.locateOnScreen('sellbutton.png')
    print("sell button found at " + str(s))
    return s

def refresh():
    pyautogui.moveTo(screenWidth-1600, 500)
    pyautogui.click()
    pyautogui.press('f5')
    sleep(2)

def selLeft():
    pyautogui.moveTo(screenWidth-1600, 500)
def selRight():
    pyautogui.moveTo(screenWidth-1300, 500)

def addprop():
    pyautogui.moveTo(screenWidth-1500, 500)
    pyautogui.click()

def findURLbar():
    print("Finding url bar")
    b = pyautogui.locateOnScreen('urlbar.png')
    while not b:
        sleep(1)
        b = pyautogui.locateOnScreen('urlbar.png')
    print("Using url bar at " + str(b))
    return(b)


def clickItem(r):
    x = pyautogui.locateOnScreen(r)
    pyautogui.click(r)

def Tab(n=1):
    pyautogui.press('tab', n)

def Enter():
    pyautogui.press('enter')

def mainTab():
    pyautogui.click(button='middle')
    pyautogui.hotkey('ctrl', 'tab')

def closeTab():
    pyautogui.moveTo(screenWidth-1600, 500)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'w')

def scroll():
    pyautogui.moveTo(screenWidth-1500, 600)
    sleep(5)
    pyautogui.scroll(-600)

def sellItem():
    global sellbtn
    #if not sellbtn:
    #    sellbtn = findsellbutton()
    sleep(4)
    pyautogui.moveTo(screenWidth-1100, 970)
    pyautogui.click()
    sleep(2)
    pyautogui.moveTo(screenWidth-1500, 400)
    pyautogui.click()
    pyautogui.press('backspace')
    pyautogui.write('3')
    Tab()
    pyautogui.write('0.001')
    Tab(21)
    Enter()
        #CompleteListing
    sleep(3)
    Tab(2)
    Enter()
    sleep(3.5)
    Tab(2)
    Enter()

def run(n):
    for i in range(n):
            refresh()
            sellItem()
            closeTab()
            
  
    
##def addprop():
##    pyautogui.moveTo(screenWidth-1500, 500)
##    pyautogui.click()
##    
##    print("Opening Properties")
##    Tab()
##    Enter()
##    Tab(2)
##    Enter()
##    Tab(5)
##    print("Writing Type")
##    pyautogui.write('Egg')
##    Tab()
##    print("Writing Name")
##    pyautogui.write("Yes")
##    Tab(2)
##    Enter()
##    Tab()
##    #z = pyautogui.locateOnScreen('polygon.png')
##    #pyautogui.click(z)
##    Tab(2)#this to skip blockchain selection
##    Enter()

