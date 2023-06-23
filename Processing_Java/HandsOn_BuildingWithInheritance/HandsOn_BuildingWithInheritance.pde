ColoredSpot coloredSpot = new ColoredSpot(500, 500, 50, 5, color(200, 0, 0)); 
ColoredSpot coloredSpot1 = new ColoredSpot(500, 500, 50, 5, color(0, 0, 200));
TwoSpots twoSpots = new TwoSpots(500, 500, 50, 5);
TwoSpots twoSpots1 = new TwoSpots(500, 500, 70, 4);

void setup() {
  size(1000, 1000);
  background(40);
}

void draw() {
  coloredSpot.colors();
  twoSpots.moveRight();
  twoSpots.display();
  coloredSpot1.colors();
  twoSpots1.moveDown();
  twoSpots1.displayVert();
}
