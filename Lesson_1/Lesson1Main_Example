# Last modified: July 7th '21
# Example for Using PuppyTraining Module

import hub, utime

## Uncomment the following line if you have loaded the code onto the SPIKE ##
#import Lesson1Training

##### REPLACE with your own intializaion of motors- can be paired, unpaired, depends on your puppy!!!! #####
legR = hub.port.A.motor                                                                                    #
legL = hub.port.E.motor                                                                                    #
legR.mode(2)                                                                                               #
legL.mode(2)                                                                                               #
############################################################################################################

def sit():
    print('sitting')
    ##### INSERT your own definition of puppy "sitting" #####
    #####                                               #####
    #####                                               #####
    #########################################################
def stand():
    print('standing')
    ##### INSERT your own definition of puppy "standing" #####
    #####                                                #####
    #####                                                #####
    ##########################################################
   
# Puppy starts standing 
state = "standing"

## Uncomment the following line if you have loaded the code onto the SPIKE##
#training = Lesson1Training.PuppyTraining()

# Calls the PuppyTraining Class
## Comment the following line if you have loaded the code onto the SPIKE##
training = PuppyTraining()

# Start a training session with the puppy
# Push the "left" button to record an example of command A
# Push the "right" button to record an example of command B
# Push the "center" button to stop the training session
# In this example, command A is for sitting,and command B is for standing
training.watch()

# Uses the recorded examples to train a decision model for puppy
training.train()
utime.sleep_ms(10)

# Print out the final results of the training make sure the puppy has it right!
training.report()
utime.sleep(0.5)

while not hub.button.center.is_pressed():
    utime.sleep(0.1)
while hub.button.center.is_pressed():
    utime.sleep(0.1)
    
# Use the trained model to have the puppy to do the commands you create!
while not hub.button.center.is_pressed():

    command = training.prediction()
    if command == 'A' and state == "standing":
        # Puppy should sit
        state = "sitting"
        sit()
        utime.sleep(0.1)
    elif command == 'B' and state == "sitting":
        # Puppy should stand
        state = "standing"
        stand()
        utime.sleep(0.1)
    else:
        utime.sleep(0.1)

training.forget() # exit loop and forget training when center button is pressed

