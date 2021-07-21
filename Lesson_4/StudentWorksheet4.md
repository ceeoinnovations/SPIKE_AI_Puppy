## AI Lesson 4: Fetch! ##

Uh oh! The ball you tossed for your pet landed in the tall grass and disappeared. Teach your SPIKE Puppy to predict how long it must run to fetch the ball, having only caught an initial glimpse of where it landed. 

**Design Brief:**

In this particular lesson, it is advised that students build their own “puppy” models that can roll forward and backward on wheels. Additionally, the puppy models must include the ultrasonic sensor mounted in such a way that the puppy can “see” ahead of itself and sense the distance to its target, as well as a touch sensor to substitute for another button. Feel free to reference the corresponding lesson placemat for inspiration and building tips!

Using one of two different methods, you will train your puppy to learn how quickly it can move forward. In the Linear Regression Modeling method, the puppy will prompt you via the REPL to give it a number of seconds to move, using the right and left buttons on the SPIKE hub. Once it has moved for that amount of time, record the distance (in cm) the puppy has traveled, and enter that distance into the SPIKE hub using the right and left arrows. Continue this process multiple times, teaching the puppy how far it goes for varying amounts of time. Once you have completed enough training sets, the puppy should “know” how much time it should take to move for a given target distance. 

In the Reinforcement Learning method, you will give your puppy a specific distance to move. Once the distance is received, the puppy will make a random guess for how long it should move (between 1 and 6 seconds) and will move for that amount of time. You will give the puppy feedback on whether it moved too far (right button), not enough (left button), or if it hit its target (touch sensor). The puppy learns from each new training session, and should show improvement over time. Once the puppy routinely hits its target distance on the first try, your puppy is ready for the real test! Note: you must specify beforehand how many training sessions you wish to conduct -- it is advised that you do at least four, but more is better. Once you have completed enough training sets, the puppy should “know” how much time it should take to move for a given target distance. 

Once your puppy has been properly trained, you will place an object in front of it to take a one-time reading of its distance with the ultrasonic sensor. Make sure to put a mark on the floor so that once the target is removed, its previous location is still known. Remove the object, and allow the puppy to attempt to reach the location where the target was, using its newly-learned knowledge of how fast it moves. 

**Think about these questions:**
* How does collecting data about distance traveled and time spent moving allow the puppy to learn how fast it moves?
* How will I build my puppy to be able to move forward for a given number of seconds?
* Suppose that you did not have AI or an ultrasonic sensor. What other information could you give your puppy so that it would be able to travel a given distance?

**Hints:**

* For the Linear Regression Modeling method, you must determine the number of training trials ahead of time in your code before you run it. It is advised that you use at least four trials, but more is always better. 
* During all your training sessions, make sure the puppy is moving on a uniform and level surface. If the surface changes during its movement (for example, from carpet to a hard floor) it will affect how quickly your puppy moves and will spoil your data. 

After sufficient training, your puppy should be able to move accurately to its target distance using a single reading from the ultrasonic sensor.

Work with your partner to document your initial ideas. Decide how you will evaluate these ideas to pick the best one(s) for your project. Share with another group or your teacher why you chose this solution.

Communicate the results of your group’s work by creating a presentation that demonstrates the functionality of your puppy and the code. 

Ask for feedback and conduct a self-assessment. Use the evaluation tools your teacher has provided.
