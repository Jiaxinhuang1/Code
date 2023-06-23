int angle = 0;
void setup() {
  size(1000, 1000);
  background(210, 220, 240);
  strokeWeight(2);
}

void draw() {
  //background(210, 220, 240);
  
  // Translate to origin then draw rect on upper left corner
  // green rect
  pushMatrix();
  fill(50, 100, 50);
  translate(width/2, height/2);
  rect(0, 0, 200, 200);
  popMatrix();
  
  // Scale then translate to origin (blue rect)
  pushMatrix();
  fill(50, 50, 100);
  scale(0.5);
  translate(width/2, height/2);
  rect(0, 0, 200, 200);
  popMatrix();
  
  // Scale, Rotate, then Translate to origin (random black-white rect)
  pushMatrix();
  fill(random(0, 255));
  scale(0.75);
  rotate(radians(angle));
  translate(width/2, height/2);
  rect(0, 0, 200, 200);
  popMatrix();
  
  // Scale, translate, then rotate on screen origin (rotating yellow rect)
  pushMatrix();
  fill(100, 100, 50);
  scale(0.25);
  translate(width/2, height/2);
  rotate(radians(-angle));
  rect(0, 0, 200, 200);
  popMatrix();

  // Translate, Rotate, then scale (rotating red/blue-green rect on bottom right)
  pushMatrix();
  fill(random(0, 255), 100, 100);
  translate(width/2 + 300, height/2 + 300);
  rotate(radians(angle * 30));
  scale(1.25);
  rect(0, 0, 200, 200);
  // Top Version (rotating blue/green rect on top right)
  popMatrix();
  pushMatrix();
  fill(100, 100, random(0, 255));
  translate(width/2 + 300, height/2 - 300);
  rotate(radians(-angle * 15));
  scale(0.75);
  rect(0, 0, 200, 200);
  popMatrix();

  angle++;
}
