import pickle

# load the previous score if it exists
try:
    with open('score.dat', 'rb') as file:
        score = pickle.load(file)
except:
    score = 0

print ("High score: %d" % score)

# your game code goes here
score = 10

# save the score
with open('score.dat', 'wb') as file:
    pickle.dump(score, file)