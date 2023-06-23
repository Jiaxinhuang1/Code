//import processing.sound.*;
Cloud cloud;
Cloud cloud1;
Cloud cloud2;
Cloud cloud3;
Sun sun;
Rain [] rains = new Rain[100];

Arrows arrow1;
Arrows arrow2;
Arrows arrow3;
Arrows arrow4;
Arrows arrow5;

Lake lake1;

RunOff run;
Fish fish1;

//SoundFile bkgd;

void setup() {
  // creates the new cloud Pshape group
  cloud = new Cloud(220, 80, 175, 50, 0.25, color(100));
  cloud1 = new Cloud(150, 100, 150, 50, 1, color(150));
  cloud2 = new Cloud(300, 170, 100, 50, 0.5, color(210, 220, 230));
  cloud3 = new Cloud(100, 160, 120, 50, 0.25, color(220, 230, 240));
  // creates sun
  sun = new Sun(0, 0, 150, 0, 1);
  size(1000, 1000);
  background(185, 215, 240);
  // instantiate 100 rain drop each time
  for (int i = 0; i < rains.length; i++) {
    rains[i] = new Rain(random(50, 350), random(50, 100), 0, random(3, 7), 0);
    
  //evaporation arrows
  arrow1 = new Arrows(900,620,1,color(0,183,234,220));
  arrow2 = new Arrows(795,450,1,color(0,183,234,50));
  arrow3 = new Arrows(650,580,1,color(0,183,234,180));
  arrow4 = new Arrows(830,520,1,color(0,183,234,120));
  arrow5 = new Arrows(725,655,1,color(0,183,234,255));
  
  lake1 = new Lake(650,975,975);
  
  //run off
  run = new RunOff(500, 900, color(86, 42, 12), 10, 10);
  
  // creates the fish
  fish1 = new Fish(950, 950, color(239, 159, 58), 5, 15, color(255, 87, 51));
  
  //create the background music
  //bkgd = new SoundFile(this, "WaterCycle.wav");
  //bkgd.amp(0.05);
  //bkgd.play();
  }
}

void draw() {
  background(185, 215, 240);
  // show and make all the raindrop fall
  for (int i = 0; i < rains.length; i++) {
    rains[i].fall();
    rains[i].showRain();
  }
  // show and increase/decrease size of clouds
  cloud.sizeTransform();
  cloud.display();
  cloud1.sizeTransform();
  cloud1.display();
  cloud2.sizeTransform();
  cloud2.display();
  cloud3.sizeTransform();
  cloud3.display();

  // draws the sun rotating and increasing its scale
  sun.display();
  sun.update();
  
  //draws the lake going up and down due to evaporation
  lake1.display();
  
  // draws the ground, water collecting from precipitation, runoff, and body of water
  run.display();
  run.waterCollection();
  run.flow();
  
  // draws the fish swimming in the water
  fish1.display();
  fish1.swim();
  
  //show evaporation arrows
  arrow1.display();
  arrow1.move();
  arrow1.disappear();
  arrow2.display();
  arrow2.move();
  arrow2.disappear();
  arrow3.display();
  arrow3.move();
  arrow3.disappear();
  arrow4.display();
  arrow4.move();
  arrow4.disappear();
  arrow5.display();
  arrow5.move();
  arrow5.disappear();

  
  
}
