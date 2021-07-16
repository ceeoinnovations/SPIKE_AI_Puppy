# Last modified: July 8th '21
# Main Code for Lesson 4: AI Fetch Examples (Linear Regression)


import hub, utime

sensor = hub.port.A.device  ### <------------ REPLACE WITH YOUR ULTRASONIC SENSOR HUB PORT

# Setup linear regression learning class, takes 2 ports for motor as parameters
# Make sure these ports match your motor ports
# Correct the directions to make your puppy move forward:
#                1 = counterclockwise, -1 = clockwise
puppy_linreg = Fetch_LinReg(direction1=1, direction2=1)


# Train the model
puppy_linreg.data_recording()

# Update the model
puppy_linreg.generate_linear_model(puppy_linreg.distances, puppy_linreg.times)


########## READ THIS ##############
# For the final trial, you can choose whether to manually 
# enter a distance for puppy to run, or you can choose to
# use the ultrasonic sensor to read a target distance. If
# you want to use a manual input distance, let the following
# line of code run. If you wish to use the ultrasonic
# sensor, comment out the following line by putting a
# in front of it.

puppy_linreg.linreg_prediction_entry()


utime.sleep(0.5)
# Run predictions and move for ultrasonic sensor readings
print('CENTER button:', 'predict', 'RIGHT button:','exit')
while True:
    utime.sleep(0.01)
    if hub.button.right.is_pressed():
        break
    elif hub.button.center.is_pressed():

        # Drive forward the sensor reading distance
        dist = sensor.get()[0]
        print("Measurement: ", dist)
        utime.sleep(2)
        time = puppy_linreg.linreg_prediction(dist)
        print("Drove ", dist, "cm in ", time, " sec")
        utime.sleep(1)
        
