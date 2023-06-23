class Stand {
  // Declaring PShape and float variables
  float x, y, z;
  PShape swingStand;
  PShape sideStandOne;
  PShape sideStandTwo;
  PShape topStand;
  Stand(float x, float y, float z) {
    this.x = x;
    this.y = y;
    this.z = z;
  }
  // Displays the stand as a Group of PShapes
  void displayStand() {
    swingStand = createShape(GROUP);
    // Position of stand will be based on x, y, z input (controlled by translation)
    pushMatrix();
    translate(x, y, z);
    fill(0);
    // Show the side stand as box object
    sideStandOne = createShape(BOX, 10, 300, 200);
    shape(sideStandOne);
    translate(500, 0, 0);
    // Show the second side stand as box object 500 units right
    sideStandTwo = createShape(BOX, 10, 300, 200);
    shape(sideStandTwo);
    // Translate origin up and left and show the top part of stand
    translate(-250, -150, 0);
    topStand = createShape(BOX, 600, 10, 200);
    shape(topStand);
    popMatrix();
    swingStand.addChild(sideStandOne);
    swingStand.addChild(sideStandTwo);
    swingStand.addChild(topStand);
    //shape(swingStand);
  }
}
