class Goal{
  float x, y;
  float w, h;
  Goal(float x, float y, float w, float h){
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
  }
  // draws the goal door
  void display(){
    fill(0);
    rect(x, y, w, h);
    fill(255);
    ellipse(x + 20, y + h/2, 20, 20);
  }
}
