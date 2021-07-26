# Artificial Intelligence & Machine Learning: Training Your Robot Puppy

### Learning Promise

In this unit, your students will continue to develop their coding and engineering skills by designing their own interactive projects that utilize the fundamentals of artificial intelligence and machine learning. Students will design machine learning training sets, collect and evaluate data, anticipate machine reactions, and develop multi-step systems that successfully interact with users. By developing systems that can be quantitatively and qualitatively tested for functionality, students will work across a variety of academic disciplines to meet specific design criteria and constraints. Building upon basic coding skills, students will be introduced to specially developed classes and functions, giving them the opportunity to recognize patterns while exploring existing code. Students will also work with APIs to send and receive data, and develop their own commands and functions in MicroPython. 

This learning sequence was specially designed for use with the LEGO SPIKE Prime, but the puppy can be designed in many different ways. However, students are encouraged to get creative and design their own robotic pets that can learn and interact with their owners. 



# Lesson 1: Sit

It’s time for basic obedience training! Teach your SPIKE Puppy to recognize the commands for “sit” and “stand”.

### Time:120+

### Level: Beginner

### Grades: 9 - 12



## Teacher Support

### Key Learning Objectives

* Students will explore methods of machine observation
* Students will conduct machine training
* Students will utilize training to develop a desired response


### Machine Learning Methods

* Supervised 1-dimensional minimum-distance-to-mean clustering
* Nearest centroid method of classification


### Things You Will Need

* LEGO® Education SPIKE™ Prime Set
* IDE compatible with MicroPython


### Additional Resources

* [AI & Machine Learning Overview Guide for Teachers](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/AI_Intro.md)
* [Lesson1Training.py](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/1f4c65a7e62537f2b88f7436f167bcddeded817f/Lesson_1/Lesson1Training.py) provided module


### Compatibility

This lesson works on the following operating systems: Windows, MacOS.


### Educational Standards

NGSS
* HS-ETS1-2 Design a solution to a complex real-world problem by breaking it down into smaller, more manageable problems that can be solved through engineering.
* HS-ETS1-3. Evaluate a solution to a complex real-world problem-based on prioritized criteria and trade-offs that account for a range of constraints, including cost, safety, reliability, and aesthetics, as well as possible social, cultural, and environmental impacts.

CSTA
* 3A-AP-13 Create prototypes that use algorithms to solve computational problems by leveraging prior student knowledge and personal interests.
* 3A-AP-17 Decompose problems into smaller components through systematic analysis, using constructs such as procedures, modules, and/or objects.
* 3A-AP-18 Create artifacts by using procedures within a program, combinations of data and procedures, or independent but interrelated programs.

Extension Standards

* 3B-IC-27 Predict how computational innovations that have revolutionized aspects of our culture might evolve.
* 3A-IC-24 Evaluate the ways computing impacts personal, ethical, social, economic, and cultural practices.

English Language Arts Extension:
* CCSS.ELA-LITERACY.W.9-10.2 Write informative/explanatory texts to examine and convey complex ideas, concepts, and information clearly and accurately through the effective selection, organization, and analysis of content.


## Student Material

[Student Worksheet Guide](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/Lesson_1/StudentWorksheet1.md)


1. ### Prepare

* Read through this teacher material.
* If you feel it is needed, plan a lesson using the "getting started" material in the LEGO Education SPIKE Prime app. This will help familiarize your students with their SPIKE Prime.
* If you feel it is needed, plan a lesson on supervised 1-dimensional minimum-distance-to-mean clustering and the nearest centroid method of classification.


2. ### Engage (30 minutes)

* Use the ideas in the Ignite a Discussion section below to engage your students in a discussion related to this project.
* Explain the project.
* Split your class into teams of two students.
* Allow your students some time to brainstorm, and record their initial ideas about how they will build and code to meet the objectives.


3. ### Explore (90+ minutes)

* Have students build their puppy. If they are using an original design instead of the EV3 model, be sure they include some functionality that will allow it to respond to the students’ commands. 
* Make sure students have time to iterate and build multiple prototypes if needed.
* Once students prepare their code, have them experiment with multiple methods of training (comparing a few data samples to a large number of samples). 
* Encourage both students in each pair to explore the building aspects and the coding aspects. 
* Allow students to explore the example code provided in this lesson.


4. ### Explain (30 minutes)

* Assemble students to have a “mid-design review” discussion mid way through their work where each group shares their current progress and struggles. Facilitate a discussion where students give and receive advice on specific coding and building struggles and share building and coding strategies that have been useful. 
* Highlight common motor or sensor-specific coding methods that may be useful for students. 
* Have students reflect on their work so far (successes, difficulties, surprises), and write a plan for how they will proceed to improve and finish.


5. ### Elaborate (30 - 60 minutes)

* Students continue working on their projects, improving and completing their coding and any building/design modifications.
* Give students time to document their final designs and prepare a presentation.
* Facilitate a sharing session in which each team presents their results.


6. ### Evaluate

* Give feedback on each student's performance.
* You can use the assessment ideas provided to simplify the process.


## Ignite a Discussion

Machine Learning is an incredibly complex subject, but some of the basics can be easily grasped. In the case of **1-dimensional minimum-distance-to-mean clustering**, data can be easily visualized on a 1-dimensional number line, allowing students to see the clusters of data. In this case, you could create a number line representing the distance the ultrasonic sensor is sensing, and visualize how similar distance readings would end up being clustered together in the same general area of the number line. When a new random point is added to the line, students can judge for themselves which cluster it should belong to, but what is their reasoning? Talk about **nearest centroid classification**, and how you can determine which cluster the data point most likely belongs to by determining which cluster’s center is closer to the new data point. 

Encourage an active brainstorming process. Have a discussion with your students around these questions: 
* What is the difference between supervised and unsupervised learning? What makes this project an example of supervised learning?
* How does the complexity of the task change if you add a third command, or a fourth? 
* Will the clustering and classification methods being used work perfectly every time? Can you think of examples where the system can be fooled?

Have students formulate initial solutions and how they will build for them and code for it. Have them outline the process by which they will train and test their prototypes and describe how their end product should function. They should also talk about design constraints and criteria. In this way, students set their own goals and understand how to evaluate their progress.


## Building Tips

When designing their puppies, have students consider how they will utilize the motors to have their pet sit and stand, and maintain stability throughout the process.  


## Coding Tips

