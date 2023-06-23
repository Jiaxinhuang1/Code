Spring spring1;
Spring spring2;
Spring spring3;
Spring spring4;

PVector location;
PVector forces;
PVector velocity;
PVector acceleration;

float m = 1.0;
float rx = 500;
float ry = 500;
float ks = 0.01;
float kd = 0.01;
float time = 0.20;

void setup() {
  size(1000, 1000);
  strokeWeight(10);

  spring1 = new Spring(new PVector(200, 200), new PVector(0, 0), new PVector(0, 0), 100, 100);
  spring2 = new Spring(new PVector(400, 400), new PVector(0, 0), new PVector(0, 0), 300, 300);
  spring3 = new Spring(new PVector(600, 600), new PVector(0, 0), new PVector(0, 0), 700, 700);
  spring4 = new Spring(new PVector(800, 800), new PVector(0, 0), new PVector(0, 0), 900, 900);
}
void draw() {
  background(210);
  rectMode(CENTER);

  spring1.applyForces(0.05, 0.1);
  spring2.applyForces(0.5, 0.1);
  spring3.applyForces(0.1, 0.1);
  spring4.applyForces(0.4, 0.2);
}

class Spring {
  PVector location;
  PVector velocity;
  PVector acceleration;
  float rx;
  float ry;

  Spring(PVector location, PVector velocity, PVector acceleration, float rx, float ry) {
    this.location = location;
    this.velocity = velocity;
    this.acceleration = acceleration;
    this.rx = rx;
    this.ry = ry;
  }
  void applyForces(float fx, float fy) { 
    rectMode(CENTER);
    fx = -((ks * (location.y - ry)) + kd * velocity.y);
    fy = -((ks * (location.x - rx)) + kd * velocity.x);
    acceleration.x = fx/m;
    acceleration.y = fy/m;
    velocity.x = velocity.x + acceleration.x * time;
    velocity.y = velocity.y + acceleration.y * time;
    location.x += velocity.x;
    location.y += velocity.y;
    rect(rx, ry, 40, 40);
    line(location.x, location.y, rx, ry);
    ellipse(location.x, location.y, 100, 100);
  }
}
