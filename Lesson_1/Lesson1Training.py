#Last modified: January 1, 2024
#This code creates a puppy training class where the puppy:
    #"observes" what sit and stand are based on ultrasonic sensor distance data
    #"trains" the observed data using supervised 1-dimensional minimum-distance-to-mean clustering
    #"predicts" whether a measured distance is "sit" or "stand" based on training
    #"reports" the averages of each cluster and the boundary/threshold value
    #"forgets" the training if prompted


### IF NOT UPLOADING THIS TO SPIKE, RUN THIS CODE BEFORE PUPPYLESSON1.PY ###


import hub, utime, distance_sensor, force_sensor, motor
from hub import port, button


class PuppyTraining:


    def __init__(self):
        # Constructor
        self.dist_sensor = port.C######## <----------- REPLACE with the hub port of your ultrasonic sensor #########
        self.f_sensor = port.D##### <-------- REPLACE with the hub port of your force sensor ##########
        self.trainingA = []# initializing blank arrays to store training data
        self.trainingB = []
        self.boundary = None# initializing training values
        self.averageA = None
        self.averageB = None




    def observation(self):
        # Observation function that stores distance values for command A (sit) and command B (stand)
        # Adds one training observation to the training data
        print("Press left or right buttons to tell puppy what command you're demonstrating")
        while True:
            if button.pressed(button.LEFT):
                # Record a command A observation- sit
                dist = distance_sensor.distance(self.dist_sensor)
                dog_command = 'A'
                print('Puppy learns that this means command A (sit)')
                utime.sleep(0.5)
                if dist != -1:# Parses out the null values
                    # Adds the observation to the recorded data
                    self.trainingA.append(dist)
                    return dist,dog_command


            elif button.pressed(button.RIGHT):
                # Record a command B observation- stand
                dist = distance_sensor.distance(self.dist_sensor)
                dog_command = 'B'
                print('Puppy learns that this means command B (stand)')
                utime.sleep(0.5)
                if dist != -1:
                    # Adds the observation to the recorded data
                    self.trainingB.append(dist)
                    return dist,dog_command


            elif force_sensor.pressed(self.f_sensor):
                # Stop training
                dist = 0
                dog_command = 'Exit'
                print('Puppy is done training for now.')
                return dist, dog_command




    def watch(self):
        # Adds multiple training observations to the training data
        # Puppy watches for commands until the force sensor is pressed
        command = ""
        print('Puppy is ready to start learning!')
        while not force_sensor.pressed(self.f_sensor) and command != "Exit":
            # repeat observations until the force sensor is pressed
            dist, command = self.observation()
        print('Training over.')




    def train(self):
        #Calculate the means and decision boundary between two labelled clusters
        sumA = 0
        sumB = 0
        # Calculate totals
        for observation in self.trainingA:
            sumA += observation # Totals all A Training examples
        for observation in self.trainingB:
            sumB += observation # Totals all B Training examples
        # Calculate averages
        self.averageA = sumA/len(self.trainingA)# Finds mean of A commands
        self.averageB = sumB/len(self.trainingB)# Finds mean of B commands
        # The decision boundary is halfway between the A and B means.
        self.boundary = (self.averageA + self.averageB)/2
        return self.boundary


    def distance(self, dist, command):
        # Calculates the one dimensional distance between the current dist and given command average
        if command == 'A':
            return abs(dist - self.averageA)
        elif command == 'B':
            return abs(dist - self.averageB)
        else:
            return 1000


    def prediction(self, showresult=True):
        # Calculate the current prediction of the current dist based on the training and classifies based on the minimum-distance-to-mean
        dist = distance_sensor.distance(self.dist_sensor)
        if dist != None:
            print('dist', dist)
            if self.distance(dist, 'B') >= self.distance(dist, 'A'):
                # If the current dist is closer to A, predict it is A.
                prediction = 'A'
            elif self.distance(dist, 'B') < self.distance(dist, 'A'):
                # If the current dist is closer to B, predict it is B.
                prediction = 'B'
            else:
                pass
            if showresult: # Optionally print the prediction result.
                print('The puppy thinks that is a ' + prediction + ' command!')
            return prediction


    def report(self):
        #Prints out the current state of the model
        tablewidth = 20 # Adjust this constant to change table width
        print("The Puppy Training Report")
        print("*"*tablewidth)
        print("These are the examples of command A: \n", self.trainingA)
        print("The average is %.2f" % self.averageA)
        print("*"*tablewidth)
        print("These are the examples of command B: \n", self.trainingB)
        print("The average is %.2f" % self.averageB)
        print("*"*tablewidth)
        print('The decision boundary is: ', self.boundary)
        print("*"*tablewidth)


    def forget(self):
        # Reset the training data and the model
        self.boundary = None # Reset Decision boundary
        self.distdata = [] # Reset observation measurements
        self.commanddata = [] # Reset observation labels
        self.averageA = None # Reset average for the A training
        self.averageB = None # Reset average for the B training
        print('The puppy has forgotten the training!')


        
