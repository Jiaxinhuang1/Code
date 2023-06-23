Stand stand;
Swing swing1;
Swing swing2;
Stand stand2;
Swing swing3;
Swing swing4;
Stand stand3;
Swing swing5;
Swing swing6;

Roundabout r1;
Roundabout r2;

Ball b;
Children ch1;
Children ch2;

void setup() {
  size(1000, 1000, P3D);
  // Makes three set of swing objects with different location and angle movements
  stand = new Stand (300, 800, -300);
  swing1 = new Swing(400, 650, 400, 850, 50, 0, 0);
  swing2 = new Swing(600, 650, 600, 850, 50.3, 0, 0);
  stand2 = new Stand (800, 800, -300);
  swing3 = new Swing(900, 650, 900, 850, -50.4, 0, 0);
  swing4 = new Swing(1100, 650, 1100, 850, 50, 0, 0);
  stand3 = new Stand (-200, 800, -300);
  swing5 = new Swing(-100, 650, -100, 850, 49.8, 0, 0);
  swing6 = new Swing(100, 650, 100, 850, 50.1, 0, 0);
  
  // Makes roundabouts with x position,y position,z position, 
  //speed,direction(1 = counterclockwise and 2 = clockwise),
  //color1 for half the triangles, and color2 for the other half 
  r1 = new Roundabout(200,800,-900,200,3,2,color(220,75,75), color(80,80,240));
  r2 = new Roundabout(200,800,100,100,1,1,color(215,45,242), color(45,237,240));
  
  // Makes ball
  b = new Ball(600, 910, 100, 60, color(255, 207, 51), 600, 1000);
  // Makes two children
  ch1 = new Children(570, 800, color(200, 200, 200), 600, 500);
  ch2 = new Children(1100, 800, color(200, 200, 200), 1020, 940);
}

void draw() {
  // Move camera based on mouse input
  camera(mouseX, mouseY, height/2, 500, 800, 0, 0, 1, 0);
  background(200, 230, 230);
  // Create the ground object
  fill(110, 160, 60);
  pushMatrix();
  translate(500, 1000, 0);
  box(3000, 100, 3000);
  popMatrix();
  
  // First set of swings in middle
  stand.displayStand();
  swing1.move();
  swing1.displaySwing();
  swing1.moveSeat();
  swing2.move();
  swing2.displaySwing();
  swing2.moveSeat();
  // Second set of swings in right
  stand2.displayStand();
  swing3.move();
  swing3.displaySwing();
  swing3.moveSeat();
  swing4.move();
  swing4.displaySwing();
  swing4.moveSeat();
  // Third set of swings in left
  stand3.displayStand();
  swing5.move();
  swing5.displaySwing();
  swing5.moveSeat();
  swing6.move();
  swing6.displaySwing();
  swing6.moveSeat();
  
  // makes a roundabout
  r1.displayRoundabout();
  r1.spin();
  r2.displayRoundabout();
  r2.spin();
  
  // makes a ball
  b.display();
  ch2.display();
  ch1.displayChildren();
  b.move();
  
  // makes the children
  
  //ch1.walk();
  
  
  
}
