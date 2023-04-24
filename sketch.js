
// Adapted from https://p5js.org/examples/interaction-snake-game.html
//
// var host = "cpsc484-03.yale.internal:8888";
var host = "127.0.0.1:4444";

let up = document.getElementById('up');
let down = document.getElementById('down');
let left = document.getElementById('left');
let right = document.getElementById('right');
let topleft = document.getElementById("topleft");
let topright = document.getElementById("topright");
let bottomleft = document.getElementById("bottomleft");
let bottomright = document.getElementById("bottomright");



$(document).ready(function() {
  frames.start();
//   twod.start();
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
        if (up) {
            // if in index.html
            console.log("change page");
            change_page("question1.html");
            // change to hand must be risen above shoulder.
            // sendWristCommand(command);
        } else if (bottomright) {
            // if in question.html
            console.log("bruh");
            select_square(command);
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
    var pelvis_x_pixel = pxy["x"];
    var pelvis_y_pixel = pxy["y"];
    
    console.log(pelvis_x_pixel, pelvis_y_pixel);

    // Normalize by subtracting the root (pelvis) joint coordinates
    var pelvis_x = frame.people[0].joints[2].position.x;
    var pelvis_y = frame.people[0].joints[2].position.y;
    var pelvis_z = frame.people[0].joints[2].position.z;
    var left_wrist_x = (frame.people[0].joints[7].position.x - pelvis_x) * -1;
    var left_wrist_y = (frame.people[0].joints[7].position.y - pelvis_y) * -1;
    var left_wrist_z = (frame.people[0].joints[7].position.z - pelvis_z) * -1;

    if (left_wrist_z < 100) {
        return command;
      }
    
    if (left_wrist_y > 0) {
        if (left_wrist_x > 150) {
            //topright
            command = 1;
        } else if (left_wrist_x < -150){
            //topleft
            command = 2;
        } else {
            command = 5;
        }
    } else if(left_wrist_y < 0) {
        if (left_wrist_x > 150) {
            //bottomright
            command = 3;
        } else if (left_wrist_x < -150){
            //bottomleft
            command = 4;
        } else {
            command = 5;
        }
    }
    console.log("command", command)
    return command;
  },


//   get_command_pixel: function (frame) {
//     console.log(frame)
//     var command = 0;
//     // if there are no people in the frame
//     if (frame.people.length < 1) {
//       return command;
//     }

    // Normalize by subtracting the root (pelvis) joint coordinates
    
    // var pelvis_y = frame.people[0].joints[2].position.y;
    // var pelvis_z = frame.people[0].joints[2].position.z;
    // var left_wrist_x = (frame.people[0].joints[7].position.x - pelvis_x) * -1;
    // var left_wrist_y = (frame.people[0].joints[7].position.y - pelvis_y) * -1;
    // var left_wrist_z = (frame.people[0].joints[7].position.z - pelvis_z) * -1;

    // if (left_wrist_z < 100) {
    //     return command;
    //   }
    
    // if (left_wrist_y > 0) {
    //     if (left_wrist_x > 150) {
    //         //topright
    //         command = 1;
    //     } else if (left_wrist_x < -150){
    //         //topleft
    //         command = 2;
    //     } else {
    //         command = 5;
    //     }
    // } else if(left_wrist_y < 0) {
    //     if (left_wrist_x > 150) {
    //         //bottomright
    //         command = 3;
    //     } else if (left_wrist_x < -150){
    //         //bottomleft
    //         command = 4;
    //     } else {
    //         command = 5;
    //     }
    // }
    // console.log("command", command)
    // return command;

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

let initialEventTime = Date.now();

// Code that triggers the initial event




function check_answer(boxID) {
    setTimeout(function () {
        if (boxID.style.backgroundColor == "red") {
            console.log("GOOD SEARCH", boxID);
            let tagID = boxID.getAttribute("id") + "tag";
            console.log("tagid", tagID);
            // console.log(boxID.getAttribute("href"));
            // setTimeout(function () {
            //     console.log("pause");
            // }, 2000);
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

function change_page(url) {
    window.location.href = url;
};




function select_square(command) {
    console.log("inside select", command);
    resetSquares()
    if (command == 5 || command == 0) {
        resetSquares(); 
    } else if (command == 2) {
        topleft.style.backgroundColor = "red";
        setTimeout(check_answer(topleft), 1000);
    } else if (command == 1) {
        topright.style.backgroundColor = "red";
        setTimeout(check_answer(topright), 1000);
    } else if (command == 3) {
        bottomleft.style.backgroundColor = "red";
        setTimeout(check_answer(bottomleft), 1000);
    } else if (command == 4) {
        bottomright.style.backgroundColor = "red";
        setTimeout(check_answer(bottomright), 1000);
    }
};

function resetSquares() {
    topleft.style.backgroundColor = "white";
    topright.style.backgroundColor = "white";
    bottomleft.style.backgroundColor = "white";
    bottomright.style.backgroundColor = "white";
};

// function resetColors() {
//     up.style.color = "black";
//     down.style.color = "black";
//     left.style.color = "black";
//     right.style.color = "black";
// };

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

// function resetColors() {
//     up.style.color = "black";
//     down.style.color = "black";
//     left.style.color = "black";
//     right.style.color = "black";
// };
// var twod = {
//   socket: null,

//   start: function() {
//     var url = "ws://" + host + "/twod";
//     twod.socket = new WebSocket(url);
//     twod.socket.onmessage = function(event) {
//       twod.show(JSON.parse(event.data));
//     }
//   },

//   show: function(twod) {
//     $('.twod').attr("src", 'data:image/pnjpegg;base64,'+twod.src);
//   }
// };


// // the snake is divided into small segments, which are drawn and edited on each 'draw' call
// let numSegments = 10;
// let direction = 'right';

// const xStart = 0; //starting x coordinate for snake
// const yStart = 250; //starting y coordinate for snake
// const diff = 10;

// let xCor = [];
// let yCor = [];

// let xFruit = 0;
// let yFruit = 0;
// let scoreElem;
// let scoreContainer = document.getElementById('score-container');
// let handContainer = document.getElementById('hand-container');

// let leftArrow = document.getElementById('left-arrow');
// let rightArrow = document.getElementById('right-arrow');
// let upArrow = document.getElementById('up-arrow');
// let downArrow = document.getElementById('down-arrow');

// let startButton = document.getElementById('start-button');
// startButton.addEventListener("click", () => {
//   window.location.reload();
// });

// function setup() {
//   let snakeCanvas = createCanvas(windowWidth/2, windowHeight/2);
//   snakeCanvas.parent("canvas-container");
//   frameRate(3);
//   stroke(255);
//   strokeWeight(10);
//   updateFruitCoordinates();

//   scoreElem = createDiv('Score = 0');
//   scoreElem.parent("score-container");
//   scoreElem.id = 'score';

//   for (let i = 0; i < numSegments; i++) {
//     xCor.push(xStart + i * diff);
//     yCor.push(yStart);
//   }
// }

// function draw() {
//   background('#b1d1fc');
//   for (let i = 0; i < numSegments - 1; i++) {
//     line(xCor[i], yCor[i], xCor[i + 1], yCor[i + 1]);
//     stroke('#000000');
//   }
//   updateSnakeCoordinates();
//   updateHandContainer();
//   checkGameStatus();
//   checkForFruit();
// }

// /*
//  The segments are updated based on the direction of the snake.
//  All segments from 0 to n-1 are just copied over to 1 till n, i.e. segment 0
//  gets the value of segment 1, segment 1 gets the value of segment 2, and so on,
//  and this results in the movement of the snake.

//  The last segment is added based on the direction in which the snake is going,
//  if it's going left or right, the last segment's x coordinate is increased by a
//  predefined value 'diff' than its second to last segment. And if it's going up
//  or down, the segment's y coordinate is affected.
// */
// function updateSnakeCoordinates() {
//   for (let i = 0; i < numSegments - 1; i++) {
//     xCor[i] = xCor[i + 1];
//     yCor[i] = yCor[i + 1];
//   }
//   switch (direction) {
//     case 'right':
//       xCor[numSegments - 1] = xCor[numSegments - 2] + diff;
//       yCor[numSegments - 1] = yCor[numSegments - 2];
//       break;
//     case 'up':
//       xCor[numSegments - 1] = xCor[numSegments - 2];
//       yCor[numSegments - 1] = yCor[numSegments - 2] - diff;
//       break;
//     case 'left':
//       xCor[numSegments - 1] = xCor[numSegments - 2] - diff;
//       yCor[numSegments - 1] = yCor[numSegments - 2];
//       break;
//     case 'down':
//       xCor[numSegments - 1] = xCor[numSegments - 2];
//       yCor[numSegments - 1] = yCor[numSegments - 2] + diff;
//       break;
//   }
// }

// function updateHandContainer() {
//   // set all arrows to white
//   leftArrow.className = 'left-arrow';
//   upArrow.className = 'up-arrow';
//   rightArrow.className = 'right-arrow';
//   downArrow.className = 'down-arrow';

//   switch (direction) {
//     case 'right':
//       rightArrow.className += ' active-right';
//       break;
//     case 'up':
//       upArrow.className += ' active-up';
//       break;
//     case 'left':
//       leftArrow.className += ' active-left';
//       break;
//     case 'down':
//       downArrow.className += ' active-down';
//       break;
//   }
// }

// /*
//  I always check the snake's head position xCor[xCor.length - 1] and
//  yCor[yCor.length - 1] to see if it touches the game's boundaries
//  or if the snake hits itself.
// */
// function checkGameStatus() {
//   if (
//     xCor[xCor.length - 1] > width ||
//     xCor[xCor.length - 1] < 0 ||
//     yCor[yCor.length - 1] > height ||
//     yCor[yCor.length - 1] < 0 ||
//     checkSnakeCollision()
//   ) {
//     noLoop();
//     const scoreVal = parseInt(scoreElem.html().substring(8));
//     scoreElem.html('Game ended! Your score was : ' + scoreVal);
//   }
// }

// /*
//  If the snake hits itself, that means the snake head's (x,y) coordinate
//  has to be the same as one of its own segment's (x,y) coordinate.
// */
// function checkSnakeCollision() {
//   const snakeHeadX = xCor[xCor.length - 1];
//   const snakeHeadY = yCor[yCor.length - 1];
//   for (let i = 0; i < xCor.length - 1; i++) {
//     if (xCor[i] === snakeHeadX && yCor[i] === snakeHeadY) {
//       return true;
//     }
//   }
// }

// /*
//  Whenever the snake consumes a fruit, I increment the number of segments,
//  and just insert the tail segment again at the start of the array (basically
//  I add the last segment again at the tail, thereby extending the tail)
// */
// function checkForFruit() {
//   point(xFruit, yFruit);
//   if (xCor[xCor.length - 1] === xFruit && yCor[yCor.length - 1] === yFruit) {
//     const prevScore = parseInt(scoreElem.html().substring(8));
//     scoreElem.html('Score = ' + (prevScore + 1));
//     xCor.unshift(xCor[0]);
//     yCor.unshift(yCor[0]);
//     numSegments++;
//     updateFruitCoordinates();
//   }
// }

// function updateFruitCoordinates() {
//   /*
//     The complex math logic is because I wanted the point to lie
//     in between 100 and width-100, and be rounded off to the nearest
//     number divisible by 10, since I move the snake in multiples of 10.
//   */

//   xFruit = floor(random(10, (width - 100) / 10)) * 10;
//   yFruit = floor(random(10, (height - 100) / 10)) * 10;
// }

// function sendWristCommand(command) {
//   switch (command) {
//     case 74:
//       if (direction !== 'right') {
//         direction = 'left';
//       }
//       break;
//     case 76:
//       if (direction !== 'left') {
//         direction = 'right';
//       }
//       break;
//     case 73:
//       if (direction !== 'down') {
//         direction = 'up';
//       }
//       break;
//     case 75:
//       if (direction !== 'up') {
//         direction = 'down';
//       }
//       break;
//   }
//   console.log(direction);
// }




// var host = "cpsc484-01.yale.internal:8888";
// var host = "http://127.0.0.1:4444"

// $(document).ready(function () {
//     frames.start();
//     frames.show();
// });

// var frames = {
//     socket: null,

//     start: function () {
//         var url = "ws://" + host + "/frames";
//         frames.socket = new WebSocket(url);
//         frames.socket.onmessage = function (event) {
//             frames.show(JSON.parse(event.data));
//         }
//     },

//     show: function (frame) {
//         console.log(frame);
//     }
// };