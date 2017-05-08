import random
import math
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
        a = random.randrange(0,self.diff*3)
        #gets the second number for the adding based on the diff
        b = random.randrange(0,self.diff*3)
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
        a = random.randrange(0,self.diff*3)
        #gets the second number for the subbtraction based on the diff
        b = random.randrange(0,self.diff*3)
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
        a = random.randrange(0,math.ceil((self.diff/2)))
        b = random.randrange(0,math.ceil((self.diff/2)))
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
        a=random.randrange(0,self.diff*2)
        b=random.randrange(1,math.ceil(self.diff/2))
        answer=a/b
        #checks is the answer is divisable by one ia if it is not makes a new a and b till it is
        while answer%1 != 0:
            a=random.randrange(0,self.diff)
            b=random.randrange(1,math.ceil(self.diff/2))
            answer=a/b
            answer = round(answer)
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
    
       
    
    
difficulty=difficulty_setting(5)
enemy1=enemy(difficulty,[])
enemy_list=[]
enemy_list.append(enemy1)
for enemy in enemy_list:
    enemy.generator()
print(enemy1.question_list)    


