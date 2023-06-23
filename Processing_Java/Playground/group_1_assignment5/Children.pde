class Children{
  float x, y, end, start;
  PShape body, head, arm, lleg, rleg, child;
  color c;
  boolean back;
  Children(float x, float y, color c, float end, float start){
    this.x = x;
    this.y = y;
    this.c = c;
    this.end = end;
    this.start = start;
  }
  void displayChildren(){
    // Display with movement
    pushMatrix();
    translate(x, y, 200);
    
    child = createShape(GROUP);
    
    // create each body part
    head = createShape(SPHERE, 30);
    head.translate(-40, 0, 100);
    head.setFill(c);
    
    body = createShape(BOX, 30, 90, 80);
    body.translate(-40, 75, 100);
    body.setFill(c);
    
    arm = createShape(BOX, 30, 40, 100);
    arm.translate(-40, 50, 100);
    arm.setFill(c);
    
    lleg = createShape(BOX, 15, 40, 20);
    lleg.translate(-40, 127, 120);
    lleg.setFill(c);
    
    rleg = createShape(BOX, 15, 40, 20);
    rleg.translate(-40, 127, 75);
    rleg.setFill(c);
    
    popMatrix();
    
    child.addChild(head);
    child.addChild(body);
    child.addChild(arm);
    child.addChild(lleg);
    child.addChild(rleg);
    
    // draw child
    shape(child, x, y);
    
    if (x == end){
      back = true;
    }
    else if (x == start){
      back = false;
    }
    
    if (x <= end && back == false){
      translate(x+=2, y);
    }
    else if (x > start && back == true){
      translate(x-=2, y);
    }
  }
  
  void display(){
    // Display without movement
    pushMatrix();
    translate(x, y, 200);
    
    child = createShape(GROUP);
    
    // create each body part
    head = createShape(SPHERE, 30);
    head.translate(-40, 0, 100);
    head.setFill(c);
    
    body = createShape(BOX, 30, 90, 80);
    body.translate(-40, 75, 100);
    body.setFill(c);
    
    arm = createShape(BOX, 30, 40, 100);
    arm.translate(-40, 50, 100);
    arm.setFill(c);
    
    lleg = createShape(BOX, 15, 40, 20);
    lleg.translate(-40, 127, 120);
    lleg.setFill(c);
    
    rleg = createShape(BOX, 15, 40, 20);
    rleg.translate(-40, 127, 75);
    rleg.setFill(c);
    
    popMatrix();
    
    child.addChild(head);
    child.addChild(body);
    child.addChild(arm);
    child.addChild(lleg);
    child.addChild(rleg);
    
    // draw child
    shape(child, x, y);
  }
}
