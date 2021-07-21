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
