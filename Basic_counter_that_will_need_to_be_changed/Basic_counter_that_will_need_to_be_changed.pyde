# x = 1
# speed = 1
# y = 1

# def setup():
#     size(1500, 1500)
#     background(255)
    
# def draw():
#     global x
#     global y
#     background(255)
#     fill(255)
#     rect(x,100,50,25)
#     fill(0)
#     x = x + 1
#     while y != 100:
#         if y % 5 == 0:
#             rect(10,100,50,25)
#             fill(0)
#         y = 1 + 1
            
      
# def draw():
#   background(204)
#   s = second()
#   m = minute()
#   h = hour()
#   line(s, 0, s, 33)
#   line(m, 33, m, 66)
#   line(h, 66, h, 100)




# time = "000"
# initialTime = 0
# interval = 1000
# bg = color (255)
 
 
 
# def setup():
#   size(300, 300)
#   font = createFont("Ariel", 30)
#   background(255)
#   fill(0)
#   initialTime = millis()
#   frameRate(30)
 
 
# def draw():
#   global bg
#   global initialTime
#   global time
#   background(bg)
#   if (millis() - initialTime > interval):
#     time = nf(int(millis()/1000), 3)
#     initialTime = millis()
#     bg = color (random(255), random(100), random(255))
  
 
#   text(time, width/2, height/2)
 

# stuff = []
# i = second()

# def setup():
#   size(300, 300)
#   background(255)
  
  
  
# def draw():
#     global i
#     background(255)
#     fill(255)
#     if i == 1:
#          i = 0
#          rect(x, 23, 200, 200)
#          fill (0)
        
        
# print(i)


# class Enemy():
#     def __init__(self,xPos, yPos, l, h, speed):
#         self.x = xPos
#         self.y = yPos
#         self.l = l
#         self.h = h
#         self.speed = speed
    
#     def display(self):
#         fill(255)
#         rect(self.x, self.y, self.l, self.h)
        
#     def drive(self):
#         self.x += self.speed
        
# enemies = Enemy(1, 50, 50, 50, 5)
# enemies_list = [enemies] * 25
# x = 0
# i = 0
# time = "010"
# t = 0
# interval = 10

# def setup():

#   size(300, 300)
#   font = createFont("Arial", 30)
#   background(255)
#   fill(0)


# def draw():
#     global interval
#     global x
#     global i
#     global enemies_list
#     background(255)
#     x = x + 1
#     t = interval-int(millis()/1000)
#     time = nf(t , 2)
#     if(t % 5 == 0):
#         i = i + 1
#         enemies_list[i]
#         enemies.display()
#     interval+=1

  
def draw(): 
   m = millis()
   noStroke()
   fill(m % 255)
   rect(25, 25, 50, 50)