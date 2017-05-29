import random
import math
import time
#funtion to set the difficulty
def difficulty_setting(a):
    difficulty=a
    return difficulty 
#base enemy class
class enemy(): 
    #diif is just the difficulty and question_list is where the qestion list is saved
    def __init__(self, diff, question_list):
        self.diff = diff
        self.question_list = question_list
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
        user_answer = 0 #stand in till I get user input working
        time.sleep(1)
        if user_answer == self.answer:
            fill(44,22,199)
            text("Right", 400,200)
            enemy_up.remove(enemy_up[0])
            enemy_up.append(enemy_list[0])
            enemy_list.remove(enemy_list[0])
        else:
            fill(44,22,199)
            text("Wrong", 400,200)
            time.sleep(1)
            enemy_list.append(enemy_up[0])
            enemy_up.remove(enemy_up[0])
            enemy_up.append(enemy_list[0])
            enemy_list.remove(enemy_list[0])

    
#sets the difficulty and enemy list and makes the question        
difficulty=difficulty_setting(15)
enemy_list=[enemy(difficulty,[]),enemy(difficulty,[]),enemy(difficulty,[]),enemy(difficulty,[]),enemy(difficulty,[])]
enemy_up = []
for enemy in enemy_list:
     enemy.generator()
            
def setup():
    global f
    size(800,400)
    background(255)
    f = createFont("Arial", 30)
    enemy_up.append(enemy_list[0])
    enemy_list.remove(enemy_list[0])
def draw():
    background(255)
    for enemy in enemy_up:
        enemy.question_display()
        enemy.answer()


     
        
       
    
    

 