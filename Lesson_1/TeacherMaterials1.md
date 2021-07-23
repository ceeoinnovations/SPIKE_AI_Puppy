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

[Lesson1Main_Example.py}(https://github.com/ceeoinnovations/SPIKE_AI_Puppy/blob/main/Lesson_1/Lesson1Main_Example.py)



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
