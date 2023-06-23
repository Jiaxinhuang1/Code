color red = color(230, 120, 120);
color orange = color(230, 200, 120);
color yellow = color(230, 220, 120);
color green = color(120, 230, 120);
color blue = color(120, 175, 230);
color purple = color(150, 120, 230);
color darkBlue = color(50, 80, 115);

color[] shades = {
  color(100, 100, 100),
  color(150, 150, 150),
  color(200, 200, 200),
  color(250, 250, 250),
};
  

void setup(){
  // set up the canvas
  size(1000, 1000);
  background(200, 230, 230);
  ellipseMode(RADIUS);
  
  // draw clouds
  blendMode(BLEND);
  noStroke();
  fill(shades[0], 200);
  ellipse(100, 900, 100, 80);
  fill(shades[2], 200);
  ellipse(50, 980, 90, 80);
  fill(shades[2], 200);
  ellipse(150, 950, 100, 80); 
  ellipse(250, 1000, 100, 80);
  fill(shades[1], 200);
  ellipse(900, 900, 100, 80);
  ellipse(950, 980, 90, 80);
  fill(shades[0], 200);
  ellipse(800, 950, 100, 80);
  ellipse(700, 1000, 100, 80);  
}

void draw(){
  // draw stick
  rectMode(CORNER);
  stroke(0);
  fill(10);
  rect(475, 330, 50, 900);
  
  // draw umbrella
  blendMode(DARKEST);
  noStroke();
  fill(red, 100);
  bezier(100, 700, 100, 100, 900, 100, 900, 700);
  fill(orange, 100);
  bezier(150, 750, 100, 100, 900, 100, 850, 750);
  fill(green, 100);
  bezier(200, 800, 100, 100, 900, 100, 800, 800);
  fill(blue, 100);
  bezier(250, 850, 100, 100, 900, 100, 750, 850);
  fill(purple,100);
  bezier(300, 900, 100, 100, 900, 100, 700, 900);
  fill(50, 50, 50, 100);
  bezier(350, 900, 100, 100, 900, 100, 650, 900);
  
  // draw random circles
  strokeWeight(3);
  stroke(darkBlue);
  fill(blue);
  ellipseMode(RADIUS);
  ellipse(200, 200, 10, 20);
  ellipse(800, 250, 5, 10);
  ellipse(500, 300, 6, 12);
  ellipse(500, 100, 15, 20);
  ellipse(400, 150, 25, 40);
  ellipse(100, 150, 5, 20);
  ellipse(200, 130, 15, 30);
  ellipse(900, 230, 25, 30);
  ellipse(800, 120, 25, 40);
  ellipse(800, 720, 25, 40);
  ellipse(100, 620, 25, 40);
}
