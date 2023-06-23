class Cap {  //creates the cap class
  float r;  //set the r variable value of the cap
  float x;  //set the x variable value of the cap
  float y;  //set the y variable value of the cap

  Cap(float capRadius) {  //create object cap with radius as constructor
    r=capRadius;  //set r equal to the radius of the cap
  }
  void update() {  //create a update function
    x=smanXPos;  //set x equal to the x position of the snowman
    y=600;  //set the y position equal to 600
  }
  void display() {  //create the display function
    noStroke();  //make the cap with no stroke
    noFill();  //make the cap with no fill
    ellipse(x, y, r*2, r*2);  //make the cap an ellipse with position x,y and radius doubled
  }
}
