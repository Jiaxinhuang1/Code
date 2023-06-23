class Rod {
  float x, y;
  float vy, m, ry, ks;
  PShape fishing, rod, string, bob, hook, hook2;

  Rod(float _x, float _y, float _m, float _ry, float _ks) {
    x = _x;
    y = _y;
    m = _m;
    ry = _ry;
    ks = _ks;
  }
  
  void display(){
    fill(140, 140, 140);
    fishing = createShape(GROUP);
    rod = createShape(QUAD, -70, 100, 40, 5, 45, 10, -70, 115);
    fill(202, 202, 202);
    string = createShape(QUAD, 45, 10, 47, 10, 72, 200, 70, 200);
    fill(222, 18, 18);
    bob = createShape(ELLIPSE, 70, 200, 30, 30);
    fill(100, 100, 100);
    hook = createShape(RECT, 65, 212, 10, 20);
    hook2 = createShape(RECT, 55, 232, 20, 10);
    
    fishing.addChild(hook2);
    fishing.addChild(rod);
    fishing.addChild(string);
    fishing.addChild(hook);
    shape(fishing, x, y);
    
    fill(222, 18, 18);
    bob = createShape(ELLIPSE, 70, 200, 30, 30);
    shape(bob, x, y);
  }
  
  void bob(){
    float f = -(ks * (y-ry));
    float a = f/m;
    vy = vy + a;
    y += vy;
  }
  
}
