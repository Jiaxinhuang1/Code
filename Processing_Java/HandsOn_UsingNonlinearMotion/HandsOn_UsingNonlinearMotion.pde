float x = 0.0;
float easing = 0.05;
float targetX = 1000;
float q = 1000;
float w = 0;
float r = 200;
float angle = 0;
float z = 0;
float c = 0;
float v = 0;

void setup() {
  size(1000, 1000);
  background(0);
  strokeWeight(5);
  stroke(150);
}

void draw() {
  //background(0);
  // ball going fast at first then slow (ease out)
  x += (targetX - x) * easing;
  ellipse(x, 200, 50, 50);
  if (x >= 990){
    x = 0;
  }
  // recreating lerp method with lerp function t = 0 - 1 (0.02 in this case)
  // produce same effect as ease out
  q = q * (1 - 0.02) + 0 * (0.02);
  if (q <=10) {
    q = 1000;
  }
  ellipse(q, 100, 50, 50);
  
  // oscillating a ball back and forth using sine
  v = r * sin(angle);
  ellipse(v + width/2, height/1.2, 100, 100);
  
  // circle a ball around point using sin and cosine
  z = r * cos(angle);
  c = r * sin(angle);
  ellipse(z + width/2, c + height/2, 100, 100);
  angle += 0.05;
  
}
