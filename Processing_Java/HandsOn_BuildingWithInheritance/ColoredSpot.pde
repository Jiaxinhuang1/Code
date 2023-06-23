class ColoredSpot extends Spot {
  color c;
  ColoredSpot(float x, float y, float radius, float speed, color c) {
    super(x, y, radius, speed);
    this.c = c;
  }
  void colors() {
    fill(c);
  }
}
