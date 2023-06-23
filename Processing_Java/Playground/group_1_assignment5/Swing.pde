class Swing {
  // Declare float and PShape variables
  float originX, originY, jointX, jointY, angle, aVel, aAcc;
  PShape swing;
  PShape chain;
  PShape chain2;
  PShape seat;
  Swing(float originX, float originY, float jointX, float jointY, float angle, float aVel, float aAcc) {
    this.originX = originX;
    this.originY = originY;
    this.jointX = jointX;
    this.jointY = jointY;
    this.angle = angle;
    this.aVel = aVel;
    this.aAcc = aAcc;
  }
  // Show the swing object (the two chains)
  void displaySwing() {
    // Swing is a group of two lines as chains
    swing = createShape(GROUP);
    stroke(150);
    pushMatrix();
    translate(0, 0, -300);
    strokeWeight(10);
    // Line position set by parameters
    chain = createShape(LINE, originX, originY, jointX, jointY);
    // Second chain is a line to the side of first
    chain2 = createShape(LINE, originX + 100, originY, jointX + 100, jointY);
    popMatrix();
    pushMatrix();
    translate(0, 0, -300);
    // Show swing group as two chains
    swing.addChild(chain);
    swing.addChild(chain2);
    shape(swing);
    // Show another group of two chains behind the first (4 chains in total)
    translate(0, 0, -100);
    shape(swing);
    popMatrix();
    stroke(0);
  }
  // Function that controls chain movement
  void move() {
    // rotates chain based on sin and cos (like a pendulum)
    jointX = originX + 200 * sin(angle);
    jointY = originY + 200 * cos(angle);
    // changing velocity and acceleration to show ease in and out
    aAcc = -0.01 * sin(angle);
    angle += aVel;
    aVel += aAcc;
    aVel *= 0.99;
  }
  // function that draws and translates the seat based on the chain movements
  void moveSeat() {
    pushMatrix();
    translate(50, 0, -350);
    translate(jointX, jointY);
    box(100, 10, 100);
    popMatrix();
  }
}
