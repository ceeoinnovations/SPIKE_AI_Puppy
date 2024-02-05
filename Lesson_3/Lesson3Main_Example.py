# Last modified: January 1, 2024
# Example Code using using PickyEater Class from Lesson3Training.py
# PickyEater is an AI module and class for a SPIKE running micropython.
# PickyEater uses a 4-dimenional KNN algorithm for training a robot to react
# on different food based on the color sensor Red, Green, Blue, values
# and ultrasonic sensor value of distance.


import hub, utime, motor
from hub import port


### Uncomment the following line if you uploaded the Lesson3Training.py file to your SPIKE! ###
#import Lesson3Training
#############################


##### REPLACE with your own intializaion of motors- can be paired, unpaired, depends on your puppy!!!! #####
legR = port.C                                                                                #
legL = port.D                                                                                #
                                                                                        #
############################################################################################################


def happy():
    # Stuff to show puppy is happy/or any other emotion!!!


    #####INSERT your own definition of puppy "happy"#####
    #####                                            #####
    #####                                            #####
    #########################################################
    print("The puppy is happy")
def sleepy():
    # Stuff to show puppy is sleepy


    #####INSERT your own definition of puppy "sleepy" #####
    #####                                            #####
    #####                                            #####
    #########################################################
    print("The puppy is sleepy")
###### FEEL FREE TO ADD ANOTHER REACTION IF YOU WANT TO TRAIN MORE THAN 2 COLORS ######


### Uncomment the following line if you have loaded the Lesson3Training.py file to your SPIKE! ###
#training = Lesson3Training.PickyEater()
### Comment the following line if you have loaded the Lesson3Training.py file to your SPIKE! ###
training = PickyEater()


# Collect training example
# Press RIGHT button to change to the next class label (collect 50 points)
# Press LEFT button collect 50 points without changing the class label
# Press CENTER button to quit data recording
training.watch()


# Show report and wait until CENTER button is pressed before continuing
training.report()
print('Press Force Sensor to Continue')
while not force_sensor.pressed(training.forcesensor):
    utime.sleep(0.1)
while force_sensor.pressed(training.forcesensor):
    utime.sleep(0.1)


# Define the number of nearby training examples used to predict the food type
K = 5


# Classify food when UP is pressed until CENTER button is pressed
print("Feed the puppy! Press RIGHT button to have the puppy look at the food.")


while not force_sensor.pressed(training.forcesensor):
    if button.pressed(button.RIGHT):
        guess = training.prediction(K, True)
        # Puppy is happy when it sees Color 1, sleepy when it sees Color 0
        if guess == 1:
            happy()
        elif guess == 2:
            sleepy()


        ###### IF YOU HAVE MORE THAN 2 COLORS ADD SOMETHING HERE ######


        utime.sleep(0.2)
    else:
        utime.sleep(0.05)
