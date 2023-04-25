
// Adapted from https://p5js.org/examples/interaction-snake-game.html
//
var host = "cpsc484-04.yale.internal:8888";
// var host = "127.0.0.1:4444";

let up = document.getElementById('up');
let down = document.getElementById('down');
let left = document.getElementById('left');
let right = document.getElementById('right');
let topleft = document.getElementById("1");
let topright = document.getElementById("2");
let bottomleft = document.getElementById("3");
let bottomright = document.getElementById("4");



$(document).ready(function() {
  frames.start();
});

var frames = {
  socket: null,

  start: function() {
    var url = "ws://" + host + "/frames";
    frames.socket = new WebSocket(url);
    frames.socket.onmessage = function (event) {
      var command = frames.get_command(JSON.parse(event.data));
      if (command) {
        console.log("exists", topleft);
        if (up !== null) {
            check_raised_hand(command);
            sleep(2000);
        } else if (bottomright) {
            // if in question.html
            console.log("bruh");
            select_square(command);
            sleep(2000);
        }
      } else {
        if (bottomright) {
            resetSquares()
        }
      }
    }
  },

  get_command: function (frame) {
    console.log(frame)
    var command = 0;
    // if there are no people in the frame
    if (frame.people.length < 1) {
      return command;
    }

    var pxy = frame.people[0].joints[2]["pixel"];
    var chest_x = pxy["x"];
    var chest_y = pxy["y"];
    // var chest_z = pxy["y"]

    var px = (frame.people[0].joints[8]["pixel"]["x"] - chest_x) * -1;
    var py = (frame.people[0].joints[8]["pixel"]["y"] - chest_y) * -1;

    console.log("normalized wrist pix",px, py);

    if (py > 60) {
      //up
      if (px > 10) {
        //topright
        command = 1;
      } else if (px < -50) {
        //topleft
        command = 2;
      }
    } else if (py < -20) {
      if (px > 5) {
        //bottomright
        command = 3;
      } else if (px < -80) {
        //bottomleft
        command = 4;
      }
    } 


    var rpx = (frame.people[0].joints[15]["pixel"]["x"] - chest_x) * -1;
    var rpy = (frame.people[0].joints[15]["pixel"]["y"] - chest_y) * -1;


    console.log("right wrist pix",rpx, rpy);


    if (rpy > 60) {
      //up
      if (rpx > 50) {
        //topright
        command = 1;
        // console.log("updated");
      } else if (rpx < -10) {
        //topleft
        command = 2;
        console.log("updated");
      }
    } else if (rpy < -20) {
      if (rpx > 80) {
        //bottomright
        command = 3;
        console.log("updated");
      } else if (rpx < -5) {
        //bottomleft
        command = 4;
        console.log("updated");

      }
    } 
    console.log("command", command)
    return command;
  },



  get_right_wrist_command: function (frame) {
    var command = null;
    if (frame.people.length < 1) {
        return command;
    }

    var pelvis_x = frame.people[0].joints[0].position.x;
    var pelvis_y = frame.people[0].joints[0].position.y;
    var pelvis_z = frame.people[0].joints[0].position.z;
    var right_wrist_x = (frame.people[0].joints[15].position.x - pelvis_x) * -1;
    var right_wrist_y = (frame.people[0].joints[15].position.y - pelvis_y) * -1;
    var right_wrist_z = (frame.people[0].joints[15].position.z - pelvis_z) * -1;
  }
};


// Code that triggers the initial event

function change_page(url) {
    window.location.href = url;
};



function check_answer(boxID) {
  setTimeout(function () {
      if (boxID.style.backgroundColor == "green") {
          console.log("GOOD SEARCH", boxID);
          let tagID = boxID.getAttribute("id") + "tag";
          console.log("tagid", tagID);
          let tag = document.getElementById(tagID);
          console.log("tag", tag);
          change_page(tag.getAttribute("href"));
          resetSquares();
          setTimeout(function () {
              console.log("pause again");
          })
      }
  }, 2000)
};

function check_raised_hand(command) {
  if (command == 1 || command == 2) {
    let url = "/question/1";
    change_page(url);
  }
};



function select_square(command) {
  console.log("inside select", command);
  resetSquares()
  if (command == 5 || command == 0) {
      resetSquares(); 
  } else if (command == 2) {
      topleft.style.backgroundColor = "green";
      setTimeout(check_answer(topleft), 1000);
  } else if (command == 1) {
      topright.style.backgroundColor = "green";
      setTimeout(check_answer(topright), 1000);
  } else if (command == 3) {
      bottomleft.style.backgroundColor = "green";
      setTimeout(check_answer(bottomleft), 1000);
  } else if (command == 4) {
      bottomright.style.backgroundColor = "green";
      setTimeout(check_answer(bottomright), 1000);
  }
};

function resetSquares() {
  topleft.style.backgroundColor = "white";
  topright.style.backgroundColor = "white";
  bottomleft.style.backgroundColor = "white";
  bottomright.style.backgroundColor = "white";
};

function sendWristCommand(command) {
  resetColors();
  if (command == 73) {
      up.style.color = "green";
  } else if (command == 75) {
      down.style.color = "green";
  } else if (command == 76) {
      right.style.color = "green";
  } else if (command == 74) {
      left.style.color = "green";
  }
};



function sleep(time)
{
    // defer the execution of anonymous function for 
    // 3 seconds and go to next line of code.
    setTimeout(function(){ 

        console.log('waiting');
    }, time);  
}

