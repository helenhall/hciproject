# Club Connections

## Setup

### Requirement

- Python 3.11
- Flask
  - Install Flask by following instructions listed [here](https://flask.palletsprojects.com/en/2.2.x/installation/).

### Dependencies Installation

> pip install -r requirements.txt

### Run Project
First have to run the server using the run.sh file which includes: 
 > pipenv run python app.py
 Here's the web address in web file: http://cpsc484-04.yale.internal:8080/

### Explanation and Tasks
  We set out to accomplish two tasks: 1. Give the student ability to explore clubs that meet their interests and 2. Give students the ability (via QR codes) to easily access the club to hopefully join! During the coding process with help from TAs, our project design changed slightly and we decided to focus more on the quiz feature rather than the drawing feature. So essentially, Club Connect is a quiz game which connects students to clubs that match their interests through fun questions. You should be able to use both left and right hands to navigate through the website, but you (purposefully for error elimination) have to hold your hand up in the right position for a few seconds until for the quiz questions the box turns green. There also must only be one person in the camera view, and ideally you would be a few steps back from the display. 

### Collaboration Record
<br>
####Allan Ding (azd5):
<b>Frontend:</b>
Implemented: sketch.js, question.html, info.html, still_there.html, question.css, info.css
- (sketch.js) Implemented the logic to detect hand location relative to chest to select the respective quadrant in question.html
- (sketch.js) Implemented player tracking functionality
- (sketch.js) Implemented logic to determine valid answer selection when highlighted
- (still_there.html, question.html) Implemented timeout functionality: if no answer is selected in 2 minutes, then the application will revert to the index page.

<b>Backend:</b>
Implemented: app.py 
- Set up routes for index, info, question, response, and results
- Implemented functions that query database.py and club.py and pass results to their respective html templates, rendering them with Jinja.
- Implemented QR code functionally for results page using qrserver API
- Created and implemented run.sh, setup.sh, web files to run code on monitor (shell scripts)

<b>Misc:</b> 
- Scheduled times for the group to meet.
- Divided tasks among project groups.
- Reorganized file structure to contain static and templates folded
- Tested code with recorded and live TV data



####Helen Hall: hrh24
- completely reformated prototype in figma, adding design such as:
  -  made a logo in photoshop
  -  figured out the color scheme
  -  Made each section look more visually appealing
- Made the homepage look like the new figma using CSS - so learned Tailwind CSS and applied those formats
- Started implementing flask
- Error checked for app.py, so read through and understood code, figured out how to record sample data to check console log
- created and managed the repository and merge/pull requests
- Came up with 10 questions (4 answers each) and how each club result comes from the questions - final questions displayed
- Met with group for 2 hours on April 24 to discuss questions/databses/camera and tested display
- Finally, worked on readme file (explanation and tasks) and adding last elements to home page

####Yibo Yan: yy644
- Worked on design, refinement and implementation of result page for displaying club QR code results, including styling. 
- Worked with Kevin on designing and implementing dataset for club information.
- Worked with Allan on fixing issues with website.
- Partially worked on readme discussing preparation for our project.

####Kevin Wu: sw952
- For the implementation of the prototype, I was primarily responsible for question design, collecting club data and implementing the backend. My first contribution is the initial design of questions. I collected data on over 80 clubs we included in  our prototype  and designed over ten questions that the user will answer to determine the clubs the prototype recommends. I designed questions that broke down clubs into large, reasonable categories. During this process, I collected names and categories and other information of clubs that we included for this assignment. I was also responsible for designing and implementing the backend for the prototype. I started to implement a SQL backend database that has relations Questions, Answers, Categories. The chief difficulty was for the database to be able to tell if answers lead to follow up questions or a suggested category. At the end, we decided to use multiple python dictionaries and Classes to replace a SQL backend for the flow of the prototype. I implemented the questions, answers and helped implement the clubs data structures. Code I implemented was shared with my team via text.
