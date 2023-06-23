class Buoy {
  float x, y;
  float vy, m, ry, ks;
  PShape buoy, top, b1, b2, b3, bottom;
  PShape bob;
  
  Buoy(float _x, float _y, float _m, float _ry, float _ks) {
    x = _x;
    y = _y;
    m = _m;
    ry = _ry;
    ks = _ks;
  }
  
  void display(){
    fill(255, 255, 255);
    buoy = createShape(GROUP);
    top = createShape(ELLIPSE, 0, 0, 30, 30);
    fill(222, 18, 18);
    b1 = createShape(QUAD, -15, 15, 15, 15, 30, 45, -30, 45);
    fill(255, 255, 255);
    b2 = createShape(QUAD, -30, 45, 30, 45, 45, 115, -45, 115);
    fill(222, 18, 18);
    b3 = createShape(QUAD, -45, 75, 45, 75, 60, 105, -60, 105);
    fill(255, 255, 255);
    bottom = createShape(RECT, -70, 100, 140, 60);
    
    buoy.addChild(top);
    buoy.addChild(b1);
    buoy.addChild(b2);
    buoy.addChild(b3);
    buoy.addChild(bottom);
    shape(buoy, x, y);
  }
  
  void bob(){
    float f = -(ks * (y-ry));
    float a = f/m;
    vy = vy + a;
    y += vy;
  }
}
