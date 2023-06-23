class Crab {
  float x, y;
  float vy;
  float ay;
  float friction;
  PShape crab, body,eye1,eye2, claw1,claw2, arm1,arm2,arm3,arm4,leg1,leg2;

  Crab(float _x, float _y, float _vy, float _ay, float fr){
    x = _x;
    y = _y;
    vy = _vy;
    ay = _ay;
    friction = fr;
    
  }
  
  void display(){
    fill(255,81,0);
    crab = createShape(GROUP);
    body = createShape(ELLIPSE, 0,0,120,80);
    claw1 = createShape(ARC, -40, -80,40,40,0, 3*PI/2 );
    claw2 = createShape(ARC, 40, -80,40,40,-PI/2,PI );
    arm1 = createShape(ELLIPSE, 60,-55,30,30);
    arm2 = createShape(ELLIPSE, 60,-30,30,30);
    arm3 = createShape(ELLIPSE, -60,-55,30,30);
    arm4 = createShape(ELLIPSE, -60,-30,30,30);
    leg1 = createShape(RECT,-45,25,30,30);
    leg2 = createShape(RECT,15,25,30,30);
    
    fill(0,0,0);
    eye1 = createShape(ELLIPSE,-20,-20,20,20);
    eye2 = createShape(ELLIPSE,20,-20,20,20);

    
    crab.addChild(body);
    crab.addChild(eye1);
    crab.addChild(eye2);
    crab.addChild(claw1);
    crab.addChild(claw2);
    crab.addChild(arm1);
    crab.addChild(arm2);
    crab.addChild(arm3);
    crab.addChild(arm4);
    crab.addChild(leg1);
    crab.addChild(leg2);
    shape(crab,x,y);
  }
  
  void applyforces(){
  vy += ay;
  vy *= friction;
  y += vy;
   if (y > (height - 100)) {
  vy = -vy;
 }
  }
}
