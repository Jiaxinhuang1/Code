void setup(){
  // set background
  size(1000, 1000);
  background(150, 100, 100);
}

void draw(){
  // draw table
  fill(50);
  quad(200, 800, 0, 1000, 1000, 1000, 800, 800);
  fill(100);
  quad(300, 900, 100, 1000, 900, 1000, 700, 900);
  // draw legs
  noFill();
  strokeWeight(10);
  bezier(650, 600, 500, 340, 800, 760, 500, 920);
  bezier(350, 600, 200, 340, 500, 760, 200, 920);
  // draw body outline
  fill(150);
  ellipse(500, 500, 500, 500);
  line(100, 400, 250, 500);
  line(900, 400, 750, 500);
  // draw eyes
  strokeWeight(50);
  point(400, 450);
  point(600, 450);
  // draw hat
  strokeWeight(10);
  fill(150);
  triangle(500, 0, 700, 300, 300, 300);
  fill(100);
  ellipse(500, 200, 100, 100);
  //draw mouth
  noFill();
  arc(500, 550, 300, 200, 0, PI);
  // draw eyebrows
  fill(200);
  rect(350, 350, 100, 25);
  rect(550, 350, 100, 25);
  // draw nose
  triangle(500, 500, 500, 550, 550, 550);
  
}
