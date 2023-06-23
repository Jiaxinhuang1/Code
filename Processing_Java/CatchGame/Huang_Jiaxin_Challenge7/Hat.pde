class Hat {  //create the hat class
  float r;  //set the r variable value of the hat
  float x;  //set the x variable value of the hat
  float y;  //set the y variable value of the hat

  Hat(float hatRadius) {  //create object hat with radius as constructor
    r=hatRadius;  //set the r equal to the radius of the hat
  }
  void update() {  //create an update function
    x=sXPos-5;  //set the x equal to 5 units to the left of santas x position 
    y=600;  //set the y to 600
  }
  void display() {  //create a display function
    noStroke();  //make the hat with no stroke
    noFill();  //make the hat with no fill
    ellipse(x, y, r*2, r*2);  //make the hat an ellipse with position x,y and radius doubled
  }
}
