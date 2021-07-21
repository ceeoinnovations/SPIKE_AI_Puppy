# Student Worksheet Guide #
*Attention Educators: This document is meant as a guide to aid you in creating your own student-facing content*

## AI Lesson 1: Sit ##

It’s time for basic obedience training! Teach your SPIKE Puppy to recognize the commands for “sit” and “stand”.

**Design Brief:**

You may choose to design and build your own robotic pet using your SPIKE kit, and feel free to reference the first placemat for inspiration! Make sure that whatever you build has the ability to sit down and stand up again, and has the ultrasonic sensor attached near the head of the puppy. The ultrasonic sensor will detect how far away your hand is: having a hand close to the puppy’s head will be the command for ‘sit’, and having a hand far away from the puppy’s head will be the command for ‘stand’. 

**Think about these questions:**
* You could have a training set of just two data points-one example of the “sit” ultrasonic distance and one example of the “stand” ultrasonic distance. What is the advantage of using multiple data points for training instead of just two?
* Should your various distance positions for controlling your puppy be very close together or very far apart from each other? Explain why.

**Hints:**

* The ultrasonic sensors tend to pick up “Null” values, meaning that they cannot register an object in front of them. What can you include in your code that either parses out these null values or categorizes them along with the “sit” or “stand” values?
* Is the puppy not responding as intended? Debug by printing sensor values to the REPL to make sure the values you are getting are realistic. 
* Just like you, the puppy learns with practice! The more training sets you do, the more accurate your results should be. 

Your design should be able to successfully assign specific puppy actions to different hand distance positions. When your hand moves a certain distance away from the ultrasonic sensor/puppy head, the puppy will react accordingly. You may choose to have your puppy sit and stand alternatively, or you may choose other actions for your puppy to execute.

Work with your partner to document your initial ideas. Decide how you will evaluate these ideas to pick the best one(s) for your project. Share with another group or your teacher why you chose this solution.

Communicate the results of your group’s work by creating a presentation that demonstrates the functionality of your puppy and the code. 

Ask for feedback and conduct a self-assessment. Use the evaluation tools your teacher has provided.

## AI Lesson 2: Pet the Puppy ##

Show your pet some love. Teach your SPIKE Puppy to notice the difference between exciting short pets and calming long strokes on its back.

**Design Brief:**

You may choose to design and build your own robotic pet using your SPIKE kit, and feel free to reference the placemat for inspiration! Make sure that your puppy is able to register long and short presses of the touch sensor. It must also be able to exhibit two distinct behaviors in reaction to the length of pats it receives.  

Program a robotic puppy that uses a touch sensor to receive user input. The puppy should “learn” the difference between pats (short) and strokes (long) and use this knowledge to classify incoming data as pats or strokes and respond accordingly.

The method used to accomplish this is K-Nearest Neighbor, which uses “supervised” training unlike methods like K-Means Clustering, which uses “unsupervised” training.

**Think about these questions: **
* What is the difference between supervised and unsupervised machine learning?
* How does the size of the training set affect your puppy’s ability to learn? How will you decide how large your training set will be?
* What reactions to short pets and long strokes should your puppy have? How will you code for these reactions?

**Hints:**

* When building your own original puppy design, make sure the touch sensor is in an accessible location for petting. 
* Consider adding something to the touch sensor to broaden the area of contact, making it easier to reach over and pet your puppy. 

Your design should be able to learn and recognize the difference between short pets and long strokes, using the supervised learning technique. Once you have trained your puppy with a data set, it should be able to continuously respond to a pet or stroke with a pre-determined reaction. 

Work with your partner to document your initial ideas. Decide how you will evaluate these ideas to pick the best one(s) for your project. Share with another group or your teacher why you chose this solution.

Communicate the results of your group’s work by creating a presentation that demonstrates the functionality of your puppy and the code. 

Ask for feedback and conduct a self-assessment. Use the evaluation tools your teacher has provided.

## AI Lesson 3: Picky Eater ##

Does your puppy love brown biscuits but refuse to eat pink treats? Train your SPIKE Puppy to recognize many different shades of colors beyond simple LEGO bricks and use it to customize your puppy’s reactions to various food sources.

**Design Brief:**

You may choose to design and build your own robotic pet using your SPIKE kit, and feel free to reference the placemat for inspiration! Your puppy should be able to react in at least two different ways to indicate that it has successfully identified a certain color of “food”.

Teach your puppy to recognize any shade of a certain color by training it with real-world objects that have many variations on that color. Training is accomplished by following the prompts printed out on the REPL, and holding an object in front of the puppy’s “mouth” for several seconds, assigning it to a particular category - in this case, a color. Use many different examples for each color category - the more examples, the better your puppy will learn! After training the puppy for a few color categories, program your puppy to react accordingly when it sees any variation on one of the colors it has been trained for.

**Think about these questions: **
* How can you ensure the use of a wide variety of hues of the same color when training? What objects will you use and why?
* What reactions do you want the puppy to have, and how will you code for that? Does it get happy when it sees orange things and sad when it sees purple things?
* Is this an example of supervised or unsupervised learning?

