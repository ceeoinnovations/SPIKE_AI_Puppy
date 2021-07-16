# Last modified: July 8th '21

# PickyEater is an AI module and class for a SPIKE running micropython.

from math import exp

class PickyEater:
    # PickyEater uses a 3-dimenional KNN algorithm for training a robot to react on
    # different food based on the color sensor Red, Green, and Blue values.
    
    def __init__(self):
        # Initialize the PickeyEater class provides a port for the color sensor.
        self.colorsensor = hub.port.B.device
        self.colorsensor.mode(5) # Set color sensor to mode 5 to get [R, G, B, ?] values
                                    # ranging from 0->1024
        self.training = []   # List of (R,G,B.distance) for training examples
        self.labels = []     # List of labels for training examples
        self.colorcount = 0  # Max Number of Colors Trained
        
    
    def watch(self):
        # Take data for each kind of color and normalize the data
        samplecount = 0
        self.colorcount = 0
        print('Data for Color #%s' % (self.colorcount))
        while True:
            # Record training data examples
            if samplecount % 50 == 0:
                print('*'*20)
                print('Press CENTER to quit training')
                print('Press LEFT to take more data for the current color')
                print('Press RIGHT to train another color')
                print('*'*20)
                while True:
                    if hub.button.center.is_pressed():
                        # Press CENTER button to quit data recording
                        print('Finished data recording for %s Colors' %
                              (self.colorcount + 1))
                        break
                    if hub.button.right.is_pressed():
                        # Press RIGHT button to change to the next class label
                        # then collect 50 points
                        self.colorcount += 1
                        print('Recording Data for Color #%s' %
                              (self.colorcount))
                        break
                    if hub.button.left.is_pressed():
                        # Press LEFT button to collect 5 seconds of data
                        # without changing the class label
                        print('Recording Additional Data for Color #%s' %
                              (self.colorcount))
                        break
            if hub.button.center.is_pressed():
                break

            samplecount += 1
            if samplecount % 5 == 0:
                # Print progress bar
                print("[]", end=" ")

            # Convert the color sensor data to a list
            self.colors = []
            self.colors.append(self.colorsensor.get()[0])  # R values
            self.colors.append(self.colorsensor.get()[1])  # G values
            self.colors.append(self.colorsensor.get()[2])  # B values 
            
            sensordata = (list(self.colors))
            # Sensor data stored in self.training
            # the correlated class names stored in self.labels
            self.training.append(sensordata)
            self.labels.append(self.colorcount)
            utime.sleep(0.1)
        return self.training, self.labels

    def distance(self, sample, point):
        #Calculate the distance between two N-dimensional points
        d = 0
        for i in range(len(sample)):
            d += pow(sample[i] - point[i], 2)
        return pow(d, 0.5)

    def find_k_nearest_class(self, sample=[], k=5):
        # Predict the class of the sample using N-dimentional KNN
        # Intialize lists
        nearest_neighbors = [0]*k
        distance_list = [(0, 0)] * len(self.training)
        # Calculate distance between sample and each self.training data point
        for i in range(len(self.training)):
            # Build a list of (distance, label) tuples
            distance_list[i] = (self.distance(sample, self.training[i]),
                                self.labels[i])
        # Sort the list based on distances
        distance_list.sort(key=lambda point: point[0])
        # Find the class labels corresponded to the k smallest distances
        nearest_neighbors = distance_list[:k]
        nearest_labels = [point[1] for point in nearest_neighbors]
        # Find mode (most common) of k-nearest labels
        guess = max(nearest_labels, key=nearest_labels.count)
        return guess

    def prediction(self, k, printresult=False):
        # Let the puppy recognize what food it is
        # Read current color sensor and set that as sample data
        self.colors = []
        self.colors.append(self.colorsensor.get()[0])
        self.colors.append(self.colorsensor.get()[1])
        self.colors.append(self.colorsensor.get()[2])
        sampledata = (list(self.colors))
        sampledata = sampledata
        print('The puppy tries to recognize the color')
        # The puppy does the recognition with KNN algorithm #
        guess = self.find_k_nearest_class(sampledata, k)
        if printresult:
            print('The puppy thinks the food is', guess)
        return guess

    def report(self):
        print("*"*20)
        for c in range(0, max(self.labels)):
            total = self.labels.count(c+1)
            print("Color #%s" % (c+1))
            print("Number of samples: %s" % (total))

            # Create a list of all samples for a color c
            clist = [self.training[i]
                     for i in range(len(self.labels))
                     if self.labels[i] == c+1]
            # Report the average value for (R,G,B,Dimension) of color c
            averages = [sum(i)/total for i in zip(*clist)]
            print("Averages")
            print("Red: %s, Green: %s, Blue: %s, " %
                  (averages[0], averages[1], averages[2]))
            print("*"*20)

    def forget(self):
        # Puppy forgets training
        self.training = []
        self.labels = []
        self.colorcount = 0
        
