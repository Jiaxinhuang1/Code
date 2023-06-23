color skyBlue = color(150, 200, 255);
color orangeBrown = color(150, 75, 0);
color mintGreen = color(220, 230, 200);
color lightPink = color(230, 220, 220);
color gray = color(10, 10, 10);
color lightBrown = color(200, 165, 120);
color brown = color(150, 130, 100);
color lightPurple = color(234, 234, 234);
color shadowGray = color(50, 50, 50);

void setup(){
  // set background and sky blue color
  size(1000, 1000);
  background(skyBlue);
}

void draw(){
  // draws the table that holds the boba
  strokeWeight(15);
  line(0, 700, 1000, 700);
  fill(orangeBrown);
  rect(0, 700, 1000, 300);
  
  // draws the straw
  stroke(0);
  fill(mintGreen);
  strokeWeight(5);
  quad(550, 0, 600, 0, 530, 400, 480, 400);
  quad(500, 400, 550, 400, 480, 790, 430, 785);
  //quad(550, 0, 600, 0, 530, 790, 480, 785);
  
  // draws the boba cup top
  fill(lightPink, 150);
  strokeWeight(3);
  ellipse(500, 80, 88, 10);
  strokeWeight(5);
  bezier(300, 250, 300, 0, 700, 0, 700, 250);
  fill(lightPink, 220);
  quad(300, 250, 700, 250, 700, 300, 300, 300);
  
  // draws boba circles
  ellipseMode(RADIUS);
  noStroke();
  fill(gray);
  ellipse(400, 600, 20, 20);
  ellipse(420, 680, 20, 20);
  ellipse(450, 700, 20, 20);
  ellipse(500, 770, 20, 20);
  ellipse(500, 660, 20, 20);
  ellipse(530, 700, 20, 20);
  ellipse(450, 770, 20, 20);
  ellipse(550, 770, 20, 20);
  ellipse(560, 730, 20, 20);
  ellipse(460, 730, 20, 20);
  ellipse(570, 690, 20, 20);
  ellipse(550, 670, 20, 20);
  ellipse(510, 630, 20, 20);
  ellipse(430, 760, 20, 20);
 
  // draws milk tea inside cup
  noStroke();
  fill(lightBrown, 150);
  quad(340, 400, 660, 400, 590, 790, 410, 790);
  
  //draws the boba cup bottom
  stroke(0);
  fill(lightPurple, 150);
  strokeWeight(5);
  quad(300, 300, 700, 300, 600, 800, 400, 800);
  
  // draws the sticker
  noStroke();
  fill(brown);
  triangle(500, 450, 600, 550, 400, 550);
  
  // draws the shadow
  noStroke();
  fill(shadowGray, 100);
  quad(400, 800, 600, 800, 800, 1000, 500, 1000);
}
