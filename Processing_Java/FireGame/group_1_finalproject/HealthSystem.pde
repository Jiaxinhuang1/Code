class HealthSystem {
  PShape health, healthbar, water, fireball1, fireball2, fireball3;
  int maxHealth, minHealth, currentHealth;
  int fsize, fx1, fy1, fx2, fy2, fx3, fy3;
  int restore, damage;
  boolean isAlive = true;
  boolean fAlive1 = true, fAlive2 = true, fAlive3 = true;
  float xPos, yPos;
  float time = 0, time2 = 0, time3 = 0;
  int waterx, watery, waterWidth, waterHeight;

  HealthSystem(int _maxHealth, int _minHealth, int _currentHealth, int _restore, int _damage, int _fsize, int _fx1, 
    int _fy1, int _fx2, int _fy2, int _fx3, int _fy3, int _waterx, int _watery, int _waterWidth, int _waterHeight) {
    maxHealth = _maxHealth;
    minHealth = _minHealth;
    currentHealth = _currentHealth;
    restore = _restore;
    damage = _damage;
    fsize = _fsize;
    fx1 = _fx1;
    fy1 = _fy1;
    fx2 = _fx2;
    fy2 = _fy2;
    fx3 = _fx3;
    fy3 = _fy3;
    waterx = _waterx;
    watery = _watery;
    waterWidth = _waterWidth;
    waterHeight = _waterHeight;
  }

  void display() {
    //create and display health bar system
    healthbar = createShape(RECT, 20, 20, 910, 40);
    healthbar.setFill(color(140, 140, 140));
    health = createShape(RECT, 20, 20, currentHealth, 30);
    health.setFill(color(0, 204, 102));
    shape(healthbar, 20, 20);
    shape(health, 25, 25);

    textSize(20);
    text("Health:", 85, 20);
  }

  boolean death() {
    //check if player is alive
    if (currentHealth == 0) {
      return true;
    }
    return false;
  }

  void kill(float xPos, float yPos) {
    //creates water
    water = createShape(RECT, waterx, watery, waterWidth, waterHeight);
    water.setFill(color(110, 216, 245));
    shape(water);
    //set health to 0 if touches water
    if (xPos > waterx-50  && xPos < waterx + waterWidth-50 && yPos > watery-150  && yPos < watery + waterHeight) {
      currentHealth = 0;
      print("death");
      gameplayMusic.stop();
      menuMusic.stop();
      if (!waterSplash.isPlaying() && !isMuted) {
        waterSplash.play(1, volume);
      }
    }
  }

  void health() {
    //constantly takes 1 away from player health per second
    if (currentHealth > 0) {
      currentHealth -= .001;
    } else if (currentHealth == 0) {
      currentHealth = 0;
    } else if (currentHealth > maxHealth) {
      currentHealth = maxHealth;
    } else if (currentHealth < minHealth) {
      currentHealth = 0;
    }
  }

  void restoreHealth() {
    //adds 10 health back when player touches fireball
    if (time < 5 && fAlive1 == false) {
      time += 0.1;
    } else if (time >= 4 && fAlive1 == false) {
      fAlive1 = true;
      time = 0;
    }
    if (time2 < 6 && fAlive2 == false) {
      time2 += 0.1;
    } else if (time2 >= 5 && fAlive2 == false) {
      fAlive2 = true;
      time2 = 0;
    }
    if (time3 < 5 && fAlive3 == false) {
      time3 += 0.1;
    } else if (time >= 4 && fAlive3 == false) {
      fAlive3 = true;
      time3 = 0;
    }
  }

  void fireball(float xPos, float yPos) {
    //spawns fireballs after specific amount of time
    fireball1 = createShape(ELLIPSE, fx1, fy1, fsize, fsize);
    fireball2 = createShape(ELLIPSE, fx2, fy2, fsize, fsize);
    fireball3 = createShape(ELLIPSE, fx3, fy3, fsize, fsize);

    fireball1.setFill(color(252, 144, 3));
    fireball2.setFill(color(252, 144, 3));
    fireball3.setFill(color(252, 144, 3));

    //checks to see if fireball is supposed to be spawne
    if (fAlive1 == true) {
      shape(fireball1);
    }
    if (fAlive2 == true) {
      shape(fireball2);
    }
    if (fAlive3 == true) {
      shape(fireball3);
    }

    //println("xPos" + xPos, "yPos" + yPos);

    //checks if player touches the fireball
    if (xPos < fx1 + 20 && xPos > fx1 - 100 && yPos > fy1 - 100 && yPos < fy1 + 30 && fAlive1 == true) {
      if (!collect.isPlaying() && !isMuted)
      {
        collect.play(1, volume);
        println("play");
      }
      if (currentHealth >= maxHealth - 100) {
        currentHealth = maxHealth;
      } else {
        currentHealth += 100;
      }
      fAlive1 = false;
    } else if (xPos < fx2 + 20 && xPos > fx2 - 100 && yPos > fy2 - 100 && yPos < fy2 + 30 && fAlive2 == true) {
      if (!collect.isPlaying() && !isMuted)
      {
        collect.play(1, volume);
        println("play");
      }
      if (currentHealth >= maxHealth - 100) {
        currentHealth = maxHealth;
      } else {
        currentHealth += 100;
      }
      fAlive2 = false;
    } else if (xPos < fx3 + 20 && xPos > fx3 - 100 && yPos > fy3 - 100 && yPos < fy3 + 30 && fAlive3 == true) {
      if (!collect.isPlaying() && !isMuted)
      {
        collect.play(1, volume);
        println("play");
      }
      if (currentHealth >= maxHealth - 100) {
        currentHealth = maxHealth;
      } else {
        currentHealth += 100;
      }
      fAlive3 = false;
    }
  }
}