Depending on your students’ coding experience, you may wish to demonstrate how to use the specialized classes and functions being provided in Lesson1Training.py by showing them the Lesson1Main_Example.py file. Depending on your specific learning objectives, you may wish to have students explore Lesson1Training.py on their own to determine how it functions, or you may wish to walk them through it step by step.

Be sure to have students check the ports of each sensor and motor, and update the code accordingly. A common source of frustration can be mismatched sensors and motors in the wrong port. 


## Main Program & Possible Solutions

The example code leads the user through a training session and a testing session. There are two different ultrasonic sensor positions being trained, with Command A corresponding to sitting and Command B corresponding to standing. Note that the code has been written such that it should begin the lesson in standing mode, and that if it receives a command it has already executed, it will not repeat the same command.

[Lesson1Main_Example.py](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/Lesson_1/Lesson1Main_Example.py)


## Differentiation

Simplify this lesson by…
* Providing all the example code up front and having students only modify code that already functions.
* Reducing the complexity of the build by having a pet that waves an arm back and forth, or does some other simple function.

Take this lesson to the next level by…
* Encouraging students to try training for 3 or more different commands at once.
* Not providing the Lesson1Main_Example.py file and having students design their own code that utilizes the Lesson1Training.py file.


## Assessment Opportunities

**Teacher Assessment:** 
Create a scale that matches your needs, for example:
* Partially accomplished
* Fully accomplished
* Overachieved

Use the following success criteria to evaluate your students' progress:
* Students can build a functioning puppy/pet that can execute at least two different actions.
* Students can conduct training sessions and collect data for their model.
* After undergoing training, the puppy responds to new input and reacts accordingly.
* Students can self-reflect honestly and accurately on their work, both before, during, and after completion of the project. 

**Student Self-Assessment:** 
Have students reflect on their device function description and goals from the brainstorming session at the beginning of the lesson. Did they meet the goals they set for themselves? Have students explain (via writing, presentation, or other means) how they know their device was successful or not. Give students time to reflect, and ask them to come up with at least two ways they could improve upon their design. 

**Peer Feedback:** 
Students tend to struggle with giving and receiving feedback and constructive criticism, as it is not usually modeled or directly taught in classes. Educators are encouraged to actively teach good feedback skills when students are sharing their work both within their team and among the class at large. The aspects of good feedback are that it is: direct, useful, and respectful. Direct feedback addresses specific aspects of a project instead of general observations like “It doesn’t work” or “It gets the job done”. Useful feedback is helpful to the person receiving it because it addresses issues that are able to be fixed instead of pointing out things that cannot be reasonably addressed within the scope of the class. Respectful feedback avoids personal criticism or unnecessary harshness.


## Extensions

**Psychology/English Language Arts:** 
Why are so many robots that interact with humans built to resemble animals or other people? Have students write about their robotic pets that they’ve built, and how they feel about them. Can they identify instances when it would be beneficial to feel a social or emotional connection to a machine that they work with? Can they identify instances when it would be harmful to do so? Encourage them to identify the personal, ethical, social, economic, and cultural impact that these kinds of human-robot interactions can have. 

**Ethics/English Language Arts:** 
When training even a simple artificial intelligence algorithm, there is the potential for the machine to develop a bias -- a learned tendency to favor one thing over another unfairly or unreasonably. No data set is “perfect”, and even small imperfections within data sets can be amplified by machine learning into biased results. Biased data sets can be anything from scientifically incomplete or statistically skewed information, to socially or morally questionable content created by people with conscious or unconscious prejudice or favoritism. Machines that learn from biased data sets can perpetuate that bias, causing unfair or inaccurate outcomes. AI systems are rapidly being integrated into society everywhere in fields as diverse as medical diagnoses, job applicant reviews, plagiarism detection, and criminal justice profiling. AI is an automated decision making process, which can be inequitable or even harmful when left to itself without the contextual awareness that human minds possess. Have students research instances of bias in artificial intelligence systems and document what they find by presenting, writing a paper, or creating a poster or table on the dangers of AI bias, and what can be done to combat it.  


## Career Links

Students who enjoyed this lesson might be interested in exploring these career pathways:
* Information Technology (Computer Science)
* Artificial Intelligence and Machine Learning (Computer Science)
* Robotics (Mechanical Engineering) 




# Lesson 2: Pet the Puppy

Show your pet some love. Teach your SPIKE Puppy to notice the difference between exciting short pets and calming long strokes on its back. 

### Time: 120+ minutes

### Level: Beginner

### Grades: 9 - 12


## Teacher Support

### Key Learning Objectives

* Students will conduct machine training.
* Students will utilize training to develop a desired response.
* Students will recognize the difference between Supervised vs. Unsupervised Machine Learning, and the difference between Clustering and Classification.

### Machine Learning Methods
* 1 Dimensional K-Nearest Neighbor (Supervised)
* 1 Dimensional K-Means Clustering (Unsupervised)
* Nearest Centroid classification (Unsupervised)

### Things You Will Need

* LEGO® Education SPIKE™ Prime Set
* IDE compatible with MicroPython

### Additional Resources

* [AI & Machine Learning Overview Guide for Teachers](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/AI_Intro.md)
* [Lesson2Training.py](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/Lesson_2/Lesson2Training.py) provided module

### Compatibility

This lesson works on the following operating systems: Windows, MacOS

### Educational Standards

NGSS
* HS-ETS1-2 Design a solution to a complex real-world problem by breaking it down into smaller, more manageable problems that can be solved through engineering.
* HS-ETS1-3. Evaluate a solution to a complex real-world problem-based on prioritized criteria and trade-offs that account for a range of constraints, including cost, safety, reliability, and aesthetics, as well as possible social, cultural, and environmental impacts.

CSTA
* 3A-AP-13 Create prototypes that use algorithms to solve computational problems by leveraging prior student knowledge and personal interests.
* 3A-AP-17 Decompose problems into smaller components through systematic analysis, using constructs such as procedures, modules, and/or objects.
* 3A-AP-18 Create artifacts by using procedures within a program, combinations of data and procedures, or independent but interrelated programs.
* 3A-DA-12 Create computational models that represent the relationships among different elements of data collected from a phenomenon or process.

English Language Arts Extension:
* CCSS.ELA-LITERACY.W.9-10.2 Write informative/explanatory texts to examine and convey complex ideas, concepts, and information clearly and accurately through the effective selection, organization, and analysis of content.


## Student Material

[Student Worksheet Guide](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/Lesson_2/StudentWorksheet2.md) 


1. ### Prepare

