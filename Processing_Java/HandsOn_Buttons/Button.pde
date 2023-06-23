class Button {
  PVector pos = new PVector(0, 0);
  float w;
  float h;
  color c;
  String t;
  Button (float x, float y, float w, float h, color c, String t) {
    pos.x = x;
    pos.y = y;
    this.w = w;
    this.h = h;
    this.c = c;
    this.t = t;
  }
  void changeBg()
  {
    // check if the mouse hovered over button, if so, change fill to c
    if (mouseX >= pos.x && mouseX <= pos.x + w && mouseY >= pos.y && mouseY <= pos.y + h) {
      fill(c);
      rect(pos.x, pos.y, w, h);
      // change background to c if pressed
      if (mousePressed == true && mouseButton == LEFT) {
        background(c);
      }
    } 
    // if not hover, rect filled gray
    else {
      fill(200);
      rect(pos.x, pos.y, w, h);
    }
    // write text within button
    fill(0);
    textAlign(CENTER, CENTER);
    textSize(40);
    text(t, pos.x + (w/2), pos.y + (h/2));
  }
  // function for circle button
  void displayShape()
  {
    ellipseMode(CENTER);
    // fill circle button with c if hovered
    if (mouseX >= pos.x - (w/2) && mouseX <= pos.x + (w/2) && mouseY >= pos.y - (h/2) && mouseY <= pos.y + (h/2)) {
      fill(c);
      ellipse(pos.x, pos.y, w, h);
      // create a bunch of ellipse when pressed
      if (mousePressed == true && mouseButton == LEFT) {
        for (int i=0; i < 10; i++){
          fill(random(0, 255));
          ellipse(random(0, width), random(0, height), random(50, 100), random(50, 100));
        }
      }
      // set bool to true when not pressed
      else{
        released = true;
      }
    }
    // fill circle button with gray if not hovered
    else {
      fill(200);
      ellipse(pos.x, pos.y, w, h);
    }
    // write text in center of button
    fill(0);
    textAlign(CENTER, CENTER);
    textSize(40);
    text(t, pos.x, pos.y);
  }
  // return the boolean value of released
  boolean isReleased(){
    return released;
  }
}
