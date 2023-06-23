PFont courier;
String [] fontlist = PFont.list();
final int FONT_SIZE = 32;
String typedText = "";
int charLimit = 30;


void setup() {
  size(1000, 1000);
  background(250);
  printArray(fontlist);
  // create a new font using the embedded default font
  PFont font = createFont("Yu Gothic UI Bold", FONT_SIZE);
  textFont(font);
  //courier = createFont("Courier", FONT_SIZE);
  //textFont(courier);
}

void draw() {
  // set the settings for text
  fill(0);
  textAlign(CENTER);
  textSize(40);
  textLeading(50);
  //text("Hello World", 200, 100);
}

void mousePressed() {
  // clears the text in mouse click
  if (mouseButton == LEFT) {
    typedText = "";
    background(250);
    charLimit = 30;
  }
}

void keyPressed() {
  print(charLimit);
  // Go to a new line if press enter or return
  if ((key == ENTER) || (key == RETURN)) {
    typedText = typedText + "\n";
    background(250);
    text(typedText, 500, 100);
    // resets character limit becuz new line
    charLimit = 30;
  } 
  // string is the substring with last char deleted when press backspace or delete
  else if ((key == BACKSPACE) || (key == DELETE)) {  
    if (typedText.length() > 0) {
      typedText = typedText.substring(0, typedText.length() - 1);
      background(250);
      text(typedText, 500, 100);
      // increase character limit becuz subtract one character
      if (charLimit < 30) {
        charLimit += 1;
      }
    } else {
      return;
    }
  } 
  // if it is not those coded keys, string type will equal to key pressed
  else {
    background(250);
    typedText += String.valueOf(key);
    text(typedText, 500, 100);
    // one less char to type in line
    charLimit -= 1;
    // go to new line if character limit exceeds 30
    if (charLimit <= 0) {
      typedText += "\n";
      charLimit = 30;
    }
  }
}
