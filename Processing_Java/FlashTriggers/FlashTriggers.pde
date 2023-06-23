PVector location;
PVector velocity;
PVector gravity; 

void setup() {
  size(1280, 720);
  outside();
  squaresRandom();
  location = new PVector(0, 0);
  velocity = new PVector(1.5, 2.1);
  gravity = new PVector(0, 0.2);
}

void draw() {
  location.add(velocity);
  velocity.add(gravity);
  if ((location.x > 1280) || (location.x < 0)) {
    velocity.x = velocity.x * -1;
  }
  if ((location.y > 720)|| (location.y<0)) {
    velocity.y = velocity.y * -0.95; 
    location.y = 720;
  }
  if (mousePressed) {
    velocity.y=velocity.y-0.50;
  }
  if (keyPressed) {
    velocity.y=velocity.y+0.50;
  }

  stroke(255);
  strokeWeight(2);
  fill(mouseX/3, mouseY/3, 100);
  ellipse(location.x, location.y, 50, 50);
}

int width;
int height;

void squaresRandom() {
  int x=0;
  while (x<40) {
    color r=int(random(100, 255));
    color g=int(random(100, 255));
    color b=int(random(100, 255));
    stroke(int(random(255)));
    fill(r, g, b);
    square(int(random(1280)), int(random(720)), int(random(10, 300)));
    x++;
  }
}
void outside() {
  for (int a=0; a<1280; a+=15) {
    for (int b=0; b<720; b+=15) {
      fill(a/4, b/4, 255, 255);
      stroke(255);
      square(a, b, 25);
    }
  }
}
