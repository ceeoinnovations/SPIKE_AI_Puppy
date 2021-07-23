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