* Read through this teacher material.
* If you feel it is needed, plan a lesson using the "getting started" material in the LEGO Education SPIKE Prime app. This will help familiarize your students with their SPIKE Prime.
* If you feel it is needed, plan a lesson on the specific topics of K-Nearest Neighbor and K-Means Clustering machine learning methods. 


2. ### Engage (30 - 60 minutes)

* Use the ideas in the Ignite a Discussion section below to engage your students in a discussion related to this project.
* Explain the project.
* Split your class into teams of two students.
* Allow your students some time to brainstorm, and record their initial ideas about how they will build and code to meet the objectives.


3. ### Explore (90+ minutes)

* Have students build their puppy. Be sure they include some functionality that will allow it to respond to the students’ commands. 
* Make sure students have time to iterate and build multiple prototypes if needed.
* Once students prepare their puppy and code, have them experiment with the supervised training. 
* Encourage both students in each pair to explore the building aspects and the coding aspects. 
* Allow students to explore coding for their systems without providing example code first.


4. ### Explain (30 minutes)

* Assemble students to have a “mid-design review” discussion mid way through their work where each group shares their current progress and struggles. Facilitate a discussion where students give and receive advice on specific coding and building struggles and share building and coding strategies that have been useful. 
* Highlight common motor or sensor-specific coding methods that may be useful for students. Share the example code provided below so that students may clearly see an example of how to accomplish the task.
* Have students reflect on their work so far (successes, difficulties, surprises), and write a plan for how they will proceed to improve and finish.


5. ### Elaborate (30 - 60 minutes)

* Students continue working on their projects, improving and completing their coding and any building/design modifications.
* Give students time to document their final designs and prepare a presentation.
* Facilitate a sharing session in which each team presents their results.


6. ### Evaluate

* Give feedback on each student's performance.
* You can use the assessment ideas provided to simplify the process.




## Ignite a Discussion

When humans learn to categorize something we’ve never seen before, there is usually one of two ways we do it. In some cases, we are given many examples of Category A and Category B, and we learn to take new items and compare them to the examples, and decide which category they belong in. In other cases, we are not given explicit examples, but after observing a bunch of Item A’s and Item B’s we can tell them apart by clustering them into groups that share similar traits. When a new item comes along, we see how it fits into our self-made clusters and decide which group it belongs to. These are examples of **supervised** and **unsupervised learning**. In supervised learning, examples of each category are given in advance. In unsupervised learning, data in a set are clustered into groups by virtue of their attributes, and new data are categorized similarly. 

Machine learning can also be classified as supervised or unsupervised. In this lesson, two different methods for training the puppy are presented. In the **K-Nearest Neighbor** method, we use supervised training by giving the puppy examples of short pets and long strokes before asking it to identify a new touch. With **K-Means Clustering**, the puppy observes a set of pets and strokes, and then decides how they differ. 

In each case, a decision must be made to help us sort new data. In the **supervised** method, you could visualize a number line where the numbers represent the time it takes the touch to occur. After taking a set of pets and a set of strokes, the data might look like this:
![L2E1](/images/L2E1.png)

The green dots are pets, and the purple dots are strokes. How can we use these labeled data to make a decision about a new touch of unknown identity? We could try to choose a dividing line where any value above the line would be a stroke, and any value below would be a pat. There would be a clear separation between pats and strokes, but what value should we make the dividing line on this data set? 0.6 ms? 0.7 ms? Some other number? How should we choose? One possibility would be to find the midpoint between the highest pat value and the lowest stroke value. In this case, the dividing line would be (0.548 +0.801)/2 = 0.675 ms. With that division, all of our training set data are correctly categorized. However, most of the pat values are much smaller than 0.548 ms. That highest pat was an outlier. It would probably be better to choose a lower value for our dividing line. But how much lower?

Most of the algorithms that are used for these problems are considerably more sophisticated (and more complicated) than the simple midpoint one we just discussed. (And most of the training sets used are much larger than ten examples!) There is no single perfect algorithm; instead, computer scientists must weigh a number of factors in choosing the most appropriate algorithm to use: the quality and quantity of the data available, the computing power available, the potential consequences of misclassifying items, and many other factors. 

One common and relatively simple approach to choosing a dividing line is the **K-Nearest Neighbor** algorithm. In this method, to classify a new piece of data you look at the k (number of) points closest to it in the training set. Whatever classification the majority of those points have, you assign that classification to your new piece of data. For example, if you use k=1, you look at the single number in the training set that is closest to your new value. If the training set neighbor is classified as a pat, then your new value is also a pat. If the training set neighbor is a stroke, then your new value is classified as a stroke. If you use k=3, you look at the three nearest values in the training set. Whichever classification two of them have (or perhaps all three, depending upon your data), will be the classification you assign to your new piece of data.


With an **unsupervised** data set, we have data but no labels. Again, picturing it on a one-dimensional number line, we have: 
![L2E2](/images/L2E2.png)

Our human brains can easily see that we have two basic clusters and one outlier in the middle which is closer to the left side. A machine cannot make these observations, so how can it be done with math? In the **K-Means Clustering** method, two random points are selected and the distance to each data point is measured. Each data point is then assigned to belong to one of the two random points - whichever is closer. With these two (mostly arbitrary) new groups, the middle point (or mean) is calculated and a new center of the group is defined. These steps are repeated with the new center points for each group. Some data points will change which group they belong to, and others will stay the same. If this process keeps being repeated, the center point of each group gradually shifts to the actual centers of the clusters, making the final definition of each cluster more or less accurate. The algorithm determines that the clusters have been successfully defined when the identity of individual data points stops changing over each iteration. 
The K-Means Clustering algorithm is not guaranteed to find the best classification of the points. Depending upon the initial centers chosen at random, it can get “stuck” on a suboptimal solution. Because of this, often the algorithm is run multiple times with different initial centers.

Encourage an active brainstorming process. Have a discussion with your students around these questions: 
* Humans classify data into different groups all the time—heads or tails, fair or foul, dots or dashes. How can we teach a machine to divide data into meaningful groups?
* What are the benefits and drawbacks to using supervised learning? 
* What are the benefits and drawbacks to using unsupervised learning?
* How will you determine how many trials will be enough to train your model? 

Have students formulate initial solutions and how they will build for them and code for them. Have them outline the process by which they will test their prototypes and describe how their end product should function. They should also talk about design constraints and criteria. In this way, students set their own goals and understand how to evaluate their progress.


## Building Tips

As students build their own designs, have them consider how they will utilize the touch sensor for ease of petting.  