**Hints:** 

* When training for a specific color, make sure you use many different hues of that color. For example, if you are training for the color blue, be sure to use dark and pale blues, greenish and purplish blues, and a variety of surfaces like smooth, shiny, matte, rough, fuzzy, soft, etc. 
* When training for a specific color, move the observed object around during the 5 second session so that your puppy can view it from many angles and distances. As the distances and angles of light hitting the surface of the object change, it will produce different variations of color to observe. 

Your puppy should be able to observe an object’s color and correctly categorize it into one of your pre-trained color groups. When it has correctly categorized the color, it will produce an accompanying reaction. Train your puppy to recognize at least three different colors. 

Work with your partner to document your initial ideas. Decide how you will evaluate these ideas to pick the best one(s) for your project. Share with another group or your teacher why you chose this solution.

Communicate the results of your group’s work by creating a presentation that demonstrates the functionality of your puppy and the code. 

Ask for feedback and conduct a self-assessment. Use the evaluation tools your teacher has provided.

## AI Lesson 4: Fetch! ##

Uh oh! The ball you tossed for your pet landed in the tall grass and disappeared. Teach your SPIKE Puppy to predict how long it must run to fetch the ball, having only caught an initial glimpse of where it landed. 

**Design Brief:**

In this particular lesson, it is advised that students build their own “puppy” models that can roll forward and backward on wheels. Additionally, the puppy models must include the ultrasonic sensor mounted in such a way that the puppy can “see” ahead of itself and sense the distance to its target, as well as a touch sensor to substitute for another button. Feel free to reference the corresponding lesson placemat for inspiration and building tips!

Using one of two different methods, you will train your puppy to learn how quickly it can move forward. In the Linear Regression Modeling method, the puppy will prompt you via the REPL to give it a number of seconds to move, using the right and left buttons on the SPIKE hub. Once it has moved for that amount of time, record the distance (in cm) the puppy has traveled, and enter that distance into the SPIKE hub using the right and left arrows. Continue this process multiple times, teaching the puppy how far it goes for varying amounts of time. Once you have completed enough training sets, the puppy should “know” how much time it should take to move for a given target distance. 

In the Reinforcement Learning method, you will give your puppy a specific distance to move. Once the distance is received, the puppy will make a random guess for how long it should move (between 1 and 6 seconds) and will move for that amount of time. You will give the puppy feedback on whether it moved too far (right button), not enough (left button), or if it hit its target (touch sensor). The puppy learns from each new training session, and should show improvement over time. Once the puppy routinely hits its target distance on the first try, your puppy is ready for the real test! Note: you must specify beforehand how many training sessions you wish to conduct -- it is advised that you do at least four, but more is better. Once you have completed enough training sets, the puppy should “know” how much time it should take to move for a given target distance. 

Once your puppy has been properly trained, you will place an object in front of it to take a one-time reading of its distance with the ultrasonic sensor. Make sure to put a mark on the floor so that once the target is removed, its previous location is still known. Remove the object, and allow the puppy to attempt to reach the location where the target was, using its newly-learned knowledge of how fast it moves. 

**Think about these questions: **
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

## AI Lesson 5: Visual Cues ##

Train your LEGO SPIKE Puppy to follow your visual commands, such as hand signals and body poses.

**Design Brief:**

You may choose to design and build your own robotic pet using your SPIKE kit, and feel free to reference the placemat for inspiration! Make sure that your model is able to respond to your commands by performing at least two different actions. 

Using an API that works with online artificial intelligence, train your puppy to respond to your visual cues. In this case, the AI source will be Google’s TeachableMachine. The data generated by the TeachableMachine will be stored in AirTable (a multi-use online data storage app), and relayed to your SPIKE through AirTable. 

**Think about these questions: **
* In what circumstances would it be useful to activate machines and systems with visual commands? 
* What kinds of visual cues will you use for your commands? What reactions will those commands trigger in your puppy?
* Using an API requires using information that is specific to your account. Keeping this information secure is very important. How will you keep your API information safe?

**Hints:**

* TeachableMachine uses body poses in PoseNet. It can easily recognize a person’s head, torso, and full-body movements. Think of ways you can orient your body to create command gestures.
* Try to make your visual commands as different as possible. For example, tilting your head to the left for one command, and tilting your head to the right for a different command. 
* Closely follow the instructions in README.md to set up your AirTable account, acquire your API key and Base ID, and transfer data from TeachableMachine.

Your design should be able to accurately recognize at least two different commands, and execute them upon seeing them through your computer’s webcam. 

Work with your partner to document your initial ideas. Decide how you will evaluate these ideas to pick the best one(s) for your project. Share with another group or your teacher why you chose this solution.

Communicate the results of your group’s work by creating a presentation that demonstrates the functionality of your puppy and the code. 

Ask for feedback and conduct a self-assessment. Use the evaluation tools your teacher has provided.
