void setup() {
  // Set canvas size
  size(1000, 1000);
}

void draw() {
  // keyboard input: 1 - circle, 2 - rect, 3 - triange in position of mouse
  if (keyPressed) {
    stroke(0);
    fill(random(0, 255), random(0, 255), random(0, 255));
    if (key == '1')
    {
      ellipse(mouseX, mouseY, 100, 100);
    } else if (key == '2')
    {
      rect(mouseX, mouseY, 100, 100);
    } else if (key == '3')
    {
      triangle(mouseX, mouseY, mouseX + 100, mouseY + 100, mouseX - 100, mouseY + 100);
    }
  }
  // Mouse Press functionality in draw 
  // (left click black, right click white, center click gray)
  if (mousePressed) {
    if (mouseButton == LEFT) {
      background(0);
    } else if (mouseButton == RIGHT) {
      background(255);
    } else if (mouseButton == CENTER) {
      background(100);
    }
  }
}

// same functionality as the mousePress variable in draw
void mousePressed() {
  if (mouseButton == LEFT) {
    background(0);
  } else if (mouseButton == RIGHT) {
    background(255);
  } else if (mouseButton == CENTER) {
    background(100);
  }
}

// draws a random colored point in position of mouse at all times (leaves a trial)
void mouseMoved() {
  strokeWeight(20);
  stroke(random(0, 255), random(0, 255), random(0, 255));
  point(mouseX, mouseY);
}

// same functionality as keyPressed variable in draw
void keyPressed() {
  noStroke();
  fill(random(0, 255), random(0, 255), random(0, 255));
  if (key == '1')
  {
    ellipse(mouseX, mouseY, 100, 100);
  } else if (key == '2')
  {
    rect(mouseX, mouseY, 100, 100);
  } else if (key == '3')
  {
    triangle(mouseX, mouseY, mouseX + 100, mouseY + 100, mouseX - 100, mouseY + 100);
  }
}
