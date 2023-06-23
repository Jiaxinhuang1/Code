class RunOff {
  color c;
  float x, y, speed, len, wid;
  float start = 360, end = 880;
  boolean grown = false;
  RunOff(float x, float y, color c, float len, float wid) {
    this.x = x;
    this.y = y;
    this.c = c;
    this.len = len;
    this.wid = wid;
  }
  
  void display(){
    //ground for water to collect
    fill(86, 42, 12);
    rect(0, y + 100, 700, 250);
    rect(700, y + 150, 900, 100);
    triangle(350, 875, 350, 1000, 1000, 1000);
    
    //body of water
    fill(60, 143, 205);
    triangle(600, 925, 1000, 925, 1000, 1000);
    
    //water collecting
    ellipse(150, 880, len, wid);
    
    //water droplet rolling
    ellipse(start, end, 20, 20);
  }
  
  //grow and shrink
  void waterCollection(){
    if (len == 400){
      grown = true;
    } else if (len == 10){
      grown = false;
    }
    if (len < 400 && grown == false){
      len += 10;
      wid += 1;
    } else {
      len -= 10;
      wid -= 1;
    }
  }
  
  //ellipse rolling down the hill
  void flow(){
    if (end == 925){
      start = 360;
      end = 880;
    }
    if (start < 925){
      start += 5;
      end++;
    }
  }
}
