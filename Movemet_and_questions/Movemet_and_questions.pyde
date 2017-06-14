import random
import math
import time
from timeit import default_timer as timer
#funtion to set the difficulty
def difficulty_setting(a):
    difficulty=a
    return difficulty 
#base enemy class
class Enemy(): 
    #diif is just the difficulty and question_list is where the qestion list is saved
    def __init__(self, diff, question_list, cpos, tpos, speed, colour1, colour2, colour3, right):
        self.diff = diff 
        self.question_list = question_list
        self.x = cpos.x
        self.y = cpos.y
        self.tx = tpos.x
        self.ty = tpos.y
        self.speed = speed
        self.listc = [colour1,colour2,colour3]
        self.right = 0
        if (speed < 1):
            self.type = str(speed) + "fast"
        else:
            self.type = normal
    #generates the addding questions and returns them in a list that looks like [a, b, answer, "+"]   
    def Adding(self):
        #gets the first number for the adding based on the diff
        a = random.randrange(0,self.diff*2)
        #gets the second number for the adding based on the diff
        b = random.randrange(1,self.diff*2)
        #gets the answer for the question
        answer = a+b
        #saves all the parts of the question on the list they have to be in the order
        self.question_list.append(a)
        self.question_list.append(b)
        self.question_list.append(answer)
        self.question_list.append("+")
        return self.question_list
    #generates the subbtraction questions and returns them in a list that looks like [a, b, answer, "-"]
    def subbtraction(self):
        #gets the first number for the subbtraction based on the diff
        a = random.randrange(1,self.diff*2)
        #gets the second number for the subbtraction based on the diff
        b = random.randrange(1,self.diff*2)
        #gets the first answer
        answer = a-b
        #check to make sure the answer is postitve than makes the list
        if answer < 0:
            answer = b-a
            self.question_list.append(b)
            self.question_list.append(a)
            self.question_list.append(answer)
            self.question_list.append("-")
        
        else:
        
            self.question_list.append(a)
            self.question_list.append(b)
            self.question_list.append(answer)   
            self.question_list.append("-")
            return self.question_list
    #makes the multiplication questions returns a list [a, b, answer, "x"]
    def multiplication(self):
        #gets a and b for the question based on the diff
        a = random.randrange(1,math.ceil((self.diff/2)))
        
        b = random.randrange(1,math.ceil((self.diff/2)))
        
        #gets the answer
        answer = a*b
        #makes the list
        self.question_list.append(a)
        self.question_list.append(b)
        self.question_list.append(answer)
        self.question_list.append("x")
        return self.question_list
    #makes the division question returns a list [a, b, answer, "/"]
    def division(self):
        #gets a and b and answer for the first time set up so a is more likely to be bigger than b
        a=random.randrange(0,(self.diff*2))
        thing = (math.ceil(self.diff/2))
        b=random.randrange(2,thing)
        answer = float(a)/float(b)
        #checks is the answer is divisable by one ia if it is not makes a new a and b till it is
        while float(answer%1) != 0:
            a=int(random.randrange(0,(math.ceil(self.diff))))
            b=int(random.randrange (2,(math.ceil(self.diff/2))))
            answer=float(a)/float(b)
        #makes the list for the question
        self.question_list.append(a)
        self.question_list.append(b)
        self.question_list.append(answer)
        self.question_list.append("/")
        return self.question_list
    #picks a radom number and based on the number makes a certan type of question          
    def generator(self):
        question_type = random.randrange(1,11)
        if question_type == 1:
            enemy.Adding()
        elif question_type == 2:
            enemy.Adding()
        elif question_type == 3:
            enemy.Adding()
        elif question_type == 4:
            enemy.subbtraction()
        elif question_type == 5:
            enemy.subbtraction()
        elif question_type == 6:
            enemy.subbtraction()
        elif question_type == 7:
            enemy.multiplication()
        elif question_type == 8:
            enemy.multiplication()
        elif question_type == 9:
            enemy.division()
        elif question_type == 10:
            enemy.division()
    def question_check(self):
        if self.qestion_list == []:
            enemy.generator() 
    #displays the question in the middle of the screen for now
    def question_display(self):
        global f
        textFont(f,30)
        fill(44,22,199)
        text(str(self.question_list[0]) + " " + str(self.question_list[3]) + " " + str(self.question_list[1]) + " " + "= ", 350, 100)
    def answer(self):
        global user_answer
        global userinput
        real_answer = float(self.question_list[2])
        real_answer = int(real_answer)
        try:
            int(userinput)
            userinput = float(userinput)
        except ValueError:
            text("next time enter a letter", 400,500)
            time.sleep(1)
        if userinput == real_answer:
            fill(44,22,199)
            text("Right", 400,500)
            print("right")  
            self.right = 1
            time.sleep(1)          
            enemy_up.remove(enemy_up[0])
                   
        else:
            fill(44,22,199)
            text("Wrong", 400,500)
            print("wrong")
            time.sleep(1)
            enemy_up.remove(enemy_up[0])
    def placeEnemy(self):
        fill(0)
        ellipse(self.x,self.y,35,35)
        fill(self.listc[0],self.listc[1],self.listc[2])
        ellipse(self.x,self.y,30,30)
        
    def move(self):
        
        atX = False
        atY = False
        moveX = self.tx-self.x
        print(str(self.tx) + "-" + str(self.x) + "=" +str(moveX))
        moveY = self.ty-self.y
        print(str(self.ty) + "-" + str(self.y) + "=" +str(moveX))
        print(str(moveX))
        if(moveY == 0):
            shiftX = 1
            shiftY = 0
        elif(moveX == 0):
            shiftY = 1
            shiftX = 0
        else:
            shiftY = moveY/moveX
            print("Before: " + str(self.x))
        self.x = self.x + (shiftX*self.speed)
        print(str(self.x))
        self.y = self.y + (shiftY*self.speed)
        if (self.x > self.tx):
            self.x = self.tx
            atX= True
        if (self.y > self.ty):
            self.y = self.ty
            atY= True
            
    def nextPoint(self,pointsList,player):
        for i in range(len(pointsList)):
            if ( i + 1 == len(pointsList)):
                    player.health = player.health - 1
            if (pointsList[i].x == self.x)and(pointsList[i].y == self.y):
                self.tx = (pointsList[i + 1].x)
                self.ty = (pointsList[i + 1].y)
    
    def pause(self):
        if (self.speed == 0):
            if ("fast" in typ):
                self.speed = int(typ[0])
            else:
                self.speed = 1
        else:
            self.speed = 0

        
        
        
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        print (self.x)
        print (self.y)
    def drawMe(self):
        fill(0)
        ellipse(self.x,self.y,4,4)
