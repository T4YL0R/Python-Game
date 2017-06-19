def setup():
    size(1500, 800)
    background(255)
    shapeMode(CENTER)
    rectMode(CENTER)


def printMenu():
    if (menu_state == 0):
        fill(150)
        rect(x-1230,y-525,175,80)#Play
        rect(x-1100,y-425,400,80)#Endless
        rect(x-1230,y-325,200,80)#Exit
        rect(x-475,y-525,250,60)#Settings
        rect(x-400,y-425,400,60)#Add
        rect(x-350,y-365,500,60)#Sub
        rect(x-400,y-305,400,60)#Div
        rect(x-300,y-245,600,60)#Mul
        rect(x-430,y-185,350,60)#Diff
        textSize(120)
        fill(0)
        text("The Math Game",x-1450,y-600)
        textSize(72)
        fill(32,175,57)
        text("Play",x-1300,y-500)
        fill(0)
        textSize(60)
        text("Endless Mode",x-1300,y-400)
        text("Exit",x-1300,y-300)
        text("Settings",x-600,y-500)
        text("Additon: " + str(ad),x-600,y-400)
        text("Subtraction: " + str(su),x-600,y-340)
        text("Divison: " + str(di),x-600,y-280)
        text("Multiplacation: " + str(mu),x-600,y-220)
        text("Difficulty: " + str(diff),x-600,y-160)
def draw():
    background(251)
    printMenu()
    
        
global menu_state
global x
global y
global ad
global su
global di
global mu 
global ad
global diff
ad = True
su = True
di = True
mu = True
diff = 0
x = 1500
y = 800
menu_state = 0


def mouseClicked():
    global menu_state
    global ad
    global su
    global di
    global mu
    global diff
    if (mouseX > 182.5 and mouseX < 357 and mouseY > 235 and mouseY < 315):
        print("Play")
        menu_state = 1
        
        
    elif (mouseX > 200 and mouseX < 400 and mouseY > 335 and mouseY < 415):
        print("Endless")
    elif (mouseX > 170 and mouseX < 370 and mouseY > 435 and mouseY < 515):
        print("Exit")
    elif (mouseX >  900 and mouseX < 1300 and mouseY > 345 and mouseY < 405):
        if (ad == True):
            ad = False
        else:
            ad = True
    elif (mouseX >  950 and mouseX < 1350 and mouseY > 405 and mouseY < 465):
        if (su == True):
            su = False
        else:
            su = True
    elif (mouseX > 850 and mouseX < 1350 and mouseY > 465 and mouseY < 525):
        if ( di == True):
            di = False
        else:
            di = True
    elif (mouseX > 900 and mouseX < 1300 and mouseY > 525 and mouseY < 585):
        if (mu == True):
            mu = False
        else:
            mu = True
    elif (mouseX > 820 and mouseX < 1220 and mouseY > 585 and mouseY < 645):
        if mouseX > 1070:
            diff += 1
        else:
            diff -= 1
        if diff < 0:
            diff = 0
        if diff > 15:
            diff = 15