## Coding Tips

Depending on your students’ coding experience, you may wish to demonstrate how to use the specialized classes and functions being provided and walk them through the example code. Depending on your specific learning objectives, you may wish to have students explore Lesson2Training.py on their own to determine how they function, or you may wish to walk them through it step by step.

Be sure to have students check port identities in their code. A common source of frustration can be mismatched sensors and motors in the wrong port. 




## Main Program & Possible Solutions

**K-Nearest Neighbor Method**
This example code walks a user through training the puppy with a set of pets and a set of strokes (supervised learning) before having the puppy react. 

[Lesson2Main_Example](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/Lesson_2/Lesson2Main_Example.py)


## Differentiation

Simplify this lesson by…
* Providing all the example code up front and having students only modify code that already functions.
* Reducing the complexity of the build by having a pet that waves an arm back and forth, or does some other simple function.


Take this lesson to the next level by…
* Having the puppy’s behavior change for repeated pats or strokes. For example, if the puppy receives three pats in a row, it exhibits a new, happier behavior.
* Limiting exposure to the example code and challenging students to create their own code, using the Lesson2Training.py as a reference. 
* Highly Advanced: Limiting exposure to any assistive code and having students come up with their own algorithm to determine K-Nearest Neighbor or K-Means Clustering.


## Assessment Opportunities

**Teacher Assessment:** 
Create a scale that matches your needs, for example:
* Partially accomplished
* Fully accomplished
* Overachieved

Use the following success criteria to evaluate your students' progress:
* Students can build a functioning puppy/pet that can execute at least two different actions.
* Students can conduct training sessions and collect data for their model.
* After undergoing training, the puppy responds to new input and reacts accordingly.
* Students can self-reflect honestly and accurately on their work, both before, during, and after completion of the project. 

**Student Self-Assessment:** 
Have students reflect on their device function description and goals from the brainstorming session at the beginning of the lesson. Did they meet the goals they set for themselves? Have students explain (via writing, presentation, or other means) how they know their device was successful or not. Give students time to reflect, and ask them to come up with at least two ways they could improve upon their design. 

**Peer Feedback:** 
Students tend to struggle with giving and receiving feedback and constructive criticism, as it is not usually modeled or directly taught in classes. Educators are encouraged to actively teach good feedback skills when students are sharing their work both within their team and among the class at large. The aspects of good feedback are that it is: direct, useful, and respectful. Direct feedback addresses specific aspects of a project instead of general observations like “It doesn’t work” or “It gets the job done”. Useful feedback is helpful to the person receiving it because it addresses issues that are able to be fixed instead of pointing out things that cannot be reasonably addressed within the scope of the class. Respectful feedback avoids personal criticism or unnecessary harshness.


## Extensions

**Mathematics**
The k in the K-nearest neighbor algorithm tells how many nearby points are examined in deciding whether a new data point is a pat or a stroke. The code you used had k=3. What happens if you make k larger and then run the code? What if you make k smaller? Devise a strategy for systematically investigating the effects of changing k.

Something to think about: Generally, odd numbers are used for k rather than even numbers. What is the advantage of odd numbers?

**English Language Arts:** 
Creating social robots, robots designed to interact with humans (like your puppy), is an active area of artificial intelligence. Investigate the field of social robots. What are some of the most successful social robots that have been created thus far? What are some of the hurdles to creating robots that can interact effectively with humans? Have students research social robots document what they find by presenting, writing a paper, or creating a poster.


## Career Links

Students who enjoyed this lesson might be interested in exploring these career pathways:
* Information Technology (Computer Science)
* Artificial Intelligence and Machine Learning (Computer Science)
* Robotics (Mechanical Engineering) 




# Lesson 3: Picky Eater

Does your puppy love brown biscuits but refuse to eat pink treats? Train your SPIKE Puppy to recognize many different shades of colors beyond simple LEGO bricks and use this ability to customize your puppy’s reactions to various food sources.

### Time: 120+ minutes

### Level: Intermediate

### Grades: 9 - 12


## Teacher Support

### Key Learning Objectives

* Students will explore methods of machine observation
* Students will conduct machine training
* Students will utilize training to develop a desired response
* Students will explore higher-dimensional data processing and the impacts of initial training data


### Machine Learning Methods

* 3-Dimensional K-Nearest Neighbor


### Things You Will Need

* LEGO® Education SPIKE™ Prime Set
* IDE compatible with MicroPython


### Additional Resources

* [AI & Machine Learning Overview Guide for Teachers](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/AI_Intro.md)
* [Lesson3Training.py](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/Lesson_3/Lesson3Training.py) provided module


### Compatibility

This lesson works on the following operating systems: Windows, MacOS


### Educational Standards

NCSS
* HS-ETS1-2 Design a solution to a complex real-world problem by breaking it down into smaller, more manageable problems that can be solved through engineering.
* HS-ETS1-3. Evaluate a solution to a complex real-world problem-based on prioritized criteria and trade-offs that account for a range of constraints, including cost, safety, reliability, and aesthetics, as well as possible social, cultural, and environmental impacts.

CSTA
* 3A-AP-13 Create prototypes that use algorithms to solve computational problems by leveraging prior student knowledge and personal interests.
* 3A-AP-17 Decompose problems into smaller components through systematic analysis, using constructs such as procedures, modules, and/or objects.
* 3A-AP-18 Create artifacts by using procedures within a program, combinations of data and procedures, or independent but interrelated programs.
* 3A-DA-12 Create computational models that represent the relationships among different elements of data collected from a phenomenon or process.

English Language Arts Extension:
* CCSS.ELA-LITERACY.W.9-10.2 Write informative/explanatory texts to examine and convey complex ideas, concepts, and information clearly and accurately through the effective selection, organization, and analysis of content.




## Student Material

[Student Worksheet Guide](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/Lesson_3/StudentWorksheet3.md)


1. ### Prepare

* Read through this teacher material.
* If you feel it is needed, plan a lesson using the "getting started" material in the LEGO Education SPIKE Prime app. This will help familiarize your students with their SPIKE Prime.
* If you feel it is needed, plan a lesson on the K-Nearest Neighbor machine learning algorithm


2. ### Engage (30 - 60 minutes)

* Use the ideas in the Ignite a Discussion section below to engage your students in a discussion related to this project.
* Explain the project.
* Split your class into teams of two students.
* Allow your students some time to brainstorm, and record their initial ideas about how they will build and code to meet the objectives. 


3. ### Explore (90+ minutes)