class Player():
    def __init__(self,xl,yl,hpl):
        self.x = xl
        self.y = yl
        hp = hpl
    def place(self):
        fill(0)
        ellipse(self.x,self.y,60,60)
        fill(18,255,233)
        ellipse(self.x,self.y,50,50)
        fill(164)
        triangle(self.x,self.y-30,self.x-25,self.y+15,self.x+25,self.y+15)
    
#sets the difficulty and enemy list and makes the question  
player = Player(750,400,3)
start_point = Point(1,400)
end_point = Point(1000,400)     
difficulty=difficulty_setting(15)

enemy_list=[Enemy(difficulty,[],start_point,end_point,2,0,12,250,0)]
enemy_up = []
userinput = ''
real_time = time()
user_answer = 0
goal_time = 0
start_time = 0

            
def setup():
    global f
    size(1500, 800)
    background(255)
    f = createFont("Arial", 30)

    rectMode(CENTER)
    ellipseMode(CENTER)
def draw():
    global goal_time
    global start_time
    global enemy
    background(255)
    real_time = timer()
    textFont(f,30)
    text(userinput, 400,400)
    #this is causeing the error
    if start_time+2 <= real_time:
        enemy_list.append(Enemy(difficulty,[],start_point,end_point,2,0,12,250,0))
        start_time = timer()
    for enemy in enemy_up:
        enemy.question_display()
        if real_time >= goal_time:        
            enemy.answer()
            unerinput = ""
            time.sleep(1)
            for enemy in enemy_list:
                enemy.pause()
    for enemy in enemy_list:
        if enemy.right == 1:
            enemy_list.remove(enemy)
    for enemy in enemy_list:
        if enemy.question_list == []:
            enemy.generator()
    fill(170)
    rect(750,400,1500,400)
    player.place()
    for i in range(len(enemy_list)):
        enemy_list[i].move()
        enemy_list[i].placeEnemy()


def keyPressed():

  global userinput
  global value
  global user_answer
  if key == "c":
    userinput = ''
  else:
    userinput = userinput + key
    print (userinput)

def mouseClicked():
    global goal_time
    for enemy in enemy_list:
        if mouseX >= enemy.x-17.5 and mouseX <= enemy.x+17.5 and mouseY >= enemy.y-17.5 and mouseY <= enemy.y+17.5:
            enemy_up.append(enemy)
            goal_time = (timer()+10)
            enemy.pause()
            
    
     
        
       
    
    

 