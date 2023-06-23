class Rain extends Precipitation {
  // parameters the same as the precipitation superclass
  Rain(float x, float y, float radius, float speed, float size) {
    super(x, y, radius, speed, size);
  }
  // show the rain
  void showRain() {
    stroke(100, 120, 130);
    strokeWeight(random(3, 7));
    line (x, y, x, y + random(10, 20));
  }
}
