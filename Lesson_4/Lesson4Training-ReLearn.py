# Last modified: July 8th '21
# Fetch Reinforcement Learning
# Fetch Reinforcement Learning is an AI module and class for a SPIKE running micropython.


import random, hub, force_sensor, motor, distance_sensor
from random import randint
from hub import port, button


class Fetch_ReLearn():


    """This is the class for reinforcement learning.


    The idea is to train the puppy accurately move to given distance
    by first let the puppy try to reach the designated place by
    itself and then give feedback based on whether the puppy accurately
    arrives or stops too far or too close, the puppy would modify the time
    it moves based on the feedback.


    Repeat this process for several times
    and train the puppy to move to several distance, then the puppy
    would be able to accurately arrive at all given distance"""


    def __init__(self, direction1=1, direction2=1):
        # Initialize instance variables
        self.motor1 = port.A    #### REPLACE WITH YOUR SPIKE'S HUB PORTS
        self.motor2 = port.D    #### <----------------------------------
        self.touch = port.F    #### <----------------------------------


        self.speed = 200 ### Modify this to adjust puppy's speed
        self.current_feedback = None
        self.last_feedback = None
        self.reduce_coefficient = 1
        self.training_count = 0
        self.distances = [] # Training distances (training inputs)
        self.times = [] # Training times (training labels)
        self.w1 = 0 # Model Slope Coeffiecent
        self.w0 = 0 # Model Intercept
        self.motor1direction = direction1
        self.motor2direction = direction2


    def set_d_on_screen(self, dist):
        # Use right and left button on Spike to input the distance that puppy moved
        # Right -> adds distance
        # Left -> subtracts distance
        print('d='+str(dist)+'cm')
        while not force_sensor.pressed(self.touch):
            utime.sleep(0.01)
            if button.pressed(button.RIGHT):
                dist += 0.5
                print('d='+str(dist)+'cm')
                utime.sleep(0.2)
            if button.pressed(button.LEFT):
                dist -= 0.5
                print('d='+str(dist)+'cm')
                utime.sleep(0.2)
        return dist


    def puppy_move_forward(self, time):
        # Move the puppy forward a distance specified using a time determined by the trained linear model.
        # IMPORTANT: This function should be modified to match the puppy construction, using time as control parameter.
        motor.run(self.motor1, self.motor1direction * self.speed)
        motor.run(self.motor2, self.motor2direction * self.speed)
        utime.sleep(time)
        motor.stop(self.motor1)
        motor.stop(self.motor2)


    def process_feedback(self, feedback, time):
        # Modify running time based on the feedback
        self.current_feedback = feedback/self.reduce_coefficient
        if self.current_feedback * self.last_feedback > 0:
            time -= self.current_feedback
            self.last_feedback = self.current_feedback
            utime.sleep(1)
            print('t=', time)
            return time
        # If last feedback is opposite to current feedback, half the time that
        # changes each step
        if self.current_feedback * self.last_feedback < 0:
            self.reduce_coefficient = self.reduce_coefficient*2
            self.current_feedback = feedback/self.reduce_coefficient
            time -= self.current_feedback
            self.last_feedback = self.current_feedback
            utime.sleep(1)
            print('t=', time)
            return time
        return time


    def generate_linear_model(self, Input, Output):
        # Build up linear relation between time and distance
        n = len(Input)
        sumxy = 0
        sumx = 0
        sumy = 0
        sumSquarex = 0
        # Caluculate the sum of all pairs of t*d
        for a in range(len(Input)):
            sumxy += Input[a]*Output[a]
        # Calculate the sum of all d
        for i in Input:
            sumx += i
        # Calculate the sum of all t
        for j in Output:
            sumy += j
        # Calculate the sum of all d^2
        for k in Input:
            sumSquarex += pow(k, 2)
        # Formular of least squares method
        self.w1 = (n*sumxy - sumx*sumy)/(n*sumSquarex - pow(sumx, 2))
        self.w0 = (sumSquarex*sumy - sumx*sumxy)/(n*sumSquarex - pow(sumx, 2))
        print('linear model slope=', self.w1, 'intercept= ', self.w0)
        return self.w1, self.w0


    def reinforcement_learning(self):
        # Perform reinforcement learning for one distance
        distance = 0
        distance = self.set_d_on_screen(distance) # Set a target distance
        if self.training_count < 2:
            # Randomly generate initial time when training data is no more than 2
            time = random.randrange(1, 6)
            self.training_count += 1
        else:
            time = distance*self.w1+self.w0
            self.training_count += 1
        while True:
            print('Press TOUCH sensor to let the puppy give it a try')
            print('t=', time)
            while not force_sensor.pressed(self.touch):
                utime.sleep(0.01)
            self.puppy_move_forward(time) # Move forward the guessed time
            print(str(distance) + 'cm in ' + str(time) + 'sec?')
            print('TOUCH sensor: good, RIGHT button: too far,LEFT button: too short')
            while True:
                # Give feedback to the puppy with right, left and touch buttons, if
                # not accurately arrive at the target distance, the puppy would
                # modify the time it moves based on the feedback and then press
                # touch button to let it try again
                utime.sleep(0.01)
                if force_sensor.force(self.touch)>0:
                    print('Great! Went ' + str(distance) + ' cm in ' + str(time) + ' seconds')
                    utime.sleep(2)
                    print('One distance training fininshed. Start training another distance')
                    utime.sleep(2)
                    self.times.append(time)
                    self.distances.append(distance)
                    self.last_feedback = None
                    self.current_feedback = None
                    if self.training_count < 2:
                        self.reduce_coefficient = 1
                    if not self.training_count < 2:
                        self.generate_linear_model(self.distances,
                                                self.times)
                    return self.times, self.distances
                if self.last_feedback is None:
                    if button.pressed(button.RIGHT):
                        self.last_feedback = 1
                        time -= 0.5
                        print('t=', time)
                        break
                    if button.pressed(button.LEFT):
                        self.last_feedback = -1
                        time += 0.5
                        print('t=', time)
                        break
                else:
                    if button.pressed(button.RIGHT):
                        time = self.process_feedback(1, time)
                        break
                    if button.pressed(button.LEFT):
                        time = self.process_feedback(-1, time)
                        break


    def prediction(self, distance):
        # Let the puppy move to a distance measured by the ultrasonic sensor based on the training result
        time = distance*self.w1+self.w0
        self.puppy_move_forward(time)
        return time


    def prediction_entry(self):
        # Prompt user for distance entry. Use trained model to predict time to go forward and move
        print('Press TOUCH button to start prediction')
        dist = 0
        utime.sleep(0.5)
        while not force_sensor.pressed(self.touch):
            utime.sleep(0.01)
        utime.sleep(0.5)
        while not button.pressed(button.LEFT):
            dist = self.set_d_on_screen(dist)
            print('t=%.2f*d+%.2f' %(self.w1, self.w0))
            utime.sleep(0.5)
            # Calculate t with the model
            time = self.w1*dist + self.w0
            print('d='+str(dist)+'cm')
            print('t='+str(time)+'s')
            # Puppy tries moving
            self.puppy_move_forward(time)
            print('TOUCH button: try again, LEFT button: exit')
            # Press touch button to retry or press left button to exit
            while True:
                utime.sleep(0.01)
                if button.pressed(button.LEFT):
                    return time
                elif force_sensor.pressed(self.touch):
                    utime.sleep(0.5)
                    break
