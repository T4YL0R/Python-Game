# Intializing the enemies left and enemies destroyed counter
enemies_left = 0
enemies_destroyed = 0

# setting the enemies destroyed to so so when we destory the we cand add 1 to the counter
enemies_destroyed = False

# setting all these to false because we will use buttons in the main menu to see which one is checked
twenty_five_enemies = False
fifty_enemies = False
seventy_five_enemies = False
one_hundered_enemies = False



# See which one enemies count is selected after which the counter is changed to what the user has selected
if twenty_five_enemies == True:
    enemies_left = 25
elif fifty_enemies == True:
    enemies_left = 50
elif seventy_five_enemies == True:
    enemies_left = 75
elif one_hundered_enemies == True:
    enemies_left = 100
    


# Not used now but when the enemies are destroyed add one to enemies destroyed counter
if enemeies_destroyed == True:
    enemies += 1