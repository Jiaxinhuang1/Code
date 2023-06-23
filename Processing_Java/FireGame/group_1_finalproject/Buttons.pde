class Buttons {
  PVector pos = new PVector(0, 0);
  float w;
  float h;
  color c;
  String t;
  Buttons (float x, float y, float w, float h, color c, String t) {
    pos.x = x;
    pos.y = y;
    this.w = w;
    this.h = h;
    this.c = c;
    this.t = t;
  }
  // function that does something based on command when button is pressed
  void buttonPressed(String command)
  {
    // check if the mouse hovered over button, if so, change fill to c
    if (mouseX >= pos.x && mouseX <= pos.x + w && mouseY >= pos.y && mouseY <= pos.y + h) {
      fill(c, 200);
      rect(pos.x, pos.y, w, h);
      // change background to c if pressed
      if (mousePressed == true && mouseButton == LEFT) {
        if (!buttonClick.isPlaying() && !isMuted) {
          buttonClick.play(1, volume);
        }
        // check then command and change scene accordingly
        if (command == "startGame")
        {
          menuMusic.stop();
          scene = 2;
        }
        if (command == "restartGame") {
          //gameLose.stop();
          scene = 2;
        }
        if (command == "exitGame") {
          exit();
        }
        if (command == "resumeGame") {
          scene = 2;
        }
        if (command == "returnMenu") {
          scene = 1;
        }
        if (command == "openCredits") {
          scene = 6;
        }
        if (command == "openSettings") {
          scene = 7;
        }
        if (command == "muteSound") {
          isMuted = true;
          //print(isMuted);
        }
        if (command == "unmuteSound") {
          isMuted = false;
        }
      }
    } 
    // if not hover, rect filled gray
    else {
      fill(150);
      rect(pos.x, pos.y, w, h);
    }
    // write text within button
    fill(0);
    textAlign(CENTER, CENTER);
    textSize(50);
    text(t, pos.x + (w/2), pos.y + (h/2));
  }
}
