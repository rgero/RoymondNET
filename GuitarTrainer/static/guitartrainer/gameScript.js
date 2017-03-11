function playGame(){

  console.log( timeBetween );
  console.log( numberOfChords );
  timer = setInterval(chooseChord(), timeBetween*1000);
};

function chooseChord(){
  console.log("called");
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
var timeBetween = 10; //document.getElementById("timeBetweenChords").innerHTML;
var numberOfChords = 10; //document.getElementById("numberOfChords").innerHTML;
var chosenChords = ['A','B','C'];
playGame();
