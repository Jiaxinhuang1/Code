//Credit: Altered Daniel Shiffman's simple particle system example on processing.org
class BubbleSystem {
  // create an array list of bubble objects (this is the Particle system)
  ArrayList<Bubble> bubs;
  float x, y;

  BubbleSystem(float x, float y) {
    this.x = x;
    this.y = y;
    bubs = new ArrayList<Bubble>();
  }
  
  // add a new bubble object every frame
  void createBubbles() {
    bubs.add(new Bubble(x, y, random(-3, 3), random(-10, -5), random(20, 50), color(200, 250, 250)));
  }

  // apply forces and display each bubble in the arraylist
  void moveBubbles() {
    for (int i=bubs.size()-1; i > 0; i--) {
      Bubble bub = bubs.get(i);
      bub.applyForces(random(-0.1, 0.1), random(0.05, 0.1));
      bub.display();
      // if the bubble is dead, remove it
      if (!bub.isAlive()) {
        bubs.remove(i);
      }
    }
    // make bubble disappear gradually when mouse is pressed
    if (mousePressed == true && mouseX > 0 && mouseX < width && mouseY > 200 && mouseY < height) {
      for (int j=bubs.size()-1; j > 0; j--) {
        //bubs.remove(j);
        Bubble bub = bubs.get(j);
        bub.disappear();
      }
      // checks to see if mouse is pressed
      textAlign(CENTER, CENTER);
      fill(100);
      textSize(100);
      text("Popped!", 500, 500);
    }
    //println(bubs.size());
  }
  // Attempt to remove a bubble from array but did not work so changed to arraylist
  int [] removeIndex (int [] bubs, int index) {
    int fin_index = bubs.length - 1;
    int prev = bubs[index];
    bubs[index] = bubs[fin_index];
    bubs[fin_index] = prev;
    bubs = shorten(bubs);
    return bubs;
  }
}