* Have students build their puppy. Be sure they include some functionality that will allow it to respond to the students’ commands.
* Students should gather objects that are different hues of the same color, and use them for their training model. See the Student Worksheet Starter for specific advice on how to train your models. 
* Make sure students have time to iterate and build multiple prototypes if needed.
* Encourage both students in each pair to explore the building aspects and the coding aspects. 
* Allow students to explore coding for their systems without providing example code first.


4. ### Explain (30 minutes)

* Assemble students to have a “mid-design review” discussion mid way through their work where each group shares their current progress and struggles. Facilitate a discussion where students give and receive advice on specific coding and building struggles and share building and coding strategies that have been useful. 
* Highlight common motor or sensor-specific coding methods that may be useful for students. Share the example code provided below so that students may clearly see an example of how to accomplish the task.
* Have students reflect on their work so far (successes, difficulties, surprises), and write a plan for how they will proceed to improve and finish.


5. ### Elaborate (30 - 60 minutes)

* Students continue working on their projects, improving and completing their coding and any building/design modifications.
* Give students time to document their final designs and prepare a presentation.
* Facilitate a sharing session in which each team presents their results.


6. ### Evaluate

* Give feedback on each student's performance.
* You can use the assessment ideas provided to simplify the process.


## Ignite a Discussion

Have you ever noticed that classifying colors can sometimes be a tricky thing? Is that object pink, or orange? Is this object a shade of blue or green, or some color in between? If humans have trouble identifying colors sometimes, imagine the difficulties that computers can have! The basic SPIKE Prime color sensor functions by reading the amount of red, blue, and green light that it detects and matching that detection to a predetermined list of simple colors that correspond to LEGO bricks. In this lesson, the sensor’s RGB setting is used to just output the RGB values instead of the name of the color it is closest to. 

The color sensor collects data for red, green, and blue light -- three different dimensions of data. In Lesson 2, we explained how the K-Nearest Neighbor algorithm worked in one dimension, using a number line as an example. In this new case, one can imagine THREE number lines, with each data point having a value on all three lines simultaneously: how much red light, how much green light, and how much blue light. Three-dimensional data can be difficult for students to think about, but it is not too complex for an algorithm. In many real-life applications of AI, data sets can have even more dimensions! 

Encourage an active brainstorming process. Have a discussion with your students around these questions: 
* Is this training method an example of supervised or unsupervised learning? How do you know?
* How does the ultrasonic sensor aid in color recognition?
* How can you ensure the use of a wide variety of hues of the same color when training? What objects will you use and why?
* What reactions do you want you puppy to have, and how will you code for that? Does it get happy when it sees orange things and sad when it sees purple things?

Have students formulate initial solutions and how they will build for them and code for them. Have them outline the process by which they will test their prototypes and describe how their end product should function. They should also talk about design constraints and criteria. In this way, students set their own goals and understand how to evaluate their progress.


## Building Tips

As students build their own designs, have them consider how they will place the color sensor in an accessible location to make observations. 

## Coding Tips

Depending on your students’ coding experience, you may wish to demonstrate how to use the specialized classes and functions being provided and walk them through the example code. Depending on your specific learning objectives, you may wish to have students explore Lesson3Training.py on their own to determine how they function, or you may wish to walk them through it step by step. 

Be sure to have students check port identities in their code. A common source of frustration can be mismatched sensors and motors in the wrong port. 


## Main Program & Possible Solutions

This example code shows a method for training the puppy for various colors, assigned to classes, and then testing the training to see if the puppy reacts accordingly. The default K value is 5, but can be modified by students

[Lesson3Main_Example.py](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/Lesson_3/Lesson3Main_Example.py)

## Differentiation

Simplify this lesson by…

* Providing all the example code up front and having students only modify code that already functions.
* Only having students work with two different color classifications instead of three or more.
* Reducing the complexity of the build by having a pet that waves an arm back and forth, or does some other simple function.


Take this lesson to the next level by…

* Increasing the number of different colors training colors to four or more. 
* Limiting exposure to the example code and challenging students to create their own code, using Lesson3Main_Example.py as a reference.


## Assessment Opportunities

**Teacher Assessment:** 
Create a scale that matches your needs, for example:
* Partially accomplished
* Fully accomplished
* Overachieved

Use the following success criteria to evaluate your students' progress:
* Students can build a functioning puppy/pet that can execute at least three different actions.
* Students can conduct training sessions and collect data for their model.
* After undergoing training, the puppy responds to new input and reacts accordingly, successfully recognizing colors out of at least three options.
* Students can self-reflect honestly and accurately on their work, both before, during, and after completion of the project. 

**Student Self-Assessment:** 
Have students reflect on their device function description and goals from the brainstorming session at the beginning of the lesson. Did they meet the goals they set for themselves? Have students explain (via writing, presentation, or other means) how they know their device was successful or not. Give students time to reflect, and ask them to come up with at least two ways they could improve upon their design. 

**Peer Feedback:** 
Students tend to struggle with giving and receiving feedback and constructive criticism, as it is not usually modeled or directly taught in classes. Educators are encouraged to actively teach good feedback skills when students are sharing their work both within their team and among the class at large. The aspects of good feedback are that it is: direct, useful, and respectful. Direct feedback addresses specific aspects of a project instead of general observations like “It doesn’t work” or “It gets the job done”. Useful feedback is helpful to the person receiving it because it addresses issues that are able to be fixed instead of pointing out things that cannot be reasonably addressed within the scope of the class. Respectful feedback avoids personal criticism or unnecessary harshness.


## Extensions

**Biology/English Language Arts:** 
Throughout the animal kingdom, animals have a wide range of visual abilities. Bees and other insects are capable of perceiving light “past” the color violet and into the ultraviolet spectrum. Some fish and snakes can sense light beyond the color red, known as infrared. There are a variety of color perception abilities based on specialized cells in the eyes called cones. What causes color blindness? How many different kinds of color blindness are there, and how common is it? Can some people have better than average color perception? How so? Have students research and learn about how colored vision works, and share written reports documenting what they have learned about color and vision.


## Career Links

Students who enjoyed this lesson might be interested in exploring these career pathways:
* Information Technology (Computer Science)
* Artificial Intelligence and Machine Learning (Computer Science)
* Robotics (Mechanical Engineering) 




# Lesson 4: Fetch!

Uh oh! The ball you tossed for your pet landed in the tall grass and disappeared. Teach your SPIKE Puppy to predict how long it must run to fetch the ball, having only caught an initial glimpse of where it landed.

