class Menu():
    def __init__(self,x,y):
        self.x = x/2
        self.y = y/2
        self.statelist = ["main","pause","none"]
        self.state = 2
    def switchState(self,input):
        for i in range(len(self.statelist)):
            if (input == self.statelist[i]):
                 self.state = i
    def draw_menu(self):
        if (self.state = 1):
            text("The Math Game",self.x,self.y/2)
            rect(self.x,self.y/2+20,40,20)
            rect(self.x,self.y/2+40,40,20)
        elif (self.state = 2):
            text("Game Paused",self.x,self.y/2)
            text("Resume",self.x,self.y/2+20,40,20)
            rect(self.x,self.y/2+20,40,20)
            rect(self.x,self.y/2+40,40,20)
            
            
            
def setup():
    rectMode
    #Seting up the 
    size(800, 400)
    background(255)
    
                