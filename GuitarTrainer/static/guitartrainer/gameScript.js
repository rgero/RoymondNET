function playGame(){

  console.log( timeBetween );
  console.log( numberOfChords );
  timer = setInterval(function(){
    chooseChord();
  }, 1000);
};

function chooseChord(){
  console.log("called");
  document.getElementById("chordsRemaining").innerHTML = numberOfChords;
  var chosenIndex = Math.floor(Math.random() * chosenChords.length );
  while (chosenChord == previousCall){
    while (chosenIndex == chosenChords.length-2){
      chosenIndex = Math.floor(Math.random() * chosenChords.length );
    }
    chosenIndex = Math.floor(Math.random() * chosenChords.length );
    chosenChord = chosenChords[chosenIndex];
  }
  previousCall = chosenChord;
  console.log(chosenChord);
  numberOfChords--;
  if (numberOfChords < 0){
    window.clearTimeout(timer);
    document.getElementById("chordsRemaining").innerHTML = "Game Over";
  } else {
    document.getElementById("chord").src= "../../static/guitartrainer/chords/" + chosenChord + ".png";
    document.getElementById("chordTitle").innerHTML = chosenChord;
  }
}

var timer;
var previousCall = "";
var chosenChord = "";
var timeBetween = 1; //document.getElementById("timeBetweenChords").innerHTML;
var numberOfChords = 10; //document.getElementById("numberOfChords").innerHTML;
var chosenChords = ['A','B','C'];
playGame();
