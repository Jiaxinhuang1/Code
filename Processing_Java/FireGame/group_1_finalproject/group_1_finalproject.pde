import processing.sound.*;

int counter = 0;
int currenths= 0;
PrintWriter highscorefile;

int scene = 1;
boolean isPaused = false;
boolean isMuted = false;
boolean played = false;
float volume;
Screens screen;
Goal goal;
Characters fire;
WaterEnemy enemy;
boolean left;
boolean right;
boolean up;
boolean down;
float xPos;
float yPos;
HealthSystem healthsystem;
Level stage;
Scrollbar volumeSlider;
//Sound sound;
SoundFile menuMusic;
SoundFile gameplayMusic;
SoundFile buttonClick;
SoundFile waterSplash;
SoundFile collect;
SoundFile gameLose;

void setup() {
  counter +=1;
  if (counter < 2){
  highscorefile = createWriter("highscore.txt");
  }
  size(1000, 1000);
  screen = new Screens(1000, 1000);
  xPos = 20;
  yPos = 800;
  fire = new Characters(xPos, yPos);
  goal = new Goal(700, 400, 100, 150);
  healthsystem = new HealthSystem(900, 0, 900, 10, 1, 50, 300, 275, 750, 275, 450, 700, 500, 800, 150, 150);
  stage = new Level();
  volumeSlider = new Scrollbar(600, 50, 200, 400);
  volume = volumeSlider.getPos();
  enemy = new WaterEnemy(920, 500, 30, color(77, 166, 255), color(255, 42, 0), color(0, 85, 255), 700, 75);
  //sound = new Sound();
  menuMusic = new SoundFile(this, "menuMusic.mp3");
  gameplayMusic = new SoundFile(this, "gameplayMusic.mp3");
  buttonClick = new SoundFile(this, "buttonClick.mp3");
  waterSplash = new SoundFile(this, "waterSplash.wav");
  collect = new SoundFile(this, "collect.wav");
  gameLose = new SoundFile(this, "gameLose.mp3"); 
  menuMusic.play(1, volume);
 
}

void draw() {
  if (isMuted) {
    menuMusic.stop();
    gameplayMusic.stop();
    buttonClick.stop();
    waterSplash.stop();
    collect.stop();
    gameLose.stop();
  }
  //volume = volumeSlider.getPos();
  //println(volumeSlider.getPos());
  //print(goalIntersect(fire, goal));
  // if the character touches the goal, then go to scene 3 (win game screen)

  if (goalIntersect(fire, goal)) {
    println("start");
    currenths = healthsystem.currentHealth;
    highscorefile.println(currenths);
    highscorefile.flush();
    highscorefile.close();
    String[] lines = loadStrings("highscore.txt");
    println(lines[0]);
    if(currenths > int(lines[0])){
      highscorefile = createWriter("highscore.txt");
      highscorefile.println(currenths);
      highscorefile.flush();
      highscorefile.close();
    }

    println("end");
    scene = 3;
  }

  // isPaused true only if the scene is 5
  if (scene == 5) {
    isPaused = true;
  } else {
    isPaused = false;
  }

  // switching between scenes calls for different functions inside Screens class depending on which scene
  if (scene == 1) {
    screen.menuScreen();
    gameplayMusic.stop();
    if (!menuMusic.isPlaying() && !isMuted)
    {
      menuMusic.loop(1, volume);
    }
  } else if (scene == 2) {
    menuMusic.stop();
    waterSplash.stop();
    if (!gameplayMusic.isPlaying() && !isMuted) {
      gameplayMusic.loop(1, volume);
    }
    screen.gameplayScreen();
    stage.display();
    stage.checkCollision(fire.xPos, fire.yPos); 
    goal.display();
    fire.displayCharacter();
    fire.update();
    enemy.display();
    enemy.movement();
    if (enemy.collision(fire.xPos, fire.yPos) == true) {
      scene = 4;
    }
    healthsystem.display();
    healthsystem.health();
    healthsystem.kill(fire.xPos, fire.yPos);
    healthsystem.fireball(fire.xPos, fire.yPos);
    healthsystem.restoreHealth();
    if (healthsystem.death() == true) {
      scene = 4;
    }
  } else if (scene == 3) {
    waterSplash.stop();
    menuMusic.stop();
    gameplayMusic.stop();
    screen.winScreen();
    // run the setup again if win to restart/reset positions and stats
    setup();
  } else if (scene == 4) {
    menuMusic.stop();
    gameplayMusic.stop();
    screen.loseScreen();
    // run the setup again if lose to restart/reset positions and stats
    setup();
  } else if (scene == 5) {
    screen.pauseScreen();
  } else if (scene == 6) {
    screen.creditScreen();
  } else if (scene == 7) {
    screen.settingScreen();
    volumeSlider.update();
    volumeSlider.display();
  }
}

void keyPressed() {
  // for testing scenes (comment out when finished)
  //if (keyCode == '1') {
  //  scene = 1;
  //}
  //if (keyCode == '2') {
  //  scene = 2;
  //}
  //if (keyCode == '3') {
  //  scene = 3;
  //}
  //if (keyCode == '4') {
  //  scene = 4;
  //}
  if ((key == 'p') && (scene == 2)) {
    scene = 5;
  }
  // test out the credit and settings scene
  if ((keyCode == '6') && (scene == 1)) {
    scene = 6;
  }
  if ((keyCode == '7') && (scene == 1)) {
    scene = 7;
  }

  //key press that controls fire spirte movement
  if (keyCode == ' ' || keyCode == UP || key == 'w') {
    if (!stage.collideAbove) {
      up = true;
    }
  }
  if ((keyCode == LEFT || key == 'a') && !stage.collideOnRight) {
    left = true;
  }
  if ((keyCode == RIGHT || key == 'd')&& !stage.collideOnLeft) {
    right = true;
  }
  if ((keyCode == DOWN || key == 's') && !stage.collideBelow) {
    down = true;
  }
}

// keep sprite moving until key is released
void keyReleased() {
  if (keyCode == ' ' || keyCode == UP || key == 'w') {
    up = false;
  }
  if (keyCode == LEFT || key == 'a') {
    left = false;
  }
  if (keyCode == RIGHT || key == 'd') {
    right = false;
  }
  if (keyCode == DOWN || key == 's') {
    down = false;
  }
}

// checks the intersection between the two rectangle objects
// This can be duplicated to check collision for platforms
// Credit to John McCaffrey's YouTube video on programming platform and jump using processing
boolean goalIntersect(Characters c, Goal g) {
  float distanceX = (c.xPos + c.w/2) - (g.x + g.w/2);
  float distanceY = (c.yPos + c.h/2) - (g.y + g.h/2);
  float comHalfWid = c.w/2 + g.w/2;
  float comHalfHei = c.h/2 + g.h/2;
  if (abs(distanceX) < comHalfWid) {
    if (abs(distanceY) < comHalfHei- 100) {
      return true;
    }
  }
  return false;
}
