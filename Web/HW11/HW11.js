var seconds = 0
var puzzle_idx = Math.trunc(Math.random() * 3) + 1
var path = "329E.HW11.images/puzzle" + puzzle_idx +"/img" + puzzle_idx + "-"
function LoadPuzzle(){
    timer = setInterval(startTimer, 1000)
    startTimer()
    //var puzzle_idx = Math.trunc(Math.random() * 3) + 1
    timeCount = document.getElementById("timeCount")
    document.getElementById("Title").innerHTML = "Jigsaw Puzzle " + puzzle_idx
    //var path = "329E.HW11.images/puzzle" + puzzle_idx +"/img" + puzzle_idx + "-"
    var img_idx = Array.from({length: 12}, (_, i) => i + 1)
    shuffle(img_idx)
    for (let i = 1; i <= img_idx.length; i ++){
        let id = "img" + i.toString()
        document.getElementById(id).src = path + img_idx[i - 1] + ".jpg"
    }
}

//helper function to shuffle images
function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

function Grabber(event) {

   // Set the global variable for the element to be moved
   theElement = event.currentTarget;

   // Determine the position of the word to be grabbed, first removing the units from left and top
   posX = parseInt(theElement.style.left);
   posY = parseInt(theElement.style.top);

   // Compute the difference between where it is and where the mouse click occurred
   diffX = event.clientX - posX;
   diffY = event.clientY - posY;

   // Now register the event handlers for moving and dropping the word
   document.addEventListener("mousemove", mover, true);
   document.addEventListener("mouseup", dropper, true);

}

// The event handler function for moving the word
function mover(event) {
   // Compute the new position, add the units, and move the word
   theElement.style.left = (event.clientX - diffX) + "px"
   theElement.style.top = (event.clientY - diffY) + "px"
   theElement.style.cursor = "pointer"
}

// The event handler function for dropping the word
function dropper(event) {
   // Unregister the event handlers for mouseup and mousemove
   document.removeEventListener("mouseup", dropper, true)
   document.removeEventListener("mousemove", mover, true)
   // if ((theElement.getAttribute("src") == path + "1.jpg") 
   //  && (parseInt(theElement.style.top) < -315)
   //  && (parseInt(theElement.style.top) > -335))  {
   //      alert(parseInt(theElement.style.left))
   // }
}

// helper function to start timer
function startTimer() {
    timeCount.innerHTML = "Time: " + seconds
    seconds ++
}

// function called when done button pressed
function StopTimer(){
    //alert(document.getElementById("img1").getAttribute("src"))
    clearInterval(timer)
}