function startCountdown(){
  var countdown = 3;
  var startTimer = setInterval(function(){
    document.getElementById("chordTitle").innerHTML = countdown;
    countdown--;
    if (countdown < 0){
      window.clearInterval(startTimer);
      playGame();
    }
  }, 1000);
}

function playGame(){
  chooseChord();
  timer = setInterval(function(){
    chooseChord();
    if( numberOfChords < 0){
      window.clearInterval(timer);
    }
  }, timeBetween*1000);
};

function chooseChord(){
  document.getElementById("chordsRemaining").innerHTML = numberOfChords;
  var chosenIndex = Math.floor(Math.random() * chosenChords.length );
  while (chosenChord == previousCall){
    while (chosenIndex == chosenChords.length-1){
      chosenIndex = Math.floor(Math.random() * chosenChords.length );
    }
    chosenIndex = Math.floor(Math.random() * chosenChords.length );
    chosenChord = chosenChords[chosenIndex];
  }
  previousCall = chosenChord;
  numberOfChords--;
  if (numberOfChords < 0){
    window.clearTimeout(timer);
    document.getElementById("chordsRemaining").innerHTML = "Game Over";
    document.getElementById("chord").src= "../../static/guitartrainer/chords/empty.png";
    document.getElementById("chordTitle").innerHTML = "";
  } else {
    document.getElementById("chord").src= "../../static/guitartrainer/chords/" + chosenChord + ".png";
    document.getElementById("chordTitle").innerHTML = chosenChord;
  }
}

var timer;
var previousCall = "";
var chosenChord = "";
var timeBetween = document.getElementById("timeBetweenChords").innerHTML;
var numberOfChords = document.getElementById("numberOfChords").innerHTML;
var chosenChords = document.getElementById("selectedChords").innerHTML.split(" ");
document.getElementById("chordsRemaining").innerHTML = numberOfChords;
startCountdown();
