function playGame(){

  console.log( timeBetween );
  console.log( numberOfChords );
  timer = setInterval(chooseChord, timeBetween*1000);
};

function chooseChord(){
  var chosenIndex = Math.floor(Math.random() * chosenChords.length );
  while (chosenChord === previousCall){
    while (chosenIndex == chosenChords.length-2){
      chosenIndex = Math.floor(Math.random() * chosenChords.length );
    }
    chosenIndex = Math.floor(Math.random() * chosenChords.length );
    chosenChord = chosenChords[chosenIndex];
  }
  previousCall = chosenChord;
  console.log(chosenChord);
  if (--numberOfChords < 0){
    window.clearTimeout(timer);
    console.log("Game Over");
  } else {
    document.getElementById("chord").src= "static/guitartrainer/chords/" + chosenChord + ".png";
  }
}
var timer;
var previousCall = "";
var chosenChord = "";
var timeBetween = document.getElementById("timeBetweenChords").innerHTML;
var numberOfChords = document.getElementById("numberOfChords").innerHTML;
var chosenChords = document.getElementById("selectedChords").innerHTML.split(", ");
playGame();
