class Bubble {
  float x, y;
  float vx, vy;
  float r;
  color c;
  float alpha = 200;

  Bubble(float x, float y, float vx, float vy, float r, color c) {
    this.x = x;
    this.y = y;
    this.vx = vx;
    this.vy = vy;
    this.r = r;
    this.c = c;
  }
  // add force (acceleration), velocity, and gravity to position
  void applyForces(float fx, float fy) { 
    // if the mouse is inside the ocean, move the bubble towards the mouse
    if (mouseX > 0 && mouseX < width && mouseY > 200 && mouseY < height) {
      PVector mouse = new PVector(mouseX, mouseY);
      mouse.x = mouseX - x;
      mouse.y = mouseY - y;
      mouse.setMag(0.8);
      fy = mouse.x;
      fy = mouse.y;
    }
    // change position based on velocity and acceleration
    vy += fy;
    vx += fx;
    y += vy;
    x += vx;
    // decrease alpha to transparency
    alpha -= 1;
  }

  // draws the bubbles as two ellipses
  void display() {
    noStroke();
    fill(c, alpha);
    ellipse(x, y, r, r);
    fill(220, 240, 240, alpha);
    ellipse(x - r/10, y - r/10, r-30, r-30);
  }
  
  // decrease the radius to make the bubbles gradually disappear
  void disappear(){
    r -= 5;
    if (r <= 0){
      r = 0;
    }
  }

  // returns boolean to kill the bubble when out of ocean or when transparent
  boolean isAlive() {
    if ((alpha < 0) || (x < 0) || (x > 1000) || (y < 250) || (y > 1000) || (r == 0)) {
      return false;
    }
    else {
      return true;
    }
  }
}
