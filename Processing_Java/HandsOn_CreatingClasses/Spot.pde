class Spot {
  float x, y, radius, speed;
  // Add attributes or parameters to class that can be called when creating new spot object
  Spot(float _x, float _y, float _r, float _speed){
    this.x = _x; 
    this.y = _y;
    this.radius = _r;
    this.speed = _speed;
  }
  // Moves the object right and loops with additional height
  void moveRight(){
    x += speed;
    if (x > width){
      x = 10;
      y = y + 100;
      if (y > height){
        y = 0;
      }
    }
    ellipse(x, y, radius, radius);
  }
  // Moves the object down and loops with additional width
    void moveDown(){
    y += speed;
    if (y > height){
      y = 10;
      x = x + 100;
      if (x > width){
        x = 0;
      }
    }
    ellipse(x, y, radius, radius);
  }
}
