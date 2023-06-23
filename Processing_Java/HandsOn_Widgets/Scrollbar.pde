//Credit: Used Scrollbar example from processing.org
class Scrollbar {
  int w, h;
  float xpos, ypos;
  float sliderX, newSliderX;
  float min, max;
  boolean hover;
  boolean locked;
  float ratio;

  Scrollbar(int w, int h, float xpos, float ypos) {
    this.w = w;
    this.h = h;
    this.xpos = xpos;
    this.ypos = ypos - h/2;
    int wtoh = w - h;
    ratio = (float)w / (float)wtoh;
    sliderX = xpos + w/2 - h/2;
    newSliderX = sliderX;
    min = xpos;
    max = xpos + w - h;
  }
  void update() {
    if (overEvent()) {
      hover = true;
    } else {
      hover = false;
    }
    if (mousePressed && hover) {
      locked = true;
    }
    if (!mousePressed) {
      locked = false;
    }
    if (locked) {
      newSliderX = constrain(mouseX-h/2, min, max);
    }
    if (abs(newSliderX - sliderX) > 1) {
      sliderX = sliderX + (newSliderX - sliderX);
    }
  }

  float constrain(float val, float minx, float maxv) {
    return min(max(val, minx), maxv);
  }
  boolean overEvent() {
    if (mouseX > xpos && mouseX < xpos + w && mouseY > ypos && mouseY < ypos +h) {
      return true;
    } else {
      return false;
    }
  }

  void display() {
    noStroke();
    fill(250);
    rect(xpos, ypos, w, h);
    if (hover || locked) {
      fill(0);
    } else {
      fill(102);
    }
    rect(sliderX, ypos, h, h);
  }

  float getPos() {
    return int((sliderX - xpos) / 650 * 255);
  }
}
