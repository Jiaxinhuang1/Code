class TwoSpots extends Spot {
  TwoSpots(float x, float y, float radius, float speed) {
    super(x, y, radius, speed);
  }
  void display() {
    ellipse(x, y, radius, radius);
    ellipse(x, y + radius + 10, radius + 20, radius + 20);
    ellipse(x, y - radius - 10, radius + 20, radius + 20);
  }

  void displayVert() {
    ellipse(x, y, radius, radius);
    ellipse(x + radius + 10, y, radius + 20, radius + 20);
    ellipse(x - radius - 10, y, radius + 20, radius + 20);
  }
}