### Time: 120+ minutes

### Level: Advanced

### Grades: 9 - 12



## Teacher Support


### Key Learning Objectives

* Students will explore methods of machine sensing
* Students will conduct machine training
* Students will utilize training to develop a desired response


### Machine Learning Methods

* Linear Regression modeling
* Reinforcement Learning


### Things You Will Need

* LEGO® Education SPIKE™ Prime Set
* IDE compatible with MicroPython 
* Measuring tape or ruler (in centimeters)


### Additional Resources

* [AI & Machine Learning Overview Guide for Teachers](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/AI_Intro.md)
* [Lesson4Training-LinReg.py](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/Lesson_4/Lesson4Training-LinReg.py) provided module
* [Lesson4Training-ReLearn.py](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/Lesson_4/Lesson4Training-ReLearn.py) provided module


### Compatibility

This lesson works on the following operating systems: Windows, MacOS


### Educational Standards

NGSS
* HS-ETS1-2 Design a solution to a complex real-world problem by breaking it down into smaller, more manageable problems that can be solved through engineering.
* HS-ETS1-3. Evaluate a solution to a complex real-world problem-based on prioritized criteria and trade-offs that account for a range of constraints, including cost, safety, reliability, and aesthetics, as well as possible social, cultural, and environmental impacts.

CSTA
* 3A-AP-13 Create prototypes that use algorithms to solve computational problems by leveraging prior student knowledge and personal interests.
* 3A-AP-17 Decompose problems into smaller components through systematic analysis, using constructs such as procedures, modules, and/or objects.
* 3A-AP-18 Create artifacts by using procedures within a program, combinations of data and procedures, or independent but interrelated programs.
* 3A-DA-12 Create computational models that represent the relationships among different elements of data collected from a phenomenon or process.



## Student Material

[Student Worksheet Guide](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/Lesson_4/StudentWorksheet4.md)


1. ### Prepare

* Read through this teacher material.
* If you feel it is needed, plan a lesson using the "getting started" material in the LEGO Education SPIKE Prime app. This will help familiarize your students with their SPIKE Prime.
* If you feel it is needed, plan a lesson on Linear Regression Modeling and Reinforcement Learning.


2. ### Engage (30 - 60 minutes)

* Use the ideas in the Ignite a Discussion section below to engage your students in a discussion related to this project.
* Explain the project.
* Split your class into teams of two students.
* Allow your students some time to brainstorm, and record their initial ideas about how they will build and code to meet the objectives. 


3. ### Explore (90+ minutes)

* Have students build their puppy, ensuring that their model is able to move forward for a given number of seconds. Their model should also be able to utilize the ultrasonic sensor to take a distance reading from its front. (See Building Tips and Design Brief in the Student Worksheet Starter)
* Have students explore one (or both) machine learning methods, Linear Regression Modeling or Reinforcement Learning.
* Make sure students have time to iterate and build multiple prototypes if needed.
* Encourage both students in each pair to explore the building aspects and the coding aspects. 
* Allow students to explore coding for their systems without providing example code first.


4. ### Explain (30 minutes)

* Assemble students to have a “mid-design review” discussion mid way through their work where each group shares their current progress and struggles. Facilitate a discussion where students give and receive advice on specific coding and building struggles and share building and coding strategies that have been useful. 
* Highlight common motor or sensor-specific coding methods that may be useful for students. Share the example code provided below so that students may clearly see an example of how to accomplish the task.
* Have students reflect on their work so far (successes, difficulties, surprises), and write a plan for how they will proceed to improve and finish.


5. ### Elaborate (30 - 60 minutes)

* Students continue working on their projects, improving and completing their coding and any building/design modifications.
* Give students time to document their final designs and prepare a presentation.
* Facilitate a sharing session in which each team presents their results.


6. ### Evaluate

* Give feedback on each student's performance.
* You can use the assessment ideas provided to simplify the process.



## Ignite a Discussion

Two different methods of machine learning are presented in this lesson. In **Linear Regression Modeling**, the machine uses input to construct an equation that describes the relationship between two sets of data. In this case, the two sets of data are time and distance, which will have a linear relationship to each other as long as the puppy’s speed is constant. The more data is used for training, the more accurate the equation can be. Using this equation as a model, the machine can take a new single data point (a target distance) and compute the corresponding time. In this way, the puppy can make a prediction for how long it must move in order to reach the target distance. 


In **Reinforcement Learning**, the puppy begins with a target distance and randomly selects a number of seconds (in the code provided, 1 - 6 seconds) to move. There are three possible outcomes -- it will overshoot its target, it will not go far enough, or it will stop directly on the target. A human observer judges this outcome, and gives the machine feedback on the result. By collecting feedback from multiple attempts, the machine begins to construct a model that hones in on the correct time to distance ratio and learns from more trials with different target distances. If it is learning correctly, the machine should show improvement over time, getting better at predicting for how long it should move to hit the target. Once the puppy routinely hits its target distance on the first try, it has most likely completed enough trials and is ready for a real test. 

Encourage an active brainstorming process. Have a discussion with your students around these questions: 
* How does collecting data about distance traveled and time spent moving allow the puppy to learn how fast it moves?
* How will I build my puppy to be able to move forward for a given number of seconds?
* Without using AI, what other information must be used by the puppy in order to travel a given distance without constantly getting input from the ultrasonic sensor?

Have students formulate initial solutions and how they will build for them and code for them. Have them outline the process by which they will test their prototypes and describe how their end product should function. They should also talk about design constraints and criteria. In this way, students set their own goals and understand how to evaluate their progress.


## Building Tips

In this particular lesson, it is advised that students build their puppy so that it can roll forward on wheels. However students build their models, make sure that the buttons on the SPIKE Prime hub are easily accessible, as the buttons will be how they give feedback to the puppy. Additionally, all puppy models must include the ultrasonic sensor, mounted in such a way that the puppy can “see” ahead of itself and sense the distance to its target. 

## Coding Tips

Depending on your students’ coding experience, you may wish to demonstrate how to use the specialized classes and functions being provided and walk them through the example code. Depending on your specific learning objectives, you may wish to have students explore Lesson4Training-LinReg.py and Lesson4Training-ReLearn.py on their own to determine how they function, or you may wish to walk them through it step by step.

Be sure to have students check port identities in their code. A common source of frustration can be mismatched sensors and motors in the wrong port.


## Main Program & Possible Solutions

