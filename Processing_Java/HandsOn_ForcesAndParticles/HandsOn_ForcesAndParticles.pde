float y = 0.0;
float r = 50.0;
float vel = 0.0;
float accel = 0.1;
float friction = 0.999;
color c = color(random(0, 255), random(0, 255), random(0, 255));

Particle [] parts = new Particle[100];

void setup() {
  size(1000, 1000);
  ellipseMode(RADIUS);
  noStroke();
  // create the 100 particle objects and set random position/radius
  for (int i = 0; i < parts.length; i++) {
    parts[i] = new Particle(random(0, width), random(0, height), 0, 0, random(10, 50), c);
  }
}

void draw() {
  background(0);
  // create ellipse falling from top of screen to bottom at increasing speed
  fill(255);
  ellipse(250, y, r, r);
  vel += accel;
  // adding friction and restitution to slow down and create realistic bounce
  vel *= friction;
  y += vel;
  // bounces back when hit the ground
  if (y > (height - r)) {
    vel = -vel;
  }
  
  // apply forces and show the ellipses in the parts list
  for (int i = 0; i < parts.length; i++) {
    parts[i].applyForces(random(-0.1, 0.1), random(-0.1, 0.1));
    parts[i].display();
  }
}
