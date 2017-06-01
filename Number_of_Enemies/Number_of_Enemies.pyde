# Variable for the rectangle
x = 340
y = 50
w = 165
h = 50
y2 = 130
y3 = 210
y4 = 290
y5 = 370

# The enemies left counter 
enemies_left = 0

#creating the canvas
def setup():
 size(800,500)
 background(255)
 fill(150)

# Drawing the stuff
def draw():
 background(255)
 
 # Rectangle 1
 fill(150)
 rect(x,y,w,h)
 textSize(15)
 fill(0, 150, 153)
 text("25 enemies", 360, 85)
 
 # Rectangle 2
 fill(150)
 rect(x,y2,w,h)
 textSize(15)
 fill(0, 150, 153)
 text("50 enemies", 360, 160)
 
 # Rectangle 3
 fill(150)
 rect(x,y3,w,h)
 textSize(15)
 fill(0, 150, 153)
 text("75 enemies", 360, 245)
 
 # Rectangle 4
 fill(150)
 rect(x,y4,w,h)
 textSize(15)
 fill(0, 150, 153) 
 text("100 enemies", 360, 320)
 
 # Rectangle 5
 fill(150)
 rect(x,y5,w,h)
 textSize(15)
 fill(0, 150, 153) 
 text("Endless enemies", 360, 400)

# Assingning command that will happen when the mouse is pressed
def mouseClicked():
        if(mouseX>x and mouseX <x+w and mouseY>y and mouseY <y+h):
            enemies_left = 25
            print("There are %d enemies left" % (enemies_left))
        elif(mouseX>x and mouseX <x+w and mouseY>y2 and mouseY <y2+h):
            enemies_left = 50
            print("There are %d enemies left" % (enemies_left))
        elif(mouseX>x and mouseX <x+w and mouseY>y3 and mouseY <y3+h):
           enemies_left = 75
           print("There are %d enemies left" % (enemies_left))
        elif(mouseX>x and mouseX <x+w and mouseY>y4 and mouseY <y4+h):
            enemies_left = 100
            print("There are %d enemies left" % (enemies_left))
        elif(mouseX>x and mouseX <x+w and mouseY>y5 and mouseY <y5+h):
            enemies_left = 1000000000
            print("There are %d enemies left" % (enemies_left))