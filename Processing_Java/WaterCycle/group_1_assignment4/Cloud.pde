class Cloud extends Precipitation {
  color c;
  PShape clouds;
  PShape cloud1;
  PShape cloud2;
  PShape cloud3;
  // Parameters same as precipitation super class but with additional color variable
  Cloud(float x, float y, float radius, float speed, float size, color c) {
    super(x, y, radius, speed, size);
    this.c = c;
  }
  // creates group of PShapes
  void display() {
    noStroke();
    fill(c);
    clouds = createShape(GROUP);
    cloud1 = createShape(ELLIPSE, x, y, radius, radius);
    cloud2 = createShape(ELLIPSE, x - radius/4 *3, y, radius - 10, radius - 10);
    cloud3 = createShape(ELLIPSE, x + radius/4 *3, y, radius - 20, radius - 20);
    // assigning  circles to main group
    clouds.addChild(cloud1);
    clouds.addChild(cloud2);
    clouds.addChild(cloud3);
    shape(clouds);
  }
  // increase/decrease radius with certain size speed
  void sizeTransform() {
    radius -= size;
    if ((radius < 100) || (radius > 180)) {
      size = -size;
    }
  }
}
