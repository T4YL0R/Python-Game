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
        
class Enemy():
    def __init__(self,cpos,tpos,speed,colour1,colour2,colour3,question):
        self.x = cpos.x
        self.y = cpos.y
        self.tx = tpos.x
        self.ty = tpos.y
        self.speed = speed
        self.listc = [colour1,colour2,colour3]
        self.q = question
        if (speed < 1):
            self.type = str(speed) + "fast"
        else:
            self.type = normal
        
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
        if (ed == 0):
            if ("fast" in typ):
                speed = int(typ[0])
            else:
                speed = 1
        else:
            speed = 0
'''
def menus():
    def __init__(self,x,y,state):
        self.x = x
        self.y = y
        self.state = "None"
    def mainMenu(self):
        #Title:
        #text()
        rect((self.x,self.y + 200,200,100)
        rect((self.x,self.y + 200,200,100)
        text(
             '''
        
        
            
def setup():
    size(1500, 800)
    background(255)
    rectMode(CENTER)
    ellipseMode(CENTER)
    
def draw():
    background(255)
    fill(170)
    rect(750,400,1500,400)
    player.place()
    for i in range(len(enemy_list)):
        enemy_list[i].move()
        enemy_list[i].placeEnemy()
    
setup
player = Player(750,400,3)
start_point = Point(1,400)
end_point = Point(1000,400)
enemy_list = [Enemy(start_point,end_point,1,0,250,12,"Hey"),Enemy(start_point,end_point,2,0,12,250,"Hey")]