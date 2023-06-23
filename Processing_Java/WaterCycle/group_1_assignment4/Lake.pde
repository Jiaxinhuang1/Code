class Lake{
  float x,y,miny;
  float change;
  Lake(float x, float y,float miny){
  this.x = x;
  this.y = y;
  this.miny = miny;
  change = 1;
  }
  
  void display(){
  fill(60, 143, 205);
  rect(x,y,700,200);
  y +=change;
  if ((y == miny)||(y ==height+50)){
    change = -change;
  }
  }
}
