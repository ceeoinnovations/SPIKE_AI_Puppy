# Last modified: July 8th, '21

# Fetch Linear Regression
# Lesson4Training.py is an AI module and Fetch LinReg() is a class for an SPIKE running micropython.

class Fetch_LinReg():
    
    def __init__(self, direction1=1, direction2=1):

        # Initialize instance variables
        
        self.motor1 = hub.port.C.motor   ### <------ REPLACE WITH YOUR SPIKE HUB PORTS!!!!! ###
        self.motor2 = hub.port.D.motor   ### <------------------- #############################
        
        self.distances = [] # Training distances (training inputs)
        self.times = []     # Training times (training labels)
        self.slope = 0      # Model Slope Coeffiecent
        self.intercept = 0  # Model Intercept
        self.motor1direction = direction1
        self.motor2direction = direction2
        
    def puppy_move_forward(self, time):
        # Move the puppy forward a distance specified using a time determined by the trained linear model.
        # IMPORTANT: This function should be modified to match the puppy construction, using time as control parameter.
        self.motor1.pwm(self.motor1direction*50)
        self.motor2.pwm(self.motor2direction*50)
        utime.sleep(time)
        self.motor1.pwm(0)
        self.motor2.pwm(0)
        
    def set_t_on_screen(self, time):
        # Use right and left button on Spike to set running time
        # Right -> add time
        # Left -> subtract time 
        print('t='+str(time)+'s')
        while not hub.button.center.is_pressed():
            utime.sleep(0.01)
            if hub.button.right.is_pressed():
                time += 0.25
                print('t='+str(time)+'s')
                utime.sleep(0.2)
            if hub.button.left.is_pressed():
                time -= 0.25
                print('t='+str(time)+'s')
                utime.sleep(0.2)
        return time
    
    def set_d_on_screen(self, dist):
        # Use right and left button on Spike to input the distance that puppy moved
        # Right -> add distance
        # Left -> subtract distance
        print('d='+str(dist)+'cm')
        while not hub.button.center.is_pressed():
            utime.sleep(0.01)
            if hub.button.right.is_pressed():
                dist += 0.5
                print('d='+str(dist)+'cm')
                utime.sleep(0.2)
            if hub.button.left.is_pressed():
                dist -= 0.5
                print('d='+str(dist)+'cm')
                utime.sleep(0.2)
        return dist
    
    def data_recording(self):
        # Record pairs of time and distance that puppy moves for training a model later
        print('Start data recording')
        while True:
            time = 0
            print('t='+str(time)+'s')
            # Set t by pressing right and left buttons
            time = self.set_t_on_screen(time)
            self.times.append(time)
            utime.sleep(1)
            # Puppy moves in a constant speed by t seconds
            self.puppy_move_forward(time)
            # User records the distance puppy moved with up and down buttons.
            dist = 0
            dist = self.set_d_on_screen(dist)
            self.distances.append(dist)
            utime.sleep(0.3)
            print('Press CENTER button to continue')
            # After take a pair of t and d, press center button to continue or
            # press left button to exit data recording
            while True:
                utime.sleep(0.01)
                if hub.button.center.is_pressed():
                    print('Press RIGHT to record more, or LEFT to exit data recording')
                    utime.sleep(0.1)
                    while True:
                        if hub.button.right.is_pressed():
                            break
                        elif hub.button.left.is_pressed():
                            return self.distances, self.times
                        utime.sleep(0.01)
                    break
                
    def generate_linear_model(self, Input, Output):
        # Linear regression with least squares method
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
        # Formula of least squares method
        self.slope = (n*sumxy - sumx*sumy)/(n*sumSquarex - pow(sumx, 2))
        self.intercept = (sumSquarex*sumy - sumx*sumxy)/(n*sumSquarex - pow(sumx, 2))
        print("SLOPE: ", self.slope, " INTERCEPT: ", self.intercept)
        return self.slope, self.intercept
    
    def linreg_prediction(self, dist):
        # Use trained model to do predict time to go forward and move
        time = self.slope*dist + self.intercept # Calculate t with the model
        print('d='+str(dist)+'cm')
        print('t='+str(time)+'s')
        self.puppy_move_forward(time)
        return time
    
    def linreg_prediction_entry(self):
        # Prompt user for distance entry. Use trained model to do predict time to go forward and move
        print('Press CENTER button to start prediction')
        dist = 0
        utime.sleep(0.5)
        while not hub.button.center.is_pressed():
            utime.sleep(0.01)
        utime.sleep(0.5)
        while not hub.button.left.is_pressed():
            dist = self.set_d_on_screen(dist)
            print('t=%.2f*d+%.2f' %(self.slope, self.intercept))
            utime.sleep(0.5)
            # Calculate t with the model
            time = self.slope*dist + self.intercept
            print('d='+str(dist)+'cm')
            print('t='+str(time)+'s')
            # Puppy start moving
            self.puppy_move_forward(time)
            print('CENTER button to try again, LEFT button to exit')
            # Press center button to retry or press left button to exit
            while True:
                utime.sleep(0.01)
                if hub.button.left.is_pressed():
                    return time
                elif hub.button.center.is_pressed():
                    utime.sleep(0.5)
                    break
                    
