# Last modified: January 1, 2024
# PetTraining Supervised (K-Nearest Neighbors)
# PetTrainingSupervised is an AI module which provides PetTrainingKNN, a class for an EV3 running micropython.


import force_sensor
import hub, utime
from hub import port, button


class PetTrainingKNN:
    # PetTrainingKNN uses a 1-dimenional K-Nearest Neighbor algorithm for training
    # a robot to detect two different lengths of button presses corresponding to a
    # "pat" and "stroke" for a puppy reacting to different pet lengths


    def __init__(self, train_num):
        # Initialize the touch sensor, and timer
        # Train_num is number of training strokes and pats
        self.touch = port.F    ##### <----------- REPLACE WITH YOUR FORCE SENSOR HUB PORT ######
        self.pats = [0]*train_num
        self.strokes = [0]*train_num


    def button_timer(self):
        # Record and measure the length of the next button press
       
        #Check to see if user wishes to prematurely end training
        while not force_sensor.force(self.touch) > 0:
            utime.sleep(0.01)
            if button.pressed(button.LEFT):
                return "END"
       
        #If they press the button, measure the length in milliseconds
        time = 0
        while force_sensor.force(self.touch) > 0:
            utime.sleep(0.001)
            time += 1 #measure press in ms for more accuracy
        #print(time)
        return time


    def record_examples(self, num, ptype):
        # Record num examples and store them in the example array matching the ptype
        print('** TRAIN %ss **' % (ptype))
        if ptype == "pat":
            array = self.pats
        elif ptype == "stroke":
            array = self.strokes
        for i in range(num):
            print('%s example %ss' % (num - i, ptype))
            btime = self.button_timer()
            if btime == "END":
                break
            else:
                array[i] = btime


    def distance(self, a, b):
        # Calculate the one dimensional distance between point a and point b
        return abs(a - b)


    def k_nearest_neighbor_prediction(self, sample, k):
        # Predict the class of the provided sample using the classes of K trained cases
        distances = [(0, 0)]*(len(self.pats)+len(self.strokes))
        i = 0
        for pat_data in self.pats:
            distances[i] = (self.distance(sample, pat_data), 0)
            i += 1
        for stroke_data in self.strokes:
            distances[i] = (self.distance(sample, stroke_data), 1)
            i += 1
        distances.sort()
        sum = 0
        for i in range(k):
            sum += distances[i][1]
        if sum < (k-sum): # return 0 if mostly 0s
            return "pat"
        else:
            return "stroke"


    def report(self):
        # Create a print report of training data


        # Find pat and stroke means
        sumpats = sum(self.pats)
        sumstrokes = sum(self.strokes)
        numpats = len(self.pats)
        numstrokes = len(self.strokes)
        meanpats = round(sumpats/numpats)
        meanstrokes = round(sumstrokes/numstrokes)


        # Print pat and stroke lists and means
        print("*"*20)
        print('Pats: ' + str(self.pats))
        print('Mean of %d pats is %s' % (numpats, meanpats))
        print("*"*20)
        print('Strokes: ' + str(self.strokes))
        print('Mean of %d strokes is %s' % (numstrokes, meanstrokes))
        print("*"*20)


    def forget(self):
        # Clear training and model
        self.pats = [0]*train_num
        self.strokes = [0]*train_num
