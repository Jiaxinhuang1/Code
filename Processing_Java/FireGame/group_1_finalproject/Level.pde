class Level {
PShape level, p1,p2,p3,p4,p5,p6,p7,p8,p9,p10;  
int p1x = 500,p1y = 750,p1width = 150,p1height = 50;
int p2x = 0, p2y = 550,p2width = 800, p2height =50;
int p3x =150, p3y = 750, p3width = 50, p3height = 200;
int p4x = 325, p4y = 600, p4width = 50, p4height = 250;
int p5x = 800, p5y = 350, p5width = 50 , p5height = 400;
int p6x = 200, p6y = 350, p6width = 600, p6height =50;
int p7x = 200, p7y = 150, p7width = 650, p7height =50;
int p8x = 150, p8y = 150, p8width = 50, p8height = 250;
boolean collideOnLeft = false;
boolean collideOnRight = false;
boolean collideAbove = false;
boolean collideBelow = false;
  Level(){
  }
  
  void display(){
   level = createShape(GROUP);
  fill(140,90,30);
  p1 = createShape(RECT, p1x = 500,p1y = 750,p1width = 150,p1height = 50);
  p1.setStroke(false);
  p2 = createShape(RECT, p2x = 0, p2y = 550,p2width = 800, p2height =50);
  p2.setStroke(false);
  p3 = createShape(RECT, p3x =150, p3y = 750, p3width = 50, p3height = 200);
  p3.setStroke(false);
  p4 = createShape(RECT, p4x = 325, p4y = 600, p4width = 50, p4height = 250);
  p5 = createShape(RECT, p5x = 800, p5y = 350, p5width = 50 , p5height = 400);
  p6 = createShape(RECT, p6x = 200, p6y = 350,p6width = 600, p6height =50);
  p7 = createShape(RECT, p7x = 200, p7y = 150,p7width = 650, p7height =50);
  p8 = createShape(RECT, p8x = 150, p8y = 150, p8width = 50, p8height = 250);
  level.addChild(p1);
  level.addChild(p2);
  level.addChild(p3);
  level.addChild(p4);
  level.addChild(p5);
  level.addChild(p6);
  level.addChild(p7);
  level.addChild(p8);
  shape(level);
  }
  
  void checkCollision(float xPos,float yPos){
    float realy = yPos+100;
    float realx = xPos +50;
    //println(realx,realy);
    
    //println(abs(realx - p3x),abs(realx - (p3x + p3width)));
    //println(abs(realy - p3y),abs(realy - (p3y + p3height)));
    if ( abs(realx - p1x)< p1width+ 50 && abs(realx - (p1x + p1width)) < p1width+ 50 && abs(realy - p1y)< p1height+ 50 && abs(realy - (p1y + p1height)) < p1height+ 50 ) {
      if(abs(realx - p1x) < abs(realx - (p1x + p1width)) && realy > p1y && realy < (p1y + p1height)){
        collideOnLeft = true;
      }
      if (abs(realx - p1x) > abs(realx - (p1x + p1width)) && realy > p1y && realy < (p1y + p1height)){
        collideOnRight = true;
      }
      if (abs(realy - p1y) < abs(realy - (p1y + p1height)) && realx > p1x && realx < (p1x + p1width)){
        collideBelow = true;
      }
      if (abs(realy - p1y) > abs(realy - (p1y + p1height)) && realx > p1x && realx < (p1x + p1width)){
        collideAbove = true;
      }

    }else if ( abs(realx - p2x)< p2width+ 50 && abs(realx - (p2x + p2width)) < p2width+ 50 && abs(realy - p2y)< p2height+ 50 && abs(realy - (p2y + p2height)) < p2height+ 50) {
      if(abs(realx - p2x) < abs(realx - (p2x + p2width)) && realy > p2y && realy < (p2y + p2height)){
        collideOnLeft = true;
      }
      if (abs(realx - p2x) > abs(realx - (p2x + p2width)) && realy > p2y && realy < (p2y + p2height)){
        collideOnRight = true;
      }
      if (abs(realy - p2y) < abs(realy - (p2y + p2height)) && realx > p2x && realx < (p2x + p2width)){
        collideBelow = true;
      }
      if (abs(realy - p2y) > abs(realy - (p2y + p2height)) && realx > p2x && realx < (p2x + p2width)){
        collideAbove = true;
      } 

    } else if ( abs(realx - p3x)< p3width+ 50 && abs(realx - (p3x + p3width)) < p3width+50 && abs(realy - p3y)< p3height+ 50 && abs(realy - (p3y + p3height)) < p3height+ 50) {
      if(abs(realx - p3x) < abs(realx - (p3x + p3width)) && realy > p3y && realy < (p3y + p3height)){
        collideOnLeft = true;
      }
      if (abs(realx - p3x) > abs(realx - (p3x + p3width)) && realy > p3y && realy < (p3y + p3height)){
        collideOnRight = true;
      }
      if (abs(realy - p3y) < abs(realy - (p3y + p3height)) && realx > p3x && realx < (p3x + p3width)){
        collideBelow = true;
      }
      if (abs(realy - p3y) > abs(realy - (p3y + p3height)) && realx > p3x && realx < (p3x + p3width)){
        collideAbove = true;
      } 

    }else if ( abs(realx - p4x)< p4width+ 50 && abs(realx - (p4x + p4width)) < p4width+50 && abs(realy - p4y)< p4height && abs(realy - (p4y + p4height)) < p4height) {
      if(abs(realx - p4x) < abs(realx - (p4x + p4width)) && realy > p4y && realy < (p4y + p4height)){
        collideOnLeft = true;
      }
      if (abs(realx - p4x) > abs(realx - (p4x + p4width)) && realy > p4y && realy < (p4y + p4height)){
        collideOnRight = true;
      }
      if (abs(realy - p4y) < abs(realy - (p4y + p4height)) && realx > p4x && realx < (p4x + p4width)){
        collideBelow = true;
      }
      if (abs(realy - p4y) > abs(realy - (p4y + p4height)) && realx > p4x && realx < (p4x + p4width)){
        collideAbove = true;
      } 

    }else if ( abs(realx - p5x)< p5width+ 50 && abs(realx - (p5x + p5width)) < p5width+50 && abs(realy - p5y)< p5height && abs(realy - (p5y + p5height)) < p5height+ 50) {
      if(abs(realx - p5x) < abs(realx - (p5x + p5width)) && realy > p5y && realy < (p5y + p5height)){
        collideOnLeft = true;
      }
      if (abs(realx - p5x) > abs(realx - (p5x + p5width)) && realy > p5y && realy < (p5y + p5height)){
        collideOnRight = true;
      }
      if (abs(realy - p5y) < abs(realy - (p5y + p5height)) && realx > p5x && realx < (p5x + p5width)){
        collideBelow = true;
      }
      if (abs(realy - p5y) > abs(realy - (p5y + p5height)) && realx > p5x && realx < (p5x + p5width)){
        collideAbove = true;
      }  
    }else if ( abs(realx - p6x)< p6width+ 50 && abs(realx - (p6x + p6width)) < p6width+50 && abs(realy - p6y)< p6height+ 25 && abs(realy - (p6y + p6height)) < p6height+ 50) {
      if(abs(realx - p6x) < abs(realx - (p6x + p6width)) && realy > p6y && realy < (p6y + p6height)){
        collideOnLeft = true;
      }
      if (abs(realx - p6x) > abs(realx - (p6x + p6width)) && realy > p6y && realy < (p6y + p6height)){
        collideOnRight = true;
      }
      if (abs(realy - p6y) < abs(realy - (p6y + p6height)) && realx > p6x && realx < (p6x + p6width)){
        collideBelow = true;
      }
      if (abs(realy - p6y) > abs(realy - (p6y + p6height)) && realx > p6x && realx < (p6x + p6width)){
        collideAbove = true;
      } 
    }else if ( abs(realx - p7x)< p7width+ 50 && abs(realx - (p7x + p7width)) < p7width+50 && abs(realy - p7y)< p7height+ 25 && abs(realy - (p7y + p7height)) < p7height+ 50) {
      if(abs(realx - p7x) < abs(realx - (p7x + p7width)) && realy > p7y && realy < (p7y + p7height)){
        collideOnLeft = true;
      }
      if (abs(realx - p7x) > abs(realx - (p7x + p7width)) && realy > p7y && realy < (p7y + p7height)){
        collideOnRight = true;
      }
      if (abs(realy - p7y) < abs(realy - (p7y + p7height)) && realx > p7x && realx < (p7x + p7width)){
        collideBelow = true;
      }
      if (abs(realy - p7y) > abs(realy - (p7y + p7height)) && realx > p7x && realx < (p7x + p7width)){
        collideAbove = true;
      } 
    }else if ( abs(realx - p8x)< p8width+ 50 && abs(realx - (p8x + p8width)) < p8width+50 && abs(realy - p8y)< p8height+ 25 && abs(realy - (p8y + p8height)) < p8height+ 50) {
      if(abs(realx - p8x) < abs(realx - (p8x + p8width)) && realy > p8y && realy < (p8y + p8height)){
        collideOnLeft = true;
      } 
      if (abs(realx - p8x) > abs(realx - (p8x + p8width)) && realy > p8y && realy < (p8y + p8height)){
        collideOnRight = true;
      }
      if (abs(realy - p8y) < abs(realy - (p8y + p8height)) && realx > p8x && realx < (p8x + p8width)){
        collideBelow = true;
      }
      if (abs(realy - p8y) > abs(realy - (p8y + p8height)) && realx > p8x && realx < (p8x + p8width)){
        collideAbove = true;
      } 
    }
    
    else{
    collideOnLeft = false;
    collideOnRight = false;
    collideBelow = false;
    collideAbove = false;
    }
   
    
  }
}
