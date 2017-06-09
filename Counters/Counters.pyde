enemies_destroyed = 0
enemies_left = 100
high_score = 0
def setup():
  size(1000, 1000)
  
def draw():
  background(255)
  textSize(15)
  fill(80,89,248)
  text (enemies_destroyed, 900, 20)
  
  textSize(15)
  fill(80,89,248)
  text (enemies_left, 850, 20)
  
  textSize(15)
  fill(80,89,248)
  text (high_score, 815, 20)
  
  
  
def keyPressed(): 
  global enemies_destroyed
  enemies_destroyed = enemies_destroyed + 1