Hat hat; //declare a class of hat
Cap cap; //declare a class of cap
Snow[] snows; //declare and array of snow

int numDrops; //create variable to set the number of drops of snow
int score; //create variable to set the score
String s; //create variable to call out score in text

import sprites.utils.*;   //import the sprite library
import sprites.maths.*;
import sprites.*;

import processing.sound.*; //import the soundfile library
SoundFile music;  //create variable soundfile called music 
SoundFile collect;  //create variable soundfile called collect
SoundFile victory;  //create variable soundfile called victory

import interfascia.*;  //import interfascia library

GUIController c;  //set the controller for interfascia
IFButton b1, b2; //create variable b1 and b2
IFLabel l; //create variable l but not used

Sprite title;  //create variable title from sprites library
Sprite flakes;  //create variable flakes from sprites library
Sprite flakes2;  //create variable flakes2 from sprites library
StopWatch sw=new StopWatch();  //create the stopwatch to control the sprites

PImage startScreen;  //create variable to store the start background
PImage gameScreen;  //create variable to store the gaming background
PImage endTitle;  //create variable to store the ending title
PImage santa;  //create variable to store the character santa
PImage snowman;  //create variable to store the character snowman
PImage loseGame;  //create varible to store the losing background

int scene=1;  //create and declare variable scene as the value 1
int sXPos=500; //create and declare variable to set santa position at 500
int smanXPos=500;  //create and declare variable to set snowman position at 500

Timer timer;  //create a class of timer
int timeInterval; //create variable to show the time interval that pass
int activeDrops;  //create varible to show the amount of active drops 

void setup() { //create setup function
  size(1000, 750);  //set the size of the screen and game
  background(200);  //set the background to dark gray

  hat=new Hat(70); //create a class of hat with radius constructor
  cap=new Cap(70);  //create a class of cap with radius constructor

  c = new GUIController (this);   //create the controller for the button
  b1=new IFButton("Start", 350, 525, 300, 50);  //create the b1 in screen with text

  b1.addActionListener(this);  //tell the b1 to detect mouse click

  c.add(b1);  //make the b1 show on screen

  numDrops=100;  //declare the number of drops to be 100
  snows = new Snow[numDrops];  //create an array of snow with 100 snow
  for (int i = 0; i<numDrops; i++) {  //loop through the number of drops
    snows[i] = new Snow();  //create new snowballs
  }

  s = "Score:" + score; //declare variable as scorekeeper

  timeInterval = 1000; //declare the time interval to be 1000
  activeDrops = 0;  //declare the active numver of drops to be 0
  timer = new Timer(timeInterval);  //create a new timer
  timer.start();  //tellls the timer to start

  startScreen = loadImage("title background.jpg");  //upload the google image of title with text added through firealpaca
  gameScreen = loadImage("game background.jpg");  //upload the google image of game background with text added through firealpaca
  endTitle = loadImage("endTitle background.jpg");  //upload the google image of winning background with text added through firealpaca
  loseGame = loadImage("lose game background.jpg");  //upload the google image of losing background with text added through firealpaca
  santa = loadImage("santa.png");  //upload the image drawn by Jiaxin in firealpaca
  snowman = loadImage("snowman.png");  //upload the image drawn by Jiaxin in firealpaca
  title = new Sprite(this, "winter rush1.png", 1, 1, 0); //upload the title sprite create by Jiaxin in firealpaca
  flakes=new Sprite(this, "rotatingflakes.png", 2, 2, 0); //upload the flake sprite drawn by Jiaxin in firealpaca
  flakes2=new Sprite(this, "rotatingflakes.png", 2, 2, 0);  //upload the second flake sprite drawn by Jiaxin in firealpaca

  music=new SoundFile(this, "winterMusic.mp3"); //upload youtube winter music to variable
  music.loop(1, 0.05);  //loop through the music with normal speed and low volume
  collect=new SoundFile(this, "catch.mp3");  //upload sound effect from zapslap website to variable
  victory=new SoundFile(this, "victory.mp3");  //upload sound effect from zapslap website to variable

  title.setXY(width/2, height/2-200); //make the title appear on screen with dimensions shown
  title.setFrameSequence(0, 7, 0.5); //set the speed per frame of the sprite title
  title.setScale(1);  //set the size of the sprite title

  flakes.setXY(350-width/4, 800-height/4); //make the flake appear on screen with dimensions shown
  flakes.setFrameSequence(0, 7, 0.5);  //set the speed per frame of the sprite flake
  flakes.setScale(0.3);  //set the size of the sprite flake

  flakes2.setXY(1100-width/4, 800-height/4);  //make the flake appear on screen with dimensions shown
  flakes2.setFrameSequence(0, 7, 0.5);  //set the speed per frame of the sprite flake
  flakes2.setScale(0.3);  //set the size of the sprite flake

  registerMethod("pre", this);  //set the control to register the sprites
}

