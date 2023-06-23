class Fish extends RunOff {
  color c2;
  PShape fish, head, body, f1, f2, f3;
  float start = 950, end = 1050;
  boolean right = true;
  Fish(float x, float y, color c, float len, float wid, color c2) {
    super(x, y, c, len, wid);
    this.c2 = c2;
  }
  
  // draws the fish based on x, y, radius, and color
  void display() {
    fish = createShape(GROUP);
    head = createShape(TRIANGLE, 10, 10, 10, 30, 20, 20);
    body = createShape(ELLIPSE, 0, 20, 30, 20);
    f1 = createShape(TRIANGLE, 10, 10, 0, 0, 0, 10);
    f2 = createShape(TRIANGLE, 0, 30, 10, 30, 0, 40);
    f3 = createShape(TRIANGLE, -10, 20, -25, 0, -25, 35);
    
    head.setFill(c);
    body.setFill(c2);
    f1.setFill(c);
    f2.setFill(c);
    f3.setFill(c);
    noStroke();
    
    fish.addChild(body);
    fish.addChild(head);
    fish.addChild(f1);
    fish.addChild(f2);
    fish.addChild(f3);
    shape(fish, x, y);
  }
  
  //makes the fish swim back and forth
  void swim() {
    if (x == 1200) {
      x = 950;
    }
    if (x < 1200) {
      x+= 2;
    } 
  }
}
