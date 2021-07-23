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