void keyPressed() {  //create function whenever the key is pressed
  if (keyCode==BACKSPACE) {  //if backspace is pressed
    scene=1;  //return to scene one
    score=0;  //return score to zero
    c = new GUIController (this);  //set button controller
    b1=new IFButton("Start", 350, 525, 300, 50);  //create the button again

    b1.addActionListener(this);  //make the button detect mouse interaction

    c.add(b1);  //add the button on screen
    music.loop(1, 0.05);  //loop through the music with normal speed and low volume
  }
  if (keyCode=='1') {  //if the 1 key is pressed
    scene=3;  //return the scene to 3
    score=0;  //return the score to 0
  }
  if (keyCode=='0') {  //if the 0 ke is pressed
    scene=4;  //return the scene to 4
    score=0;  //return the score to 0
  }
  if (keyCode==LEFT && scene==3) {  //if the left key is pressed and the scene is also 3
    sXPos=sXPos-30;  //move the santa position 30 units left
  }
  if (keyCode==RIGHT && scene==3) {  //if the right key is pressed and the scene is also 3
    sXPos=sXPos+30;  //move the santa position 30 units right
  }
  if (keyCode==LEFT && scene==4) {  //if the left key is pressed and the scene is also 4
    smanXPos=smanXPos-30;  //move the snowman position 30 units left
  }
  if (keyCode==RIGHT && scene==4) {  //if the left key is pressed and the scene is also 4
    smanXPos=smanXPos+30;  //move the snowman position 30 units right
  }
}

void draw() {  //create draw function

  if (scene==1) {  //if the scene is one
    startGame();  //call the startGame function
  }
  if (scene==2) {  //if the scene is 2
    selectCharacter();  //call the selectCharacter function
  }
  if (scene==3) {  //if the scene is 3
    playGameSanta();  //call the playGameSanta function
    hat.update();  //show the hat surrounding the santa
    hat.display();  //draw the circular hat with no stroke and fill
  }
  if (scene==4) {  //if the scene is 4
    playGameSnowman();  //call the playGameSnowman function
    cap.update();  //show the cap surrounding the snowman
    cap.display();  //draw the circular hat with no stroke and fill
  }
  if (scene==5) {  //if the scene is 5
    endScreen();  //call the endScreen function
    music.stop();  //stop the music
  }

  if (scene==6) {  //if the scene is 6
    music.stop();  //stop the music
    loseGame();  //call the loseGame function
  }
}

public void pre() {  //create pre function
  float elapsedTime = (float) sw.getElapsedTime(); 
  S4P.updateSprites(elapsedTime); //make the sprites appear on screen
}

void actionPerformed (GUIEvent e) { //create function that detects and event with buttons
  if (e.getSource()==b1) {  //if the b1 button is clicked
    scene=2;  //return scene to 2
    c.remove(b1);  //make the b1 button disappear on screen
  }
}

void startGame() {  //create a startGame function
  imageMode(CENTER);  //change the image mode to the center
  image(startScreen, 500, 400);  //make the startScreen image to appear with center in coordinate 500,400
  S4P.drawSprites(); //draw the sprite
}

void selectCharacter() {  //create a selectCharacter function
  imageMode(CENTER);  //change the image mode to center
  image(startScreen, 500, 400);  //make the startScreen image to appear with center in coordinates 500,400
  textAlign(CENTER);  //change the text alignment to center
  textSize(50);  //increase the text size
  fill(0);  //make the text black
  text("Select Character", 500, 100);  //make the text show select character in coordinates 500,100
  textSize(40);  //change the text size to 40
  textAlign(LEFT);  //change the alignment to left
  text("Press 1 for Santa", 150, 200);  //make the text show "" in coordinates 150,200
  textAlign(RIGHT); //change the alignment to right
  text("Press 0 for Snowman", 850, 200);  //make the text show "" in coordinates 850,200
  santa.resize(400, 400);  //resize the santa image
  image(santa, 275, 450);  //draw the santa image in coordinate 275,450
  snowman.resize(500, 500);  //resize the snowman image
  image(snowman, 725, 450);  //draw the snowman image in coordinate 725,450
}

