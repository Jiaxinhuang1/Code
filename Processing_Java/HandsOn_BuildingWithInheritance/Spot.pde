class Spot {
  float x, y, radius, speed;
  Spot(float x, float y, float radius, float speed) {
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.speed = speed;
  }
  void moveRight() {
    x += speed;
    //background(40);
    if ((x > width) || (x < 0)) {
      speed = -speed;
      background(40);
    }
  }
  void moveDown() {
    y += speed;
    //background(40);
    if ((y > height) || (y < 0)) {
      speed = -speed;
      background(40);
    }
  }
}
