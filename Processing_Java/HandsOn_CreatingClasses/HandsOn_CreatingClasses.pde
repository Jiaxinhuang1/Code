// Creates new spot objects
Spot sp1 = new Spot(10, 10, 50, 10);
Spot sp2 = new Spot(10, 10, 50, 10);
Spot sp3 = new Spot(30, 30, 30, 5);
Spot sp4 = new Spot(30, 30, 30, 5);

void setup() {
  size(1000, 1000);
  background(0);
}

void draw(){
  // Calls the class and moves the spot object
  fill(200);
  sp1.moveRight();
  sp2.moveDown();
  fill(150, 0, 0);
  sp3.moveRight();
  sp4.moveDown();
}