void playGameSanta() {  //create playGameSanta function
  imageMode(CENTER);  //set the image mode ot center
  image(gameScreen, 500, 275);  //make the game screen image appear with center in 500,275
  santa.resize(250, 250);  //resize the santa image to make it smaller
  image(santa, sXPos, 600);  //place santa image on screen with coordinate 500 (declare in variable), 600
  sXPos = constrain(sXPos, 0, 1000);  //prohibits the x value of santa to go outside game screen

  if (timer.complete()==true) {  //tests if the timer complete is true
    if (activeDrops<numDrops) {  //if the active drops is greater than the number of drops
      activeDrops++;  //increase the active drops by 1 each time
    }
    timer.start();  //start the timer to reset
  }

  for (int i=0; i<activeDrops; i++) {  //loop through the number of active drops
    snows[i].display();  //make the snowballs appear onscreen
    snows[i].fall();  //make the snowballs fall down randomly

    if (intersect(hat, snows[i])==true) {  //test if the snowball collides with santa with hat
      snows[i].caught();  //snowball calls the caught function
      collect.play();  //play the collect sound effect everytime collision is detected
      score++;  //increase score by one everytime collision is detected
    }

    if (score==30) {  //if the score equals to 0
      delay(20);  //delay everything my 20 millis
      scene=5;  //return the scene to 5
    }
  }

  textSize(40);  //set text size to 40
  textAlign(LEFT);  //set text alignment to left
  fill(0);  //set text color to black
  s = "Score:" +score;  //declare s string as "" with showing the increasing score
  text(s, 20, 40); //show the score on screen in coordinates 20,40
}

void playGameSnowman() {  //creates playGameSnowman function
  imageMode(CENTER);  //set the image mode to center
  image(gameScreen, 500, 275);  //make the game screen appear with center coordinates
  snowman.resize(250, 250);  //resize the snowman
  image(snowman, smanXPos, 600);  //place the snowman in 500(declared by variable),600
  smanXPos = constrain(smanXPos, 0, 1000); //prohibits the snowman from going beyond the game screen

  if (timer.complete()==true) { //tests if the timer is complete
    if (activeDrops<numDrops) {  //if the active drops is lower than the number of drops
      activeDrops++; //increase the active drops by 1
    }
    timer.start();  //start the timer to reset
  }

  for (int i=0; i<activeDrops; i++) {  //loop through each active drop
    snows[i].display();  //tells snowball to call display function
    snows[i].fall();  //tells snowball to call fall function

    if (intersect(cap, snows[i])==true) {  //detects if the cap and snowball collides
      snows[i].caught();  //tells snowball to call the caught function whenever collision is detected
      collect.play();  //plays the collect sound effect whenever collision is detected
      score++;  //increases the scre by one whenever collision is detected
    }

    if (score==30) {  //if the score is equal to 30
      delay(20);  //delay everything by 20 millis
      scene=5;  //return the scene to 5
    }
  }

  textSize(40);  //set text size to 40
  textAlign(LEFT);  //set text alignmetn to left
  fill(0);  //set text color to black
  s = "Score:" +score;  //set variable as "" with changeing score variable
  text(s, 20, 40);  //make the score appear on scren with coordinate 20,40
}

void endScreen() {  //create endScreen function
  imageMode(CENTER);  //set the image mode to center
  image(endTitle, 500, 400);  //make the end title appear on screen with center in coordinates 500,400
}

void loseGame() {  //create loseGame function
  imageMode(CENTER);  //set the image mode to center
  image(loseGame, 500, 400);  //make the lose game to appear on screen with center in coordinates 500,400
}

boolean intersect(Hat h, Snow s) {  //create boolean to check for collisions between santa and snowball
  float distance = dist(h.x, h.y, s.x, s.y);  //calculates the distance between the center of the circles
  if (distance<h.r+s.r) {  //if the distance is less than the two radiuses combined
    return true;  //the collision is true
  } else {  //if the distance is not less than the two radiuses combined
    return false;  //the collision is false
  }
}

boolean intersect(Cap c, Snow s) {  //create boolean to check for collisions between snowman and snowball
  float distance = dist(c.x, c.y, s.x, s.y);  //calculates the distance between the centers of the circles
  if (distance<c.r+s.r) {  //if the distance is less than the two radiuses combined
    return true;  //the collision is true
  } else {  //if the distance is not less than the two radiuses combined
    return false;  //the collision is false
  }
}
