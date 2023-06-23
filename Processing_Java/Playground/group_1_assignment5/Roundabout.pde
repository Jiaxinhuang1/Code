class Roundabout {
  
  float x,y,z;
  float radius;
  float speed;
  float direction;
  color color1;
  color color2;
  
  float spinAng = 0;
  
  PShape body;
  PShape tri1,tri2,tri3,tri4,centerbar,handle1,handle2,handle3,handle4;
  PShape h11,h12,h13,h21,h22,h23,h31,h32,h33,h41,h42,h43;
  
  // Makes roundabouts with x position,y position,z position, 
  //speed,direction(1 = counterclockwise and 2 = clockwise),
  //color1 for half the triangles, and color2 for the other half 
  
  Roundabout(float _x, float _y, float _z, float rad,
  float s, float dir, color col1, color col2){
    x = _x;
    y = _y;
    z = _z;
    radius = rad;
    speed = s;
    direction = dir;
    color1 = col1;
    color2 = col2;
  }
  void displayRoundabout(){
    //create one body that is the entire shape
    body = createShape(GROUP);
    pushMatrix();
    translate(x,y,z);
    
    //creates the triangles that make up the roundabout based on radius and x,y,z
    tri1 = createShape(TRIANGLE,0,0,radius,radius,radius,-radius);
    tri1.setFill(color1);
    tri2 = createShape(TRIANGLE,0,0,radius,-radius,-radius,-radius);
    tri2.setFill(color2);
    tri3 = createShape(TRIANGLE,0,0,-radius,-radius,-radius,radius);
    tri3.setFill(color1);
    tri4 = createShape(TRIANGLE,0,0,-radius,radius,radius,radius);
    tri4.setFill(color2);
    
    //create the center pole on the roundabout
    centerbar = createShape(BOX,radius/20,radius/20,200);
    centerbar.translate(0,0,radius/4);
    
    //creates handles on first color based off of radius (red)
    handle1 = createShape(GROUP);
    h11 =createShape(BOX,radius/40,radius/2,radius/40);
    h11.translate(3*radius/4,0,radius/2);
    h12 =createShape(BOX,radius/40,radius/40,radius/2);
    h12.translate(3*radius/4,radius/4,radius/4);   
    h13 =createShape(BOX,radius/40,radius/40,radius/2);
    h13.translate(3*radius/4,-radius/4,radius/4);
    
    handle2 = createShape(GROUP);
    h21 =createShape(BOX,radius/40,radius/2,radius/40);
    h21.translate(-3*radius/4,0,radius/2);
    h22 =createShape(BOX,radius/40,radius/40,radius/2);
    h22.translate(-3*radius/4,radius/4,radius/4);   
    h23 =createShape(BOX,radius/40,radius/40,radius/2);
    h23.translate(-3*radius/4,-radius/4,radius/4);
    
    //creates handles on second color based off radius (blue)
    handle3 = createShape(GROUP);
    h31 =createShape(BOX,radius/2,radius/40,radius/40);
    h31.translate(0,3*radius/4,radius/2);
    h32 =createShape(BOX,radius/40,radius/40,radius/2);
    h32.translate(-radius/4,3*radius/4,radius/4);   
    h33 =createShape(BOX,radius/40,radius/40,radius/2);
    h33.translate(radius/4,3*radius/4,radius/4);
    
    handle4 = createShape(GROUP);
    h41 =createShape(BOX,radius/2,radius/40,radius/40);
    h41.translate(0,-3*radius/4,radius/2);
    h42 =createShape(BOX,radius/40,radius/40,radius/2);
    h42.translate(-radius/4,-3*radius/4,radius/4);   
    h43 =createShape(BOX,radius/40,radius/40,radius/2);
    h43.translate(radius/4,-3*radius/4,radius/4);


    popMatrix();
    //add the specific handle parts to one handle group
    handle1.addChild(h11);
    handle1.addChild(h12);
    handle1.addChild(h13);
    
    handle2.addChild(h21);
    handle2.addChild(h22);
    handle2.addChild(h23);
    
    handle3.addChild(h31);
    handle3.addChild(h32);
    handle3.addChild(h33);
    
    handle4.addChild(h41);
    handle4.addChild(h42);
    handle4.addChild(h43);
    
    //add the triangles to the shape
    body.addChild(tri1);
    body.addChild(tri2);
    body.addChild(tri3);
    body.addChild(tri4);
    
    //add the center and the handles to a roundabout
    body.addChild(centerbar);
    body.addChild(handle1);
    body.addChild(handle2);
    body.addChild(handle3);
    body.addChild(handle4);
    
    //makes the triangles flat on the ground
    body.rotateX(PI/2);
    body.rotateY(radians(spinAng));
    
    //moves roundabout to the floor
    body.translate(0,145,z);
    shape(body,x,y);
  }
  
  void spin(){
    if(direction == 2){
      spinAng -=speed;
    } else if(direction ==1){
      spinAng +=speed;
    }
    if(spinAng > 1080){
    spinAng = 0;
    }
  }
}
