# Getting started with Airtable


<details>
<summary>Creating account on Airtable - Creating Base </summary>

<h3> 1. Go to https://airtable.com </h3>
</br>
</br> 

![login screen](/Lesson_5/images/airtable_welcome.png)

</br>
</br>

<h3> 2. Sign in if you have an Airtable account, or Sign up to create a new account</h3>
</br>
</br> 

![sign up screen](/Lesson_5/images/signup.png)![sign in screen](/Lesson_5/images/signin.png)

<h3> 3. Click on Add a base and Start from scratch   </h3>     

![add base screen](/Lesson_5/images/addbase.png)

<h3> and give it a suitable name</h3> 

![name base screen](/Lesson_5/images/namebase.png)
        
<h3> 4. This will open up your new document . Note the names of the Table and Fields </h3>
        
![table view screen](/Lesson_5/images/tableview.png)
</details>



<details>
  <summary>Finding the BaseID </summary>

<h3> 1. Go to https://airtable.com/api </h3>

![api welcome screen](/Lesson_5/images/apiwelcome.png)

<h3> 2. Click on your project name to reveal the api page. Copy the BaseID and replace the "BaseID" in secrets.py with this string </h3>

![api page screen](/Lesson_5/images/apipage.png)

</details>



<details>
  <summary>Creating the API Key</summary>


<h3> 1. Go to https://airtable.com/account and click Generate API Key</h3>

![api welcome screen](/Lesson_5/images/apikey1.png)

<h3> 2. Copy the API Key and replace the "AirtableAPPKey" in secrets.py with this string. Do not share this string.</h3>

![api welcome screen](/Lesson_5/images/apikey2.png)

</details>

# Setting up Teachable Machine on PC

Download the TeachablePose.html file from <i> On PC </i> folder. 



 <details>
 <summary> 1.	Train your Teachable Machine code. </summary>

 <br>
 <br> 

 Go to https://teachablemachine.withgoogle.com/ and click on Get Started button

 <br>
 <br> 

 ![Getting started](/Lesson_5/images/getstarted.png)

 <br>
 <br> 
 </details>

 <details>

 <summary> 2.	Select the Pose Project</summary>

 <br>
 <br> 

 ![pose project](/Lesson_5/images/poseproject.png)

 <br>
 <br> 

 </details>

 <details>

 <summary> 3.	Record poses to train your model  </summary>

 <br>
 <br> 

 Click on the webcam button to start recording. Record many samples for accuracy. Create two different classes, and name them whatever you like. Then click the Train Model button.

 <br>
 <br> 

 ![trainingscreen](/Lesson_5/images/trainingscreen1.png)

 <br>
 <br> 

 </details>

 <details>

 <summary> 4. Export your Model.  </summary>

 <br>
 <br> 

 Once you have recorded all samples and trained your data, click Export Model.

 <br>
 <br> 

 ![trainedscreen](/Lesson_5/images/trainedscreen.png)

 <br>
 <br> 

 </details>

 <details>

 <summary> 5. Get the model url  </summary>

 <br>
 <br>  

 Click on the Upload/Update my cloud model to create or update your model url. Copy the url from this page. 

 <br>
 <br> 

 ![update](/Lesson_5/images/update.png)

 <br>
 <br> 

 </details>

 <details>

 <summary> 6.	Running the TeachablePose.html file. </summary>

 <br>
 <br>  

Open the TeachablePose.html file on Google Chrome. 

Enter the url from Step 5 in the text box saying <i>url</i>.
Also enter the APIKey and BaseID for your  Airtable document in their respective boxes. Refer to the sections <i> Finding the BaseID </i> and <i> Creating API Key </i> above on where to find them.

<br>
<br>
Click submit to begin. You will need to allow Chrome access to your computer's webcam. A box should appear on the left, showing you your webcam view with the pose joints overlaid on top. 


 <br>
 <br> 

 ![apiupdate](/Lesson_5/images/teachableposemodel.png)

 <br>
 <br> 
 
 <i>Note: If you have  edited the Table name and Field name on your Airtable you will have to edit the html file and update the "Editable Section" . </i>

 <br>
 <br>
 </details>



<details>
 
<summary> Optional: editing the html file:</summary>
 
<br>
<br> 
<i> please proceed with caution...</i>

If you want to edit the html file or want to see how the code is written,  right-click and open the html file on an editor. 

<br>
<br> 


 </details>
 
# Setting up the library on SPIKE Prime

Download the main.py and secrets.py files.

<details>
  <summary>Using the library</summary>
   
<h3> 0. Download secrets.py to your SPIKE Prime.</h3>


<h3> 1. Edit the secrets.py file</h3>

Edit the secrets.py file by replacing BaseID and API Key from your account. Refer to the sections <i> Finding the BaseID </i> and <i> Creating API Key </i> above on how to do it.


<h3> 2. Edit the main.py file</h3>

You can start playing with the library using main.py. It shows how you can import the airtable library and use the available function. 


</details>
