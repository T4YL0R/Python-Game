# Variable for the rectangle
x = 340
y = 50
w = 165
h = 80
y2 = 150
y3 = 250
y4 = 350

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
 text("Addition Only", 360, 95)
 
 # Rectangle 2
 fill(150)
 rect(x,y2,w,h)
 textSize(15)
 fill(0, 150, 153)
 text("Subtraction Only", 360, 200)
 
 # Rectangle 3
 fill(150)
 rect(x,y3,w,h)
 textSize(15)
 fill(0, 150, 153)
 text("Multiplication Only", 360, 300)
 
 # Rectangle 4
 fill(150)
 rect(x,y4,w,h)
 textSize(15)
 fill(0, 150, 153) 
 text("Division Only", 360, 400)

# Assingning command that will happen when the mouse is pressed
def mouseClicked():
        if(mouseX>x and mouseX <x+w and mouseY>y and mouseY <y+h):
            println("The mouse is pressed")
            #Nikki Put Question generator here
        elif(mouseX>x and mouseX <x+w and mouseY>y2 and mouseY <y2+h):
            println("The mouse is pressed")
            #Nikki Put Question generator here
        elif(mouseX>x and mouseX <x+w and mouseY>y3 and mouseY <y3+h):
            println("The mouse is pressed")
            #Nikki Put Question generator here
        elif(mouseX>x and mouseX <x+w and mouseY>y4 and mouseY <y4+h):
            println("The mouse is pressed")
            #Nikki Put Question generator here
            # Sorry for repeating the same thing