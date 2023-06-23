class Button {
  PVector pos = new PVector(0, 0);
  float w;
  float h;
  color c;
  String t;
  boolean isChecked;
  boolean isPressed;
  Button (float x, float y, float w, float h, color c, String t) {
    pos.x = x;
    pos.y = y;
    this.w = w;
    this.h = h;
    this.c = c;
    this.t = t;
    isChecked = false;
    isPressed = false;
  }

  void changeBg(color col)
  {
    // check if the mouse hovered over button, if so, change fill to c
    if (mouseX >= pos.x && mouseX <= pos.x + w && mouseY >= pos.y && mouseY <= pos.y + h) {
      isPressed = !isPressed;
      fill(col);
      rect(pos.x, pos.y, w, h);
      // change background to c if pressed
      if (mousePressed == true && mouseButton == LEFT) {
        background(col);
      }
    } 
    // if not hover, rect filled gray
    else {
      fill(200);
      rect(pos.x, pos.y, w, h);
      // write text within button
      fill(0);
      textAlign(CENTER, CENTER);
      textSize(40);
      text(t, pos.x + (w/2), pos.y + (h/2));
    }
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
        for (int i=0; i < 10; i++) {
          fill(random(0, 255));
          ellipse(random(0, width), random(0, height), random(50, 100), random(50, 100));
        }
      }
      // set bool to true when not pressed
      else {
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

  void createShapes(String s) {
    // check if the mouse hovered over button, if so, change fill to c
    if (mouseX >= pos.x && mouseX <= pos.x + w && mouseY >= pos.y && mouseY <= pos.y + h) {
      fill(100);
      rect(pos.x, pos.y, w, h);
      // change background to c if pressed
      if (mousePressed == true && mouseButton == LEFT) {
        // problem I was having is to get it to uncheck
        if (!isChecked) {
          isChecked = true;
        } else {
          isChecked = false;
        }
        //print(isChecked);
        if (isChecked()) {
          fill(100);
          ellipse(pos.x + w/2, pos.y + h/2, w/2, h/2);
          if (s == "ellipse") {
            //ellipse(pos.x + 600, pos.y + 100, 200, 200);
          } else if (s == "rect") {
            //rect(pos.x + 500, pos.y, 200, 200);
          } else {
            println("Nothing");
          }
        } else {
          fill(100);
          rect(pos.x, pos.y, w, h);
        }
      }
    }
    // if not hover, rect filled gray
    else {
      fill(200, 240, 200);
      rect(pos.x, pos.y, w, h);
    }
  }

  void showChecked() {
    rect(pos.x, pos.y, w - 10, h - 10);
  }

  // return the boolean value of released
  boolean isReleased() {
    return released;
  }
  boolean isChecked() {
    return isChecked;
  }
  boolean isPressed() {
    return isPressed;
  }
  color bgColor() {
    return c;
  }
}
