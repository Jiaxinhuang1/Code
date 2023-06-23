class Sun {
  // declares variables for parameter
  float x, y, angle, radius, speed;
  PShape sun, ray1, ray2, ray3, ray4, ray5, ray6, main;
  Sun(float x, float y, float radius, float angle, float speed) {
    this.x = x;
    this.y = y;
    this.angle = angle;
    this.radius = radius;
    this.speed = speed;
  }
  // displays the look of the sun and assign rotation and scale
  void display() {
    pushMatrix();
    // setup the foundation
    translate(800, 150);
    rotate(radians(angle));
    scale(speed);
    rectMode(CENTER);
    strokeWeight(10);
    // creates group of PShapes
    sun = createShape(GROUP);
    fill(230, 225, 90);
    // creating the main circle
    main = createShape(ELLIPSE, x, y, radius, radius);
    fill(200, 195, 80);
    // creating the rays
    ray1 = createShape(RECT, x, y, 300, 20);
    ray2 = createShape(RECT, x, y, 20, 300);
    pushMatrix();
    fill(174, 170, 65);
    // creating the small ashes
    ray3 = createShape(ELLIPSE, x + radius/2, y + radius/2, 30, 30);
    ray4 = createShape(ELLIPSE, x - radius/2, y + radius/2, 30, 30);
    ray5 = createShape(ELLIPSE, x + radius/2, y - radius/2, 30, 30);
    ray6 = createShape(ELLIPSE, x - radius/2, y - radius/2, 30, 30);
    popMatrix();
    // adding to group
    sun.addChild(ray1);
    sun.addChild(ray2);
    sun.addChild(main);
    sun.addChild(ray3);
    sun.addChild(ray4);
    sun.addChild(ray5);
    sun.addChild(ray6);
    shape(sun);
    popMatrix();
  }

  // updates the parameters in which the scale and rotation requires
  void update() {
    angle += 1;
    radius -= speed;
    if ((radius < 100) || (radius > 180)) {
      speed = -speed;
    }
  }
}
