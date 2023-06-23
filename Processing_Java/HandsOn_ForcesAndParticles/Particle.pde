class Particle {
  float x, y;
  float vx, vy;
  float r;
  color c;

  Particle(float x, float y, float vx, float vy, float r, color c) {
    this.x = x;
    this.y = y;
    this.vx = vx;
    this.vy = vy;
    this.r = r;
    this.c = c;
  }
  void applyForces(float fx, float fy) { 
    // add force (acceleration) and velocity to position
    vy += fy;
    vx += fx;
    y += vy;
    x += vx;
    // bounces back when going out of canvas
    if ((y > (height - r)) || (y < r)){
      vy = -vy;
    }
    if ((x > (width - r)) || (x < r)){
      vx = -vx;
    }
  }

  void display() {
    fill(c);
    ellipse(x, y, r, r);
  }
}
