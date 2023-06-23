class Arrows extends Evaporation {
  // makes variables to be used and some to store from the Arrow class
  float initialy;
  float r,g,b,a, initiala;
  color c;
  PShape arrowHead, arrowBody, oneArrow;
  Arrows (float x, float y,float speed, color c) {
  super(x,y,speed);
  this.c = c;

  // store some initial values to repeat the animation
  initialy = this.y;
  r = red(c);
  g = green(c);
  b = blue(c);
  a = alpha(c);
  initiala = alpha(c);
  }
  // shows the arrows
  void display(){
    fill(c);
  oneArrow = createShape(GROUP);
  arrowHead = createShape(TRIANGLE,x-50,y,x+50,y,x,y-80);
  arrowBody = createShape(RECT,x,y+50,50,100);
  oneArrow.addChild(arrowHead);
  oneArrow.addChild(arrowBody);
  shape(oneArrow);
  }
  
  // slowly moves the arrow up based on speed, resets to inital y value when too high
  void move(){
    if(y > 350){
    y -= speed;
    } else{
        y = initialy;
    }
  }
  
  // changes the alpha level so it disappears, resets when position resets
  void disappear(){
    if (a > 1){
    a -=1;
    c = color(r,g,b,a);
    } else if (y == initialy){
      c = color(r,g,b,initiala);
      a = initiala;
    }
    }
    
}