**Method 1: Linear Regression Modeling**
This example code initializes the ultrasonic sensor and motors, and runs through training sessions and testing predictions for a target distance. Students will follow the prompts printed in the REPL. 

[Lesson4Main-LinReg_Example.py](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/Lesson_4/Lesson4Main-LinReg_Example.py)

**Method 2: Reinforcement Learning**
This example code initializes the ultrasonic sensor and motors, and runs through training sessions and testing predictions for a target distance. Note that you must declare the number of trials in your code before running the program. Students will follow the prompts printed in the REPL.

[Lesson4Main-ReLearn_Example.py](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/Lesson_4/Lesson4Main-ReLearn_Example.py)


## Differentiation

Simplify this lesson by…

* Only having students work with one machine learning method
* Providing all the example code up front and having students only modify code that already functions.
* Reducing the complexity of the build by building a simple rolling robot with the ultrasonic sensor mounted at the front


Take this lesson to the next level by…

* Having students work with both machine learning methods
* Limiting exposure to the example code and challenging students to create their own code, using the Lesson4Training-LinReg.py and Lesson4Training-ReLearn.py modules as a reference.


## Assessment Opportunities

**Teacher Assessment:** 
Create a scale that matches your needs, for example:
* Partially accomplished
* Fully accomplished
* Overachieved

Use the following success criteria to evaluate your students' progress:
* Students can build a puppy that successfully moves forward for a given amount of time
* Students can conduct training sessions and collect data for their model.
* After undergoing training, the students’ puppy can accurately move to the target distance
* Students can self-reflect honestly and accurately on their work, both before, during, and after completion of the project. 

**Student Self-Assessment:** 
Have students reflect on their device function description and goals from the brainstorming session at the beginning of the lesson. Did they meet the goals they set for themselves? Have students explain (via writing, presentation, or other means) how they know their device was successful or not. Give students time to reflect, and ask them to come up with at least two ways they could improve upon their design. 

**Peer Feedback:** 
Students tend to struggle with giving and receiving feedback and constructive criticism, as it is not usually modeled or directly taught in classes. Educators are encouraged to actively teach good feedback skills when students are sharing their work both within their team and among the class at large. The aspects of good feedback are that it is: direct, useful, and respectful. Direct feedback addresses specific aspects of a project instead of general observations like “It doesn’t work” or “It gets the job done”. Useful feedback is helpful to the person receiving it because it addresses issues that are able to be fixed instead of pointing out things that cannot be reasonably addressed within the scope of the class. Respectful feedback avoids personal criticism or unnecessary harshness.


## Extensions

**Physics (Linear Regression Model):** 
The linear regression relationship between distance and time is a foundational principle of kinematics. Have students record the time and distance data for each trial, and plot their data on a chart (by hand or using a spreadsheet) with time as the independent variable (x axis) and distance as the dependent variable (y axis). Have students calculate the slope of the best fit trendline, which will be the value of the puppy’s speed. Encourage students to conduct tests on various surfaces (carpet, hard floor, gravel, etc.) and compare charts to see the different slopes. Use this data to draw conclusions about how the surface affects the speed of the puppy. 

Using your data to create your own d vs. t plot and calculate the speed of your puppy. Test on various surfaces (carpet, hard floor, gravel, etc.) to see the different slopes. Also, ask the question: the print output includes the y intercept. Shouldn’t the value always be zero? Make a case why or why not. 


## Career Links

Students who enjoyed this lesson might be interested in exploring these career pathways:
* Information Technology (Computer Science)
* Artificial Intelligence and Machine Learning (Computer Science)
* Robotics (Mechanical Engineering) 




# Lesson 5: Visual Cues

Train your LEGO SPIKE Puppy to follow your visual commands, such as head tilts and body poses.

### Time:120+

### Level: Advanced

### Grades: 9 - 12


## Teacher Support


### Key Learning Objectives

* Students will explore Cloud-based training of advanced models
* Students will utilize an API to send and receive data


### Machine Learning Methods
* Image Recognition


### Things You Will Need

