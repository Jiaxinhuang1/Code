BubbleSystem bubs;
BubbleSystem bubs2;
float bz;
boolean change;

Crab crab1;

Fish fish1;
Fish fish2;
Fish fish3;

Buoy buoy;
Rod rod;
Seahorse seahorse;
Seahorse2 seahorse2;

void setup() {
  size(1000, 1000);
  //bubble = new Bubble(500, 900, random(-0.1, 0.01), random(-10, -5), 100, color(200, 250, 250));
  // creates two particle systems
  bubs = new BubbleSystem(0, 1000);
  bubs2 = new BubbleSystem(1000, 1000);
  crab1 =  new Crab(250, 850, 5, 0.05, 1);
  fish1 = new Fish(300, 250, 2.5, 0.2, 1);
  fish2 = new Fish(500, 750, 2, 0.25, 1);
  fish3 = new Fish(700, 550, 1.5, 0.4, 1);
  
  buoy = new Buoy(700, 40, 5.0, 60, 0.01);
  rod = new Rod(70, 0, 6.0, 10, 0.01);
  seahorse = new Seahorse(300, 300, 300, 500, 3.0, 330, 0.01);
  seahorse2 = new Seahorse2(0, 0, 0, 200, 1.0, 80, 0.01);
}

void draw() {
  // draw the sky, ocean, and ground
  background(190, 230, 230);
  fill(100, 160, 200);
  rect(0, 200, 1000, 800);
  fill(200, 160, 120);
  rect(0, 950, 1000, 50);
  strokeWeight(5);
  fill(200, 230, 160);
  bezier(300, 1000, 500 + bz, 1000, 500 - bz, 400, 600, 600);
  bezier(300, 1000, 200 + bz, 1000, 200 - bz, 500, 200, 500);
  bezier(700, 1000, 600 + bz, 900, 700 - bz, 800, 600, 800);
  bezier(700, 1000, 900 + bz, 900, 900 - bz, 700, 800, 900);
  if (bz >= 200) {
    change = false;
  }
  if (bz <= 0){
    change = true;
  }
  if (change == true)
  {
    bz += 1;
  } 
  else {
    bz -= 1;
  }

  // calls the particle system to create and move bubbles
  bubs.createBubbles();
  bubs.moveBubbles();
  bubs2.createBubbles();
  bubs2.moveBubbles();
  crab1.display();
  crab1.applyforces();
  fish1.display();
  fish1.move();
  fish1.reset();
  fish2.display();
  fish2.move();
  fish2.reset();
  fish3.display();
  fish3.move();
  fish3.reset();
  buoy.display();
  buoy.bob();
  seahorse.move();
  seahorse.display();
  seahorse.jump();
  rod.display();
  rod.bob();
  seahorse2.move();
  seahorse2.display();
  seahorse2.jump();
}
