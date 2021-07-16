# Last modified: July 7th '21
## EXAMPLE code that implements the PetTrainingKNN class from Lesson2Training.py
# PetTrainingKNN uses a 1-dimenional K-Nearest Neighbor algorithm for training a
# robot to detect two different lenghts of button presses corresponding to a
# "pat" and "stroke" for a puppy reacting to different pet lengths.

import hub, utime

### Uncomment the following line if you uploaded the Lesson2Training.py file to your SPIKE! ###
#import Lesson2Training.py
###########################

##### REPLACE with your own intializaion of motors- can be paired, unpaired, depends on your puppy!!!! #####
legR = hub.port.A.motor                                                                                    #
legL = hub.port.E.motor                                                                                    #
legR.mode(2)                                                                                               #
legL.mode(2)                                                                                               #
############################################################################################################

def happy():
    # Stuff to show puppy is happy

    #####  INSERT your own definition of puppy "happy"  #####
    #####                                               #####
    #####                                               #####
    #########################################################

def sleepy():
    # Stuff to show puppy is sleepy
    
    #####  INSERT your own definition of puppy "sleepy" #####
    #####                                               #####
    #####                                               #####
    #########################################################

    
# Define the number of training strokes and pats
train_num = 5

# Initialize training model
### Comment the following line if you have loaded the Lesson2Training.py file to your SPIKE! ###
training = PetTrainingKNN(train_num)
### Uncomment the following line if you have loaded the Lesson2Training.py file to your SPIKE! ###
#training = Lesson2Training.PetTrainingKNN(train_num)

# Collect train_num examples pats
training.record_examples(train_num, 'pat')

# Collect train_num examples strokes
training.record_examples(train_num, 'stroke')
training.report()

# Define the number of training examples used to predict the pet type
K = 3

# Classify pets until center button is pressed
print("Stroke or Pat")
while not hub.button.center.is_pressed():
    time = training.button_timer()
    if hub.button.center.is_pressed() or time == "END":
        # Exit when the center button is pressed
        break
    else:
        guess = training.k_nearest_neighbor_prediction(time, K)
        print('%d is classified as %s' % (time, guess))
        # Puppy is happy when patted, sleepy when stroked
        if guess == "pat":
            happy()
        elif guess == "stroke":
            sleepy()
