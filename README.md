# Programming Church
This repo contains a bunch of lesson for a little band of *'engineers from other disciplines'* (including my nieces) to learn software development and hardware device control using Python and Raspberry Pi

![Programming Church](https://github.com/JohnFunkCode/niece-python-lessons/blob/master/ProgrammingChurch.jpeg "Shane, Megan, Katie, David")


## Tools used:
For these lessons we will rely on core material from the following online material:
* [Udemy Complete Pything Programming Course]( https://www.udemy.com/complete-python-programming-course-beginner-to-advanced/learn/v4/overview) I like this one because it starts people out using Jupyter notebook
* [Packt Beginning Python Video](https://www.packtpub.com/application-development/beginning-python-video) This one is more programmer centric

***
## January 1st session - Getting Started with Jupyter Notebook
In this session we'll review your installation of Anaconda and PyCharm.  And do some simple things with Jupyter notebook.
Jupyter notebook will be familar to you from your MATLAB experience from your engineering courses.
#### Prerequisites
Sections 1 - 3 of the Udemy Complete Python Programming Course
***
## January 7th session - User Input, Dictionaries
In this session we're going to review user input, dictionaries, and introduce for loops.
#### Prerequisites
Sections 4 and 5 of the Udemy Complete Python Programming Course

#### Exercises
* The exercises for the session can be found in this the lessons folder of this repo at: [Jupyter Notebook]( https://github.com/JohnFunkCode/niece-python-lessons/blob/dev/Jan%207%20-%20word%20count%20lesson.ipynb  )
* The stand alone code is available in the src folder of this repo at: [wordcount.py](https://github.com/JohnFunkCode/niece-python-lessons/blob/master/src/wordcount/wordcount.py)

***
## January 15th & January 21st session - Loops, Functions and Modules
In this session we're going to begin our discussions about functions and modules
#### Prerequisites
* Sections 6 and 7 of the Udemy Complete Python Programming course
* Section 6 and 7 of the Packt Beginning Python Video course
* Review sections 1-5 of the Packt Beginning Python Video course - most of this will be a review of material from the Udemy course

#### Exercises
* The exercises for the session can be found in this repo at: [Text Analytics Functions.ipynb](https://github.com/JohnFunkCode/niece-python-lessons/blob/master/January%2015%20-%20Loops%20Functions%20Modules%20.ipynb)

***
## January 28th Session - Using other peoples code 
Kids now days don't understand how lucky they are to have such broad collection of third party code to work with.  You can find a library of code someone else has written to do just about anything you can imagine now days.  In this session we're going to learn how to use add-on packages in Python.  

#### Prerequisites
* Read about using Python packages by reading the two following articles
  * [Python Package Tutorial](https://packaging.python.org/tutorials/installing-packages/)
  * [Python Package Documentation](https://docs.python.org/3/installing/index.html)
* Read about the [Python Standard Libraries](https://docs.python.org/3/library/index.html)  Don't worry about memorizing all of them or learning how to use all of them, for now just get familar with what's available.  Also pick one or two you want to explore.
* Read about [Matplotlib](https://matplotlib.org/)  Again don't worry about learning how to use all of Matplot, just get familar with what's available.   We'll start to explore it with some labs.

#### Exercises
We'll start the day learning how to plot the results of our analysis on a graph using Matplotlib.
Then our main exercise for this session will build on our text analytics theme.
We'll move away from simple user input and instead get the text for our analysis from files using capabilites of the python standar libraries.  
* Our first exercise is to learn to use Matplotlib the exercise for that is [Jan 28 - Matt Plot Experimentation.ipynb](https://github.com/JohnFunkCode/niece-python-lessons/blob/master/Jan%2028%20-%20Matt%20Plot%20Experimentation.ipynb)
* Our second exercise using text analytics is in [Jan 28 - File Reading Experiements.ipynb](https://github.com/JohnFunkCode/niece-python-lessons/blob/master/Jan%2028%20-%20File%20Reading%20Experiements.ipynb)


***
## February 4th Session - It's time for Pi
We've been learning the core of the Python language for a month now.  Let's change it up and have some fun and build our first Raspberry Pi project.

### Prerequisites
* Get a [Raspberry Pi starter kit](https://github.com/JohnFunkCode/niece-python-lessons/blob/master/RaspberryPIStarterKit.md)
* Read the [Packt Python Programming with Raspberry Pi](https://www.packtpub.com/hardware-and-creative/python-programming-raspberry-pi) book.  (or at least as much of it as you can)
* Download [GitHub for Windows](git@github.com:xacaxulu/niece-python-lessons.git).  After installing GitHub for Windows - reboot your system.   Then open a command window and type *git* and you should see a list of github options.
* Read the [GitHub Tutorial](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)

### Exercises
#### Exercise 1 - Get your Raspberry Pi running
* If you haven't already, we'll format your memory card and load NOOBS.  Follow the instructions in the [How to get NOOBS tutorial](
https://www.raspberrypi.org/documentation/installation/noobs.md)

#### Exercise 2 - VNC to your Raspberry Pi
The next thing you need is to be able to remotely control your Raspberry Pi from your laptop.
* To do that you need to install VNC on both your latptop and your Raspberry Pi.
Follow the step in [Raspberry Pi VNC Tutorial](https://www.raspberrypi.org/documentation/remote-access/vnc/)
* Install [Real VNC Viewer on Windows](https://www.realvnc.com/en/connect/download/viewer/windows/)

#### Exercise 3 - Sharing Code with your Raspberry Pi via Github
* Create a new repository with a very simple README stating this is your first Raspberry Pi project.
* On your laptop use git clone to clone your new repository into your code directory.
* Using Atom or Pycharm create a simple Python program that prints the digits 1 - 10
* Commit those changes and push them back to the repo
* On your raspberry pi clone your new repository into a directory called code

#### Exercise 4 - built a circuit to connect a LED to a GPIO Pin
There is a great tutorial on this at [ThePiHut](https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins)
Don't worry much about the code, we'll get the code in the next exercise

#### Exercise 5 - Code to Control the GPIO pins of your Raspberry PI
* We will be using the Gpiozero library for all of our code.  They have a great [documentation and recipies site](https://gpiozero.readthedocs.io/en/stable/)
* fork my repository at https://github.com/JohnFunkCode/RaspberryPiTutorial-1 if you need help see: https://help.github.com/articles/fork-a-repo/
* clone your repository to laptop
* change the code to make it blink the LED 10 times in a for loop
* push it back to github and clone it down to your Raspberry Pi

#### Exercise 6 - Extra Credit - More advanced interactions with Rasberry Pi
Using VNC to remote to the Rasberry Pi is easy and it gives you a lot of functionality.  Pulling Code from Github is also a very good practice and it allows you to use more powerful tools on your laptop in your development.  But you should also know the quick and dirty ways to interact with the Rasberry Pi.  The fastest way to get access to these tools is to install Ubuntu Linix on you Windows 10 laptop.  This sounds complicated, but in the Windows 10 Fall Creators update Microsoft made it really easy.  Just follow the steps on the [Developer's Tidbits blog](https://devtidbits.com/2017/11/09/ubuntu-linux-on-windows-10-how-to/)

One you have it open you can learn to use a few unix tools to interact with your Raspberry Pi
* SSH - SSH allows you to open a remote terminal session to your Raspberry Pi - Here is a good [tutorial](https://www.raspberrypi.org/magpi/ssh-remote-control-raspberry-pi/)
* SCP - SCP allows you to directly copy files to and from your Raspberry Pi - Here is a good [tutorial](https://www.raspberrypi.org/documentation/remote-access/ssh/scp.md)

***
## February 11th Session - Simple Components with Raspberry Pi
Now that we got the Raspberry Pi's running and know how to get code on them via Github we're going to continue
last week's exercises to build some simple circuits and write a bunch of code on the Raspberry.

#### Exercise 1
Build a circuit to connect an LED to a GPIO pin and write some code to make it blink.   Look back at Excercise 4 from 
last week for more details

#### Exercise 2
Build a circuit to connect a bunch of LEDs to GPIO pins and write some code to make them race up and down.  Example code for this
is in src/gpiozero-racingLED.py

#### Excercise 3
Play with Pulse Width Modulation to vary the duty cycle you put on your LEDs to make them glow etc.  Example code for this 
is in src/gpiozero-pwmLED.py

#### Excercise 4
Add some buttons to your LED circuit and write some code to do things with them.   I suggest first just making sure your buttons
work, then make them start your string of LEDs racing.   Example code for this is in **src/gpizero-buttons.py**
(hint - use the GPIOZero button.whenpressed() method.  There is a great example in the [GPIOZero Recipies](http://gpiozero.readthedocs.io/en/stable/recipes.html)

***
## February 17th Session - Creating Web UI with Flask - Part 1
After taking a brief side trip to explore building circuites and programming hardware with our Raspberry Pi's its time to get back to more code.  This week we're going to begin creating web UI's in python so our code can be more interactive.  There are a lot of new concepts for you to learn so this will most likely take a few sessions.

Homework Assignment:
To get an understanding of where we're going listen to the entire [Flask Tutorial Step by Step](https://www.udemy.com/python-flask-tutorial-step-by-step/learn/v4/content) course on Udemy.  This first time through, don't try to do any of the lectures, I just want you to get a broad understanding of what the Flask framework does so we can work through it piece by piece. 

We are also going to step up our game and start working with Pycharm which is a more professional integrated development environment (IDE).  Please review the [Pycharm Quick Start Guide](https://www.jetbrains.com/help/pycharm/quick-start-guide.html)

Another handy reference you'll need is the [W3Schools](https://www.w3schools.com/) HTML web development site.

#### Solutions
My solutions for these exercises are in my [flask-textanalytics repo](https://github.com/JohnFunkCode/flask-textanalytics)

#### Exercise 1 - building your first flask application
Using Pycharm we're going to create a new project and build a very simple flask app.  I like the folder structure Santiago uses to organize his work in the Udemy [Flask Tutorial Step by Step](https://www.udemy.com/python-flask-tutorial-step-by-step/learn/v4/content), so we'll mimic it.
* First create a new repo named **flask-textanalytics** in github.  Make sure to select everything at the bottom to create python get ignor, and an MIT licences, and generate a README.md file.  Clone this project into your code directory on your computer.
* Next create a new project in Pycharm - put in in your code directory in a directory called **flask-textanalytics**
* Create a Python file for the main driver of your flask applicaton in the root of the project following the pattern of [Flask Tutorial Step by Step - Section 3](https://github.com/rmotr/flask-introduction/blob/master/flask_introduction/run_app.py)
* Create a libraries module in your application to house the code of the application.  In the library module create a python file with a route that handles the url route "/" by simply returning a string saying "hello world"
* once the code is working check it into Github

#### Exercise 2 - rendering an html template
In this exercise we'll extend what you've built so far to setup a simple flask template and pass it a variable to include in the information it outputs.
* Add the a route to handle the "/test" route with a function that calls render_template to render a file called index.html
* create a file called index.html in the templates directory
* pass a variable with a string containing your name in it to the template and have it include your name someone in the body of the data returned.
* once the code is working check it into Github

#### Exercise 3 - Rendering a form and displaying the user's input
In this exercise we'll extend what you've built so far to render an html form to gather two strings from the user.   When the user posts that data, we'll render another template to display the two string.
* Add a route to handle the "/textanalytics" route with a function that renders either a form, or an html document with results depending on if it gets a GET or a POST method.
* Add two html documents to your templates directory one called "textanalytics_form.html" with an input form in it, and one called "textanalytics_form_results.html" to display the two strings gathered by the form.
* once the code is working check it into Github

#### Exercise 4 - Hook up your text analytics funcitons from a few weeks ago
In this exercise we'll use the text anlytics module you wrote a few weeks ago to calculate the words in common between the two strings the user inputs into the web forms from the previous exercise.
* Copy your text analytics code into a directory called model in your library directory
* Call you text analytics union method from the "POST" method of your function that handle the "/textanalytics" route and pass the results to the render template code that displays your textanalytics_form_results template.
* Add code into your template to display the dictionary returned by your textanalytics.union() function.
* once the code is working check it into Github

***
## February 25th Session - Playing with WebUI's
Ok, you're on your own this week.  It's your chance to get creative playing with building simple web UI's.  Spend some time before class this week to explore some of my suggestions below to see what you want to try to build this week.
Here are some of my suggestions:
* Build variations on your text analytics code.   We've surfaced the Union function, but how about the other funcitons?
* Dress your templates up a bit with fancier HTML. Megan knows HTML pretty well, and there is a great HTML Tutorial at [w3schools.com](https://www.w3schools.com/html/).  See if you can make one of your templates look presentable.
* Build a UI for your racing lights on your rasberry pi.  There is endless combinations you can build:
    - Make the lights race up, or down 
    - Show the user a bunch of radio buttons and let them choose what LED to light up, or even use a pulldown menu to let them choose to make it light solid, blink, or even make it glow using the [Pulse Width Modulation PMWLED methods](http://gpiozero.readthedocs.io/en/stable/recipes.html#led-with-variable-brightness)

Home Work:
* Listen to [Cornilia Davis's talk about Women and Technology](https://www.youtube.com/watch?v=2lFv3qknbqQ)
* Write code!!!!

***
## March 3rd Session - Objects and More Web UI (We probably won't get through this section in 1 week)
Today we'll start with more pure Python code.  It's time you learn the next step in oranizing your code by working with classes.  Classes are the basis for Object Oriented programming which is a very important topic to master because it helps decompoze complex ideas into simpler more usable code.  After that we'll go back to working with a more sophisticated flask web app to control your raspberry Pi. 

##### Homework Assignment:
* Listen to the recording on Classes in Python that I provided.
* Learn about Github tagging and releases.  I abuse the tagging mechanism to show the stages of development in these lessons.  Here are a few resources to help you learn about tagging:
  * https://git-scm.com/book/en/v2/Git-Basics-Tagging
  * https://www.youtube.com/watch?v=90ynNkDzaNY

#### Exercise 1
Write a class to encapsuate the functionality of your Raspberry Pi LED contraption.  It should do the following:
* Initialize itself by setting up all the LEDs we need to control.
* Provide a led_on() method to turn on individual LEDs
* Provide a led_off() method to turn off individual LEDs
* Provide a race_up() method to make the leds race up
* Provide a race_down() method to make the leds race down
* Provide a dance_randomly() method to make the leds dance on and off randomly
* Your class should also include tests when the file is run by itself using the **if __name__ == "__main__"** trick you've learned.
##### Solution
My solution can be found at in my [flask-pi-led-control](https://github.com/JohnFunkCode/flask-pi-led-control/blob/WithPi/library/raspi/pi_led_contraption.py) repo with the *WithPI* tag in the library/raspi directory.

#### Exercise 2
Create a static html site with the following pages:
* index.html - acts as the home page and has a menu to get to all the other pages
* individual.html - has a menu to get to the other pages and a text box with on/off radio buttons to allow the user to control individual LEDs.
* group.html - has the menu, and a bunch of radio buttons to allow a user to turn on or off any of the LEDs at once.
* patterns.html - had the menu, and buttons to allow the user to make the LEDs race up, race down, or dance randomly.
##### Solution
My solution can be found at in my [flask-pi-led-control](https://github.com/JohnFunkCode/flask-pi-led-control/tree/static-html) repo with the *static-html* tag.

#### Exercise 3
Turn your static html site into a flask application.  You'll need to do the following:
- Setup a base flask app by copying the structure of our previous flask examples
    - Setup a libraries directory for our code and templates
    - create a driver app called run_app.py in the root of the project
    - added requirements.txt to make sure the environment include Flask
- Moved the static html into the templates directory
- Create a file called flask_pi_led_controll_app.py with all the routes for the app.
- Moved the stylesheet into /library/static/styles and changed all the html files to refer to it.
##### Solution
My solution can be found at in my [flask-pi-led-control](https://github.com/JohnFunkCode/flask-pi-led-control/tree/FlaskFromStaticHTML) repo with the *FlaskFromStaticHTML* tag.

#### Exercise 4
Wire in your class that encapsulates the functionality of your Raspberry Pi LED contraption into your flask application. A few tips for doing this include:
- Set defaults for all your radio buttons in the HTML files, to make processing the forms easier.
- Create a mock-up of your rasberry pi contraption class with all the GPIO handling stripped out.  This will make it easier to test on your PC before you move things to your raspbery pi.  I did this by simply making a copy of my class file and stripped out anything GPIO related to create a mock object that implements all right methods.
##### Solution
My solution can be found at in my [flask-pi-led-control](https://github.com/JohnFunkCode/flask-pi-led-control/tree/WithPi) repo with the *WithPi* tag.


***
## April 15 Session - Wrap up Flask Pi LED Contraption 
We've spent several weeks getting our Flask based Pi Contraption that flashes LEDs by using a clean object design and an HTML interface.  That's actually quite an accomplishment.  It's non-trivial and it has many apects of a real-world project built into it!!!!  Great Job!

#### Exercise - Mobile responsive CSS
Before moving on we'll talk a little bit more about CSS styling for mobile devices.   I've pulled all the HTML and CSS out of my Pi LED Contraption project and put it on my website at: http://www.johnfunk.com/responsive/
- look it it with Chrome's developer tools
- Dig into the CSS a bit deeper and notice the I have a wrapper class that I apply to the Body.  Also notice that I also use a variable font to help change the font size on various devices.   This is a very simple setup that scales the font size to make things work better across many different devices.

Look at the following articles to learn more about how to make things look better on mobile:
- https://css-tricks.com/fun-viewport-units/
- https://www.smashingmagazine.com/2016/05/fluid-typography/
- https://css-tricks.com/viewport-sized-typography/

## April 22 Session - Begining Our first IoT project
Today we'll wrap that up and move on to an even more intersting and more realworld project.   We're going to working on our first IoT project using techniques that IoT startup companies in their projects.  Our little project will use an Ada Fruit ADXL1345 Accelarometer to detect motion and report that back to a cloud based collection center where we can analyze the data collected from all the devices in our little internet of things world.

####  Exercise 1 - Get started with the ADXL345 Accelerometer
First read the instructions about using the ADXL345 accelerometer in the manual of your Sunfounder kit.  In my version of the kit it's exercise 14.  Your version might be a bit different.

- Wire up the Accelrometer circut according ot the manual in your sunfounder kit.  I recommend putting this on a different breakout board.  But you might put in on the same board as your LEDs if you want to show them all off together and don't mind a more complicated circuit.

- Get the sample code working
 - The core example on the Sunfounder site doesn't work: https://www.sunfounder.com/learn/Super_Kit_V2_for_RaspberryPi/lesson-14-adxl345-super-kit-for-raspberrypi.html

 - I found it's better to go direct to Adafurit’s github at: https://github.com/adafruit/Adafruit_Python_ADXL345

 - However, it doesn’t clearly explain all the pre-requisits.  Read the following article on stack exchange (and pay attention to the last line) https://raspberrypi.stackexchange.com/questions/14153/adafruit-i2c-library-problem?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

 - Here are the steps I followed to get things running:
```
sudo apt-get update
sudo apt-get install python-smbus
sudo apt-get install i2c-tools
```
Then you need to change your raspberry pi configuration:
```
sudo raspi-config
````
In the next screen choose, in order:
- Interfacing Options
- I2C - enable I2C


***
## May 6 Session - flask-pi-iot
This week we'll start by debugging any circuit or setup problems with the ADXL345 accelerometer.  From there we'll begin to build
an appliction for the Raspberry Pi that reads data from the ADXL345 and sends it via an HTTP post to a Flask application running on your laptop.

![Project Architecture](https://github.com/JohnFunkCode/ProgrammingChurch/blob/master/diagrams/flask-pi-iot-architecture1.png "Project Architecture")

#### Exercise 1 - Raspberry Pi code
Use the [Requests](http://docs.python-requests.org/en/master/user/quickstart/) library and the [Adafruit_Python_ADXL345](https://github.com/adafruit/Adafruit_Python_ADXL345) libary to write code for the Raspberry Pi that reads the sensor and uses an http post to send the x,y,z data to a flask app on your laptop. 

#### Solution
My solution can be found at [accelerometer_post.py](https://github.com/JohnFunkCode/flask-pi-iot/blob/master/pi_client/accelerometer_post.py)

#### Exercise 2 - Flask App
Using what we've learned about Flask so far write a Flask app that runs on your laptop.   It should have a route that handles the data your Raspberry Pi code posts to your app and print it to the console.   Also create a route for index.html to show something if someone goes to your app with a browser (we'll expand the UI in the future).   

#### Solution
If you need help remembering how to buidl a Flask app, look back at your last project code before simply using my solution.  My solution can be found at [fask-pi-iot](https://github.com/JohnFunkCode/flask-pi-iot)

***
## May 20 Session - flask-pi-iot part 2: To the cloud!

#### Exercise 1 - Create an account on [Pivotal Web Services](https://run.pivotal.io/)
Go to **[run.pivotal.io](https://run.pivotal.io/)** and create an account.

#### Exercise 2 - Install the Cloud Foundry CLI
Follow the steps in the [Pivotal Web Services Documentation](https://docs.run.pivotal.io/cf-cli/) to install the Cloud Foundry CLI and read a bit to get familar with it.

#### Exercise 3 - Read about building Flask apps on Pivotal Web Services
Read the article [WebApp in 5 minutes: Deploying a Flask Python App to Pivotal Web Services](http://exaforge.com/webapp-in-5-minutes-deploying-a-flask-python-app-to-pivotal-web-servicescf).   

#### Exercise 4 - Deploy your the flask poriton of your Flask Pi IoT project to Pivotal Web Services
Using the article in exercise 3 deploy your application to Pivotal Web Services.   
- You will have to create an **requrements.txt** file and you'll have to create **Procfile** as described in the article.
- You will also have to change the URL that your Raspberry Pi code uses to post data to the flask app

