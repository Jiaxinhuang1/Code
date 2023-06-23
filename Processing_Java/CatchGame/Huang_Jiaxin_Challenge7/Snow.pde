public class Snow {  //create the snowball class
  float x;   //set the x variable value of the snow
  float y;  //set the y variable value of the snow
  float r;  //set the r varible value of the snow
  float speedY;  //set the speed of y variable value of the snow

  Snow() {  //create an object of snow
    r=8;  //set r equal to 8
    x=random(width);  //set x position equal to a random pot from 0 to width
    y=-r*4;  //set y equal to above the screen
    speedY=random(1, 5);  //set the speed of y to random between 1 and 5
  }

  void fall() {  //create fall function
    y+=speedY;  //unpdate the y postion with the random speed
    if (y>height+r) {  //if the y position is greater than the height of the screen plus r
      y=-r;  //set y equal to negative r
    }
  }

  void display() {  //create the display function
    noStroke();  //make the snow with no stroke
    fill(0, 0, 200, 150);  //make the color of snow light blue with transparency
    ellipse(x, y, r*5, r*5); //make the snow an ellipse with position x,y and radius times 5
    stroke(255);  //make another snow on top with no stroke
    fill(255);  //make the snow white
    ellipse(x, y, r*3, r*3);  //make the snow an ellipse in same positon but smaller with radius times 3
  }

  void caught() {  //create a caught function
    speedY=0;  //set the speed of y to zero
    y=-50;  //set the y position out of the screen to negtive
  }
}
