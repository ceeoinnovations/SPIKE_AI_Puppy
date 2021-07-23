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

[Link to EV3 Core Set Puppy Model](https://le-www-live-s.legocdn.com/sc/media/lessons/mindstorms-ev3/building-instructions/ev3-model-core-set-puppy-7a316ae71b8ecdcd72ad4c4bcd15845d.pdf "Link to EV3 Core Set Puppy Model") 

For students building their own models, make sure they design their puppies to be able to perform at least two different actions, triggered by their commands. 


## Coding Tips

Students will first use visual commands to train image models on TeachableMachine and use its powerful machine learning algorithm to convert those image commands to text representations of various classes such as “Stop”, “Sit”, or “Come”. The class text will be pushed to Airtable and stored. The EV3 can then retrieve the class text from Airtable using an API.

This multi-stage flow of information can be overwhelming for some students, which is why much of the work has been already done behind the scenes in the airtable.py file and “On PC” html code. Depending on the experience level of your students, you may wish to teach by presenting the code up front and guiding students through an exploration of it to deduce its function. For other students, it may be enough to simply use the supporting files as a “black box”. 

Be sure to have students check port identities in their code, especially if students build their own designs. A common source of frustration can be mismatched sensors and motors in the wrong port.



## Main Program & Possible Solutions

This example code uses a training session from TeachableMachine to give visual commands to a single motor. A TeachableMachine training model was already completed, using two classes named On and Off.

**Note:** When filling in your infromation for voice_command ==, spelling and case must be an exact match with what is being printed in the AirTable cells. 
For ease of use, only open the "On EV3" folder in your VSCode. Open the "On PC" folder in your computer's file browser. 

```
#!/usr/bin/env pybricks-micropython
"""
Artificial Intelligence Lesson 5 Example Code
Prototype by Tufts Center for Engineering Education and Outreach
June 2020
This code is intended for use on a LEGO EV3 running MicroPython v2.0.
"""
from pybricks.hubs import EV3Brick
# from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import secrets
import airtable

# Write your program here
ev3 = EV3Brick()
ev3.speaker.beep()
motorA = Motor(Port.A)

while True:

    pose_command = airtable.Get_AT("Table 1", "Name")
    print(pose_command)
    if pose_command == "On":
        motorA.run(70)
    elif pose_command == "Off":
        motorA.stop()
    else:
        pass

    wait(100)


'''
By calling Get_AT, you will receive the name of the most likely pose, after you've trained your model.
Use conditional statements (think "if the pose is _____, then do ____") to move your dog.
Don't forget to put your APIKey and your Tag!
NOTE: The exact name (spelling and capitalization) of your classes must be inserted where the XXXXXX is
'''
© 2020 GitHub, Inc.
```

**On PC**

Run the TeachablePose.html file on Google Chrome. Enter your Airtable ApiKey, BaseID, and url from TeachableMachines and click submit. When you are ready press Start. You will have to allow Chrome to access your microphone. Allow this to continue running in the background while you control the EV3 via VSCode. If you have multiple tabs open in Chrome, this tab must be on top or else it will not respond. Close the Chrome browser or refresh when you are done.

Find the full instructions and code in the [README.md file](https://github.com/tuftsceeo/EV3_AI_Demos/blob/master/Lesson_5/README.md "README.md file")


## Differentiation

Simplify this lesson by…
* Providing all the example code up front and having students only modify code that already functions.
* Reducing the complexity of reactions the puppy could produce


Take this lesson to the next level by…
* Having students add additional commands and puppy reactions
* Mount a mobile webcam to the puppy itself and try running the entire code on the EV3, bypassing the need for Google Chrome as an intermediary.




## Assessment Opportunities

**Teacher Assessment:** 
Create a scale that matches your needs, for example:
Partially accomplished
Fully accomplished
Overachieved

Use the following success criteria to evaluate your students' progress:
* Students can design and build a puppy capable of displaying various reactions in response to specific visual commands
* Students successfully link their TeachableMachine training data to their EV3 with the appropriate code
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
