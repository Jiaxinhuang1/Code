void setup(){
  // sets canvas size and color
  size(1000, 1000);
  background(170, 221, 234);
}

void draw(){
  // draw cube
  rectMode(CENTER); //default mode for rects
  strokeWeight(10);
  stroke(25, 85, 100);
  fill(80, 140, 150);
  rect(400, 400, 500, 500);
  // draw circle inside cube
  noStroke();
  fill(200, 180, 130);
  ellipseMode(RADIUS);
  ellipse(250, 200, 100, 100);
  fill(250, 180, 130);
  ellipse(275, 400, 100, 100);
  fill(200, 110, 130);
  ellipse(270, 600, 100, 100);
  fill(200, 110, 200);
  ellipse(475, 350, 150, 150);
  fill(200, 180, 250);
  ellipse(675, 350, 50, 50);
  
  // continue cube
  stroke(25, 85, 100);
  fill(100, 180, 200);
  rect(600, 600, 500, 500);
  line(350, 350, 150, 150);
  line(350, 850, 150, 650);
  line(850, 350, 650, 150);
  // draw circle outside cube
  noFill();
  ellipseMode(CORNERS);
  ellipse(-100, -100, 100, 100);
  ellipseMode(CENTER);
  ellipse(1000, 1000, 150, 150);
  ellipse(1000, 0, 150, 150);
  ellipse(0, 1000, 150, 150);
  // center point for front
  stroke(25, 85, 100);
  strokeWeight(50);
  point(600, 600);

}
