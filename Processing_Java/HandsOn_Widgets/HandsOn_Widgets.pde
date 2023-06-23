public Boolean released = false;
Button r_button;
Button b_button;
Button g_button;
Button rectToggle;
Button circleToggle;
Scrollbar scrollbar;
void setup() {
  size(1000, 1000);
  background(100);
  strokeWeight(5);

  scrollbar = new Scrollbar(700, 50, 200, 800);

  // create buttons that changes color of background when pressed
  r_button = new Button(50, 0, 300, 100, color(220, 100, 100), "Fill Red");
  b_button = new Button(350, 0, 300, 100, color(100, 100, 220), "Fill Blue");
  g_button = new Button(650, 0, 300, 100, color(100, 220, 100), "Fill Green");
  rectToggle = new Button(100, 200, 200, 200, color(100), "");
  circleToggle = new Button(100, 500, 200, 200, color(100), "");
}

void draw() {
  //fill(scrollbar.getPos());
  /*
  if (r_button.isPressed()) {
   g_button.isPressed = false;
   b_button.isPressed = false;
   background(r_button.bgColor());
   } else if (g_button.isPressed()) {
   r_button.isPressed = false;
   b_button.isPressed = false;
   background(g_button.bgColor());
   } else if (b_button.isPressed()) {
   r_button.isPressed = false;
   g_button.isPressed = false;   
   background(b_button.bgColor());
   }
   */
  println(scrollbar.getPos());
  r_button.changeBg(color(scrollbar.getPos(), 50, 50));
  b_button.changeBg(color(50, 50, scrollbar.getPos()));
  g_button.changeBg(color(50, scrollbar.getPos(), 50));
  rectToggle.createShapes("rect");
  circleToggle.createShapes("ellipse");

  scrollbar.update();
  scrollbar.display();
  if (rectToggle.isChecked()) {
    fill(150);
    ellipse(200, 300, 100, 100);
    fill(scrollbar.getPos(), 100, 100);
    rect(500, 200, 200, 200);
  }
  if (circleToggle.isChecked()) {
    fill(150);
    ellipse(200, 600, 100, 100);
    fill(100, scrollbar.getPos(), 100);
    ellipse(600, 600, 200, 200);
  }

  //Shows text
  fill(255);
  textAlign(CENTER, CENTER);
  textSize(25);
  text("Press Rect Buttons on Top to Change BG Color (Saturation change by slider)", 500, 900);
  text("Check the box in order to adjust saturation of rect/circle", 500, 950);
}
