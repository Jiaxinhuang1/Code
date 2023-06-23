class Screens {

  int w, h;
  PFont font;
  // creates buttons from Buttons class
  Buttons playButton;
  Buttons restartButton;
  Buttons exitButton;
  Buttons resumeButton;
  Buttons backButton;
  Buttons creditButton;
  Buttons settingButton;
  Buttons quitButton;
  Buttons muteButton;
  Buttons unmuteButton;
  
  Screens(int w, int h) {
    this.w = w;
    this.h = h;
    // use this font
    font = createFont("Gill Sans Ultra Bold", 200);
    textFont(font);
    playButton = new Buttons(w/2 - 250, h - 750, 500, 100, color(150, 100, 100), "Play");
    creditButton = new Buttons(w/2 - 250, h - 625, 500, 100, color(150, 100, 100), "Credits");
    settingButton = new Buttons(w/2 - 250, h - 500, 500, 100, color(150, 100, 100), "Settings");
    quitButton = new Buttons(w/2 - 250, h - 375, 500, 100, color(150, 100, 100), "Quit");
    restartButton = new Buttons(w/2 - 250, h/2 - 150, 500, 150, color(150, 100, 100), "Restart");
    exitButton = new Buttons(w/2 - 250, h/2 + 50, 500, 150, color(150, 100, 100), "Exit");
    resumeButton = new Buttons(w/2 - 250, h/2 - 150, 500, 150, color(150, 100, 100), "Continue");
    backButton = new Buttons(w/2 - 250, h/2 + 225, 500, 100, color(150, 100, 100), "Back");
    muteButton = new Buttons(w/2 - 325, h/2 + 50, 300, 100, color(150, 100, 100), "Mute");
    unmuteButton = new Buttons(w/2, h/2 + 50, 300, 100, color(150, 100, 100), "Unmute");
    
  }

  // creates the menu screen with title and start button
  void menuScreen() {
    background(200, 230, 230);
    noStroke();
    fill (100, 80, 80);
    rect(0, 0, 100, 1000);
    rect(900, 0, 100, 1000);
    fill (150, 80, 80);
    rect(0, 800, 1000, 300);
    fill(0);
    textAlign(CENTER, CENTER);
    textSize(150);
    text("FLAMES", w/2, h - 900);
    playButton.buttonPressed("startGame");
    creditButton.buttonPressed("openCredits");
    settingButton.buttonPressed("openSettings");
    quitButton.buttonPressed("exitGame");
  }

  // creates the gameplay screen with ground
  void gameplayScreen() {
    background(200);
    fill(10);
    rect(0, 950, 1000, 200);
  }

  // creates the lose game screen with restart and exit button
  void loseScreen() {
    background(170, 180, 200);
    textAlign(CENTER, CENTER);
    textSize(150);
    text("YOU LOSE", w/2, h - 800);
    restartButton.buttonPressed("restartGame");
    exitButton.buttonPressed("exitGame");
  } 

  // creates the win screen with restart and exit button
  void winScreen() {
    background(230, 200, 200);
    textAlign(CENTER, CENTER);
    textSize(150);
    text("YOU WIN", w/2, h - 800);
    String[] lines = loadStrings("highscore.txt");
    textSize(100);
    text("HIGHSCORE: "+lines[0], w/2, h - 200);
    restartButton.buttonPressed("restartGame");
    exitButton.buttonPressed("exitGame");
  }

  // creates the pause screen with resume and exit button
  void pauseScreen() {
    int alpha = 10;
    fill(100, 100, 100, constrain(alpha, 10, 10));
    rect(200, 200, 600, 600);
    fill(255);
    textAlign(CENTER, CENTER);
    textSize(65);
    text("GAME PAUSED", w/2, h - 750);
    resumeButton.buttonPressed("resumeGame");
    exitButton.buttonPressed("exitGame");
  }

  void creditScreen() {
    int alpha = 100;
    fill(100, 100, 100, constrain(alpha, 50, 50));
    rect(150, 150, 700, 700);
    fill(255);
    textAlign(CENTER, CENTER);
    textSize(75);
    text("CREDITS", w/2, h - 800);
    textSize(30);
    text("Eric Matyas (soundimage.org)", w/2, h - 725);
    textSize(25);
    text(" - Menu Music", w/2, h - 675);
    text(" - Gameplay Music", w/2, h - 625);
    text(" - Button Click Sound", w/2, h - 575);
    textSize(30);
    text("freesound.org", w/2, h - 500);
    textSize(25);
    text(" - Water Splash by junggle", w/2, h - 450);
    text(" - Collect by Leszek_Szary", w/2, h - 400);
    text(" - Game Lose by yummie", w/2, h - 350);
    backButton.buttonPressed("returnMenu");
  }
  
  void settingScreen(){
    int alpha = 100;
    fill(100, 100, 100, constrain(alpha, 50, 50));
    rect(150, 150, 700, 700);
    fill(255);
    textAlign(CENTER, CENTER);
    textSize(75);
    text("SETTINGS", w/2, h - 800);
    textSize(50);
    text("Volume Slider", w/2, h - 700);
    muteButton.buttonPressed("muteSound");
    unmuteButton.buttonPressed("unmuteSound");
    backButton.buttonPressed("returnMenu");
  }
}
