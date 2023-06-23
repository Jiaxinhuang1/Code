class Precipitation {
  // main class that controls rain cloud actions
  float x, y, radius, speed, size;
  Precipitation(float x, float y, float radius, float speed, float size) {
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.speed = speed;
    this.size = size;
  }
  // increase/decrease radius with certain size speed
  void sizeTransform() {
    radius -= size;
    if ((radius < 100) || (radius > 180)) {
      size = -size;
    }
    //background(185, 215, 240);
  }
  // make the rain fall
  void fall() {
    y += speed;
    if (y > height) {
      y = random(50, 100);
    }
  }
}
