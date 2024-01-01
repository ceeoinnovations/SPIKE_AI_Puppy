# Last modified: January 1, 2024
# Example for Using PuppyTraining Module

## Uncomment the following line if you have loaded the code onto the SPIKE ##
#import Lesson1Training

##### REPLACE with your own intializaion of motors- can be paired, unpaired, depends on your puppy!!!! #####
legR = port.A                                                                                #
legL = port.B                                                                                #
############################################################################################################

def sit():
    print('sitting')
    ##### INSERT your own definition of puppy "sitting" #####
    #####                                            #####
    #####                                            #####
    ##### motor.run(legR, 250)
    ##### motor.run(legL, -250)
    #########################################################
    
def stand():
    print('standing')
    ##### INSERT your own definition of puppy "standing" #####
    #####                                                #####
    #####                                                #####
    ##### motor.run(legR, -250)
    ##### motor.run(legL, 250)
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
# Push the force sensor to stop the training session
# In this example, command A is for sitting,and command B is for standing
training.watch()

# Uses the recorded examples to train a decision model for puppy
training.train()
utime.sleep_ms(10)

# Print out the final results of the training make sure the puppy has it right!
training.report()
utime.sleep(0.5)

while not force_sensor.pressed(port.D):
    utime.sleep(0.1)
while force_sensor.pressed(port.D):
    utime.sleep(0.1)

# Use the trained model to have the puppy to do the commands you create!
while not force_sensor.pressed(port.D):

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

training.forget() # exit loop and forget training when force sensor is pressed
