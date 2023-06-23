class Characters {
  float xPos;
  float yPos;
  int numFrames;
  PImage [] fire;
  int animationTimer;
  int animationTimerVal;
  int currentFrame;
  float gravity;
  float speedX, speedY;
  float w, h;
  Level level;

  Characters(float xPos, float yPos) {
    numFrames = 8;
    // load the sprite images
    fire = new PImage[numFrames];
    for (int i = 0; i < fire.length; i++) {
      String imageName = "fire/fire-" + nf(i+1, 1) + ".PNG";
      fire[i] = loadImage(imageName);
    }
    this.xPos = xPos;
    this.yPos = yPos;
    w = 100;
    h = 150;
    animationTimer = 0;
    animationTimerVal = 100;
    currentFrame = 0;
    gravity = 10;
    speedX = 0;
    speedY = 0;
    level = new Level();
  }

  void update() {
    // check to see if public boolean is true 
    // go left if inside canvas and left key if pressed
    if (left) {
      // constrains x position to canvas
      if (xPos > 0) {
        speedX = -5;
      } else {
        speedX = 0;
      }
      if(stage.collideOnRight){
        speedX = 0;
      }
    }
    // go right if inside canvas and right key is pressed
    if (right) {
      
      // constains x position to canvas
      if (xPos < width - 100) {
        speedX = 5;
      } else {
        speedX = 0;
      }
      if(stage.collideOnLeft){
        speedX = 0;
      }
    }
    if (!left && !right) {
      speedX = 0;
    }
    if (!up && !down) {
      speedY = 0;
    }
    // jump up if inside canvas and space is pressed
    if (up) {
      // constrains y position to canvas
      if (yPos > -100) {
        speedY = -5;
      } else {
        speedY = 0;
      }
      if(stage.collideAbove){
        speedY = 0;
      }
    }
    if (down) {
      // constrains y position to canvas
      if (yPos < height-200) {
        speedY = 5;
      } else {
        speedY = 0;
      }
      if(stage.collideBelow){
        speedY = 0;
      }
    } 
  
    // gravity always there unless on ground below 800
    //if (yPos < 800) {
    //  speedY += gravity;
    //}

    xPos += speedX;
    yPos += speedY;
  }

  // show and animate the character
  void displayCharacter() {
    // test collision space
    //rect(xPos, yPos, w, h);
    //int frame = frameCount % numFrames;
    // stop animation when paused
    if (!isPaused) {
      image(fire[currentFrame], xPos - 50, yPos - 100, w + 100, h + 150);
      if ((millis() - animationTimer) >= animationTimerVal) { 
        currentFrame = (currentFrame + 1) % numFrames;
        animationTimer = millis();
      }
    }
  }

  void pauseAnim() {
    isPaused = !isPaused;
  }
}
