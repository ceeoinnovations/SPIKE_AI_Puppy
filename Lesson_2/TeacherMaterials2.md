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