* LEGO® Education SPIKE™ Prime Set
* IDE compatible with MicroPython
* A computer with an on-board camera
* Google Chrome Internet browser
* Access to and an account with [AirTable](https://airtable.com/)
* Access to and an account with [TeachableMachine](https://teachablemachine.withgoogle.com/)
* WiFi dongle and WiFi connection


### Additional Resources

* [AI & Machine Learning Overview Guide for Teachers](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/AI_Intro.md) 
* The modules and instructions hosted [here](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/tree/main/Lesson_5)
* The instructions on how to set up AirTable, TeachableMachine, train visual models, and use the custom modules is given in the [README.md](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/Lesson_5/README.md) file. 


### Compatibility

This lesson works on the following operating systems: Windows, MacOS


### Educational Standards

NGSS
* HS-ETS1-2 Design a solution to a complex real-world problem by breaking it down into smaller, more manageable problems that can be solved through engineering.
* HS-ETS1-3. Evaluate a solution to a complex real-world problem-based on prioritized criteria and trade-offs that account for a range of constraints, including cost, safety, reliability, and aesthetics, as well as possible social, cultural, and environmental impacts.

CSTA
* 3A-AP-13 Create prototypes that use algorithms to solve computational problems by leveraging prior student knowledge and personal interests.
* 3A-AP-17 Decompose problems into smaller components through systematic analysis, using constructs such as procedures, modules, and/or objects. 
* 3A-AP-18 Create artifacts by using procedures within a program, combinations of data and procedures, or independent but interrelated programs.
* 3A-DA-12 Create computational models that represent the relationships among different elements of data collected from a phenomenon or process.

Extenstion CSTA Standards
* 3A-IC-24 Evaluate the ways computing impacts personal, ethical, social, economic, and cultural practices.

English Language Arts Extension
* CCSS.ELA-LITERACY.W.9-10.2 Write informative/explanatory texts to examine and convey complex ideas, concepts, and information clearly and accurately through the effective selection, organization, and analysis of content.


## Student Material

[Student Worksheet Guide](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/Lesson_5/StudentWorksheet5.md)


1. ### Prepare
* Read through this teacher material.
* Read the [README.md file](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/Lesson_5/README.md) (see Additional Resources) to familiarize yourself with how to use and link TeachableMachine and Airtable. 
* If you feel it is needed, plan a lesson using the "getting started" material in the LEGO Education SPIKE Prime app. This will help familiarize your students with their SPIKE Prime.
* If you feel it is needed, plan a lesson to introduce the topic of APIs and/or image recognition technology.


2. ### Engage (30 minutes)
* Use the ideas in the Ignite a Discussion section below to engage your students in a discussion related to this project.
* Explain the project.
* Split your class into teams of two students.
* Allow your students some time to brainstorm, and record their initial ideas about how they will build and code to meet the objectives. 


3. ### Explore (90+ minutes)
* Have students build their puppy. Be sure they include some functionality that will allow it to respond to the students’ commands. 
* Make sure students have time to iterate and build multiple prototypes if needed.
* Encourage both students in each pair to explore the building aspects and the coding aspects. 
* Allow students to explore coding for their systems without providing example code first.


4. ### Explain (30 minutes)
* Assemble students to have a “mid-design review” discussion mid way through their work where each group shares their current progress and struggles. Facilitate a discussion where students give and receive advice on specific coding and building struggles and share building and coding strategies that have been useful. 
* Highlight common motor or sensor-specific coding methods that may be useful for students. Share the example code provided below so that students may clearly see an example of how to use APIs to send and receive data.
* Have students reflect on their work so far (successes, difficulties, surprises), and write a plan for how they will proceed to improve and finish.


5. ### Elaborate (30 minutes)
* Students continue working on their projects, improving and completing their coding and any building/design modifications.
* Give students time to document their final designs and prepare a presentation.
* Facilitate a sharing session in which each team presents their results.


6. ### Evaluate
* Give feedback on each student's performance.
* You can use the assessment ideas provided to simplify the process.


## Ignite a Discussion

TeachableMachine uses machine learning to train an algorithm to learn and recognize different kinds of visual data. Once visual data can be categorized, new visual input can be analyzed and used to activate various programs depending on which category the image is determined to belong to. Machine learning is similar to human learning in that practice makes perfect -- the more you train your model, the more accurately it will work! 

APIs (Application Programming Interface) are useful tools that help link devices to the Internet, allowing them to send and receive information and use a variety of online applications. You can access thousands of APIs on the internet for free. Since some of these websites contain sensitive user data they require authentication. The authentication can be in the form of an API Key or OAuth. In this exercise we will only deal with authentication using API Keys.  API keys should always be stored in a safe location and never be shared as they are directly linked to your account and can cause data and identity theft. 

Encourage an active brainstorming process. Have a discussion with your students around these questions: 
* In what circumstances would it be useful to activate machines and systems with visual commands? 
* What kinds of visual cues will you use for your commands? What reactions will those commands trigger in your puppy?
* Using an API requires using information that is specific to your account. Keeping this information secure is very important. How will you keep your API information safe?

Have students formulate initial solutions and how they will build for it and code for it. Have them outline the process by which they will test their prototypes and describe how their end product should function. They should also talk about design constraints and criteria. In this way, students set their own goals and understand how to evaluate their progress.


## Building Tips

When students build their own models, make sure they design their puppies to be able to perform at least two different actions, triggered by their commands. 


## Coding Tips

Students will first use visual commands to train image models on TeachableMachine and use its powerful machine learning algorithm to convert those image commands to text representations of various classes such as “Stop”, “Sit”, or “Come”. The class text will be pushed to Airtable and stored. The SPIKE can then retrieve the class text from Airtable using an API.

This multi-stage flow of information can be overwhelming for some students, which is why much of the work has been already done behind the scenes in the airtable.py file and “On PC” html code. Depending on the experience level of your students, you may wish to teach by presenting the code up front and guiding students through an exploration of it to deduce its function. For other students, it may be enough to simply use the supporting files as a “black box”. 

Be sure to have students check port identities in their code. A common source of frustration can be mismatched sensors and motors in the wrong port.   


## Main Program & Possible Solutions

This example code uses a training session from TeachableMachine to give visual commands of sit or stand to the puppy. 

[Lesson5Main_Example.py](https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/Lesson_5/Lesson5Main_Example.py)

**On PC:**
Run the TeachablePose.html file on Google Chrome. Enter your Airtable ApiKey, BaseID, and url from TeachableMachines and click submit. When you are ready press Start. You will have to allow Chrome to access your camera. Allow this to continue running in the background while you control the SPIKE via your IDE. If you have multiple tabs open in Chrome, this tab must be on top or else it will not respond. Close the Chrome browser or refresh when you are done.


## Differentiation

Simplify this lesson by…
* Providing all the example code up front and having students only modify code that already functions.
* Reducing the complexity of reactions the puppy could produce

Take this lesson to the next level by…
* Having students add additional commands and puppy reactions
* Mount a mobile webcam to the puppy itself and try running the entire code on the SPIKE, bypassing the need for Google Chrome as an intermediary.


## Assessment Opportunities

**Teacher Assessment:** 
Create a scale that matches your needs, for example:
* Partially accomplished
* Fully accomplished
* Overachieved

Use the following success criteria to evaluate your students' progress:
* Students can design and build a puppy capable of displaying various reactions in response to specific visual commands
* Students successfully link their TeachableMachine training data to their SPIKE with the appropriate code
* Students successfully execute two different visual commands that activate their respective puppy actions
* Students can self-reflect honestly and accurately on their work, both before, during, and after completion of the project. 

**Student Self-Assessment:** 
Have students reflect on their device function description and goals from the brainstorming session at the beginning of the lesson. Did they meet the goals they set for themselves? Have students explain (via writing, presentation, or other means) how they know their device was successful or not. Give students time to reflect, and ask them to come up with at least two ways they could improve upon their design. 

**Peer Feedback:** 
Students tend to struggle with giving and receiving feedback and constructive criticism, as it is not usually modeled or directly taught in classes. Educators are encouraged to actively teach good feedback skills when students are sharing their work both within their team and among the class at large. The aspects of good feedback are that it is: direct, useful, and respectful. Direct feedback addresses specific aspects of a project instead of general observations like “It doesn’t work” or “It gets the job done”. Useful feedback is helpful to the person receiving it because it addresses issues that are able to be fixed instead of pointing out things that cannot be reasonably addressed within the scope of the class. Respectful feedback avoids personal criticism or unnecessary harshness.


## Extensions

**Ethics/English Language Arts Extension:**
To incorporate language arts skills development, have your students research the modern use of image recognition and the issues surrounding privacy and data use, especially concerning facial recognition on social media and in public. Then, have them write a paper weighing the benefits and risks of this technology. 


## Career Links

Students who enjoyed this lesson might be interested in exploring these career pathways:
* Information Technology (Computer Science)
* Artificial Intelligence and Machine Learning (Computer Science)
* Robotics (Mechanical Engineering) 



