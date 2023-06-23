class Fish{
  float x, y;
  float vy;
  float ay;
  float friction;
  float ogspeed;
  PShape fish, tail, body, eye;
  
  Fish(float _x, float _y, float _vy, float _ay, float fric){
    x = _x;
    y = _y;
    vy = _vy;
    ay = _ay;
    friction = fric;
    ogspeed = vy;
    
  }
  
  void display(){
    fill(255,146,0);
    fish = createShape(GROUP);
    tail = createShape(TRIANGLE,-20,-20,-20,20,0,0);
    body = createShape(ELLIPSE,30,0,60,30);
    
    fill(0,0,0);
    eye = createShape(ELLIPSE,50,-5,10,10);
    
    fish.addChild(tail);
    fish.addChild(body);
    fish.addChild(eye);
    shape(fish,x,y);
  
  }

  void move(){
  vy += ay;
  vy *= friction;
  x += vy;
  if(vy > (ogspeed*5)){
    vy = ogspeed;
  }
  }
  
  void reset(){
  if(x > width + 200){
    x = random(-500,0);
    y = random(250,900);
  
  }
  }

}
