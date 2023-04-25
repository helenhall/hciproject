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

Allan Ding (azd5):
Contribution Record:
Frontend: 
- Implemented: sketch.js, question.html, info.html, still_there.html, question.css, info.css
  - (sketch.js) Implemented the logic to detect hand location relative to chest to select the respective quadrant in question.html
  - (sketch.js) Implemented player tracking functionality
  - (sketch.js) Implemented logic to determine valid answer selection when highlighted
  - (still_there.html, question.html) Implemented timeout functionality: if no answer is selected in 2 minutes, then the application will revert to the index page.
Backend:
- Implemented: app.py 
  - Set up routes for index, info, question, response, and results
  - Implemented functions that query database.py and club.py and pass results to their respective html templates, rendering them with Jinja.
  - Implemented QR code functionally for results page using qrserver API
  - Created and implemented run.sh web files to run code on monitor (shell scripts)

Misc: 
- Scheduled times for the group to meet.
- Divided tasks among project groups.
- Reorganized file structure to contain static and templates folded
- Tested code with recorded and live TV data



Helen Hall: hrh24
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

Yibo Yan: yy644
- Worked on design, refinement and implementation of result page for displaying club QR code results, including styling. 
- Worked with Kevin on designing and implementing dataset for club information.
- Worked with Allan on fixing issues with website.
- Partially worked on readme discussing preparation for our project.

