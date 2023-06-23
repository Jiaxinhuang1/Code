class Seahorse2 {
  float x, y, x2, currentx;
  float vy, m, ry, ks;
  PShape seahorse, head, nose, body, tail, tail2, bodyfin, eye, nostril, nostrilhole;
  boolean forward = true;
  
  Seahorse2(float _x, float _y, float _currentx, float _x2, float _m, float _ry, float _ks) {
    x = _x;
    x2 = _x2;
    currentx = _currentx;
    y = _y;
    m = _m;
    ry = _ry;
    ks = _ks;
  }
  
  void display(){
    fill(255, 229, 84);
    seahorse = createShape(GROUP);
    head = createShape(ELLIPSE, 300, 300, 25, 25);
    nose = createShape(RECT, 305, 300, 15, 10);
    nostril = createShape(ELLIPSE, 320, 302, 8, 8);
    fill(0, 0, 0);
    nostrilhole = createShape(ELLIPSE, 320, 302, 6, 6);
    fill(255, 229, 84);
    body = createShape(QUAD, 287, 305, 315, 320, 305, 370, 287, 350);
    tail = createShape(QUAD, 305, 370, 308, 350, 320, 370, 320, 380);
    fill(181, 222, 131);
    tail2 = createShape(QUAD, 320, 380, 320, 350, 330, 350, 323, 380);
    bodyfin = createShape(QUAD, 280, 310, 287, 315, 287, 330, 280, 335);
    fill(41, 62, 145);
    eye = createShape(ELLIPSE, 300, 300, 10, 10);
    
    seahorse.addChild(head);
    seahorse.addChild(nose);
    seahorse.addChild(nostril);
    seahorse.addChild(nostrilhole);
    seahorse.addChild(eye);
    seahorse.addChild(body);
    seahorse.addChild(tail);
    seahorse.addChild(tail2);
    seahorse.addChild(bodyfin);
    shape(seahorse, currentx, y);
  }
  
  void move(){
    // if currentx is at x or greater than x and moving forwards to x2
    if (currentx < x2 && forward == true && currentx >= x){
      currentx += 5;
    // else if currentx is at x2 and now switching directions
    } else if (currentx >= x2 && forward == true){
      forward = false;
      currentx -= 5;
    // else if currentx is in between x and x2 and moving backwards to x
    } else if (currentx < x2 && forward == false && currentx > x){
      currentx -= 5;
    } else {
      forward = true;
      currentx += 5;
    }
  }
  
  void jump(){
    float f = -(ks * (y-ry));
    float a = f/m;
    vy = vy + a;
    y += vy;
  }
  
}
