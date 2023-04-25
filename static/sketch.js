
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

let time_to_select = 3000;
let current_person_id = null;

$(document).ready(function() {
  frames.start();
});

var frames = {
  socket: null,

  start: function() {
    var url = "ws://" + host + "/frames";
    frames.socket = new WebSocket(url);
    frames.socket.onmessage = function (event) {
      // look at people array
      // if len of people is greater than 0
      // save the person who is at index 0, and save their body_id
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
      current_person_id = null;
      return command;
    }
    update_current_player_id(frame);

    let current_player = null;

    for (let i = 0; i < frame.people.length; i++){
      if (frame.people[i].body_id == current_person_id) {
        current_player = frame.people[i];
      } else {
        current_player = frame.people[0];
      }
    }


    var pxy = current_player.joints[2]["pixel"];
    var chest_x = pxy["x"];
    var chest_y = pxy["y"];
    // var chest_z = pxy["y"]

    var px = (current_player.joints[8]["pixel"]["x"] - chest_x) * -1;
    var py = (current_player.joints[8]["pixel"]["y"] - chest_y) * -1;

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
      } else if (px < -100) {
        //bottomleft
        command = 4;
      }
    } 


    var rpx = (current_player.joints[15]["pixel"]["x"] - chest_x) * -1;
    var rpy = (current_player.joints[15]["pixel"]["y"] - chest_y) * -1;


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



  // get_right_wrist_command: function (frame) {
  //   var command = null;
  //   if (frame.people.length < 1) {
  //       return command;
  //   }

  //   var pelvis_x = frame.people[0].joints[0].position.x;
  //   var pelvis_y = frame.people[0].joints[0].position.y;
  //   var pelvis_z = frame.people[0].joints[0].position.z;
  //   var right_wrist_x = (frame.people[0].joints[15].position.x - pelvis_x) * -1;
  //   var right_wrist_y = (frame.people[0].joints[15].position.y - pelvis_y) * -1;
  //   var right_wrist_z = (frame.people[0].joints[15].position.z - pelvis_z) * -1;
  // }
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
  }, time_to_select)
};



function get_all_players(frame) {
  let bodyIds = [];
  for (let i = 0; i < frame.people.length; i++) {
    const bodyId = frame.people[i].body_id;
    bodyIds.push(bodyId);
  }
  return bodyIds
};


function update_current_player_id(frame) {

  let bodyIds = get_all_players(frame);
  let numIds = bodyIds.length;

  if (numIds > 0) {
    if (current_person_id == null || !bodyIds.includes(current_person_id)) {
      current_person_id = bodyIds[0];
    }
  }
};

function check_raised_hand(command) {
  // if hand is raised in either quadrant 1 or 2.
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
      check_answer(topleft), time_to_select;
  } else if (command == 1) {
      topright.style.backgroundColor = "green";
      check_answer(topright), time_to_select;
  } else if (command == 4) {
      bottomleft.style.backgroundColor = "green";
      check_answer(bottomleft), time_to_select;
  } else if (command == 3) {
      bottomright.style.backgroundColor = "green";
      check_answer(bottomright), time_to_select;
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

