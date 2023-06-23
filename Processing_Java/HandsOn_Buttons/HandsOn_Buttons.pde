public Boolean released = false;
Button r_button;
Button b_button;
Button g_button;
Button circle;
void setup() {
  size(1000, 1000);
  background(0);
  strokeWeight(5);
  // create buttons that changes color of background when pressed
  r_button = new Button(50, 0, 300, 100, color(220, 100, 100), "Fill Red");
  b_button = new Button(350, 0, 300, 100, color(100, 100, 220), "Fill Blue");
  g_button = new Button(650, 0, 300, 100, color(100, 220, 100), "Fill Green");
  // create buttons that draw a bunch of circles when pressed
  circle= new Button(500, 500, 300, 300, color(100, 100, 100), "Circle");
}

void draw() {
  r_button.changeBg();
  b_button.changeBg();
  g_button.changeBg();
  circle.displayShape();

  //Shows text
  fill(255);
  textAlign(CENTER, CENTER);
  textSize(30);
  text("Press Rect Buttons on Top to Change Background Color", 500, 900);
  text("Hold Circle Button to Spawn Ellipses", 500, 950);
}

// when the mouse is released change the background to black
void mouseReleased() {
  if (circle.isReleased()) {
    released = false;
    background(0);
  }
}
