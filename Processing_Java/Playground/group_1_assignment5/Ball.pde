class Ball{
  float x, y, z, size;
  color c;
  PShape ball;
  float start, end;
  boolean back = false;
  Ball(float x, float y, float z, float size, color c, float start, float end){
    this.x = x;
    this.y = y;
    this.z = z;
    this.size = size;
    this.c = c;
    this.start = start;
    this.end = end;
  }
  
  void display(){
    // create the ball shape with sphere primitive
    noStroke();
    fill(c);
    pushMatrix();
    translate(x, y, z);
    sphere(40);
    popMatrix();
  }
  
  void move(){
    // animate ball to roll back and forth
    if (x == 1000){
      back = true;
    }
    else if (x == 600){
      back = false;
    }
    
    if (x <= 1000 && back == false){
      translate(x+=2, y, z);
    }
    else if (x > 600 && back == true){
      translate(x-=2, y, z);
    }
  }
}
