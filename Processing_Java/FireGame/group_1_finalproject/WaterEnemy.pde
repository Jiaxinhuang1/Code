class WaterEnemy extends Enemy {
  PShape waterenemy, body, top, eyel, eyer, eyebrowl, eyebrowr, rleg, lleg, rarm, larm;
  color base, face, arms;
  float maxY, minY;
  boolean forward = true;
  float fx, fy;
  HealthSystem health;
  
  WaterEnemy(float xPos, float yPos, float speed, color _base, color _face, color _arms, float _maxY, float _minY) {
    super(xPos, yPos, speed);
    this.base = _base;
    this.face = _face;
    this.arms = _arms;
    this.maxY = _maxY;
    this.minY = _minY;
  }
  
  void display() {
    noStroke();
    fill(base);
    waterenemy = createShape(GROUP);
    body = createShape(ELLIPSE, xPos, yPos, 80, 80);
    top = createShape(TRIANGLE, xPos - 36, yPos - 18, xPos + 36, yPos - 18, xPos, yPos - 75);
    fill(face);
    eyel = createShape(ELLIPSE, xPos - 20, yPos, 20, 20);
    eyer = createShape(ELLIPSE, xPos + 20, yPos, 20, 20);
    eyebrowl = createShape(TRIANGLE, xPos - 20, yPos - 12, xPos - 35, yPos - 8, xPos - 35, yPos - 16);
    eyebrowr = createShape(TRIANGLE, xPos + 20, yPos - 12, xPos + 35, yPos - 8, xPos + 35, yPos - 16);
    stroke(arms);
    strokeWeight(3);
    rleg = createShape(LINE, xPos - 30, yPos + 25, xPos - 30, yPos + 45);
    lleg = createShape(LINE, xPos + 30, yPos + 25, xPos + 30, yPos + 45);
    rarm = createShape(LINE, xPos - 40, yPos, xPos - 55, yPos + 20);
    larm = createShape(LINE, xPos + 40, yPos, xPos + 55, yPos + 20);
    noStroke();
    
    waterenemy.addChild(body);
    waterenemy.addChild(top);
    waterenemy.addChild(eyel);
    waterenemy.addChild(eyer);
    waterenemy.addChild(eyebrowl);
    waterenemy.addChild(eyebrowr);
    waterenemy.addChild(rleg);
    waterenemy.addChild(lleg);
    waterenemy.addChild(rarm);
    waterenemy.addChild(larm);
    shape(waterenemy);
  }
  
  void movement() {
    if (yPos >= maxY) {
      forward = false;
    }
    if (yPos <= minY) {
      forward = true;
    }
    if (forward == true && yPos < maxY) {
      yPos += 3;
    } else if (forward == false && yPos > minY) {
      yPos -= 3;
    }
  }
  
  boolean collision(float fx, float fy) {
    print("This is x", fx, fy);
    print("This is enemy", xPos, yPos);
    if (fx <= xPos + 50 && fx >= xPos - 50 && fy <= yPos + 100 && fy >= yPos - 100) {
      print("DEAD");
      return true;
    } else {
      return false;
    }
  }
 
}
