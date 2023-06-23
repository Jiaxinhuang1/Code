//Setup
size(1280, 720);
color darkGreen=color(8, 148, 10);
color lightGreen=color(113, 252, 50);
color gray=color(190, 190, 190);
color brown=color(150, 100, 50);
color peach=color(235, 142, 100);
background(lightGreen);

// While loop
int j=0;
while (j<25) {
  int randx=int(random(0, 1280));
  int randy=int(random(0, 720));
  strokeWeight(2);
  stroke(darkGreen);
  line(randx, randy, randx+28, randy-21);
  line(randx+28, randy-21, randx+56, randy);
  line(randx+56, randy, randx+84, randy-21);
  line(randx+84, randy-21, randx+112, randy);
  j++;
}

//Road
stroke(220);
strokeWeight(3);
line(476, 720, 640, 0);
line(764, 720, 640, 0);
fill(gray);
triangle(476, 720, 640, 0, 764, 720);
line(640, 720, 640, 609);
line(640, 546, 640, 441);
line(640, 378, 640, 294);
line(640, 231, 640, 168);
line(640, 126, 640, 105);
line(640, 63, 640, 0);

//Chimmney
stroke(100);
fill(brown);
quad(140, 399, 140, 336, 168, 336, 168, 378);
quad(168, 378, 168, 336, 196, 315, 196, 336);
fill(peach);
quad(140, 336, 168, 315, 196, 315, 168, 336);


//House
stroke(100);
strokeWeight(4);
fill(brown);
triangle(112, 421, 196, 336, 280, 421);
quad(196, 336, 308, 252, 392, 336, 280, 421);
fill(peach);
rect(112, 421, 168, 105);
quad(280, 421, 392, 336, 392, 441, 280, 525);

//Windows,doors,garage
fill(gray);
strokeWeight(3);
quad(308, 421, 392, 357, 392, 441, 308, 504);
strokeWeight(2);
line(308, 441, 392, 378);
line(308, 462, 392, 399);
line(308, 483, 392, 421);
fill(gray);
rect(140, 441, 28, 21);
rect(224, 441, 28, 21);
fill(brown);
rect(168, 483, 56, 42);
line(196, 483, 196, 525);
circle(190, 504, 3);
circle(202, 504, 3);
line(140, 462, 154, 441);
line(154, 441, 168, 462);
line(224, 462, 238, 441);
line(238, 441, 252, 462);

//Trees bark
fill(brown);
rect(476, 336, 28, 63);
rect(532, 189, 28, 42);
rect(560, 84, 28, 21);
rect(868, 567, 56, 63);
rect(784, 357, 28, 42);
rect(756, 210, 28, 21);
rect(704, 126, 20, 21);
rect(364, 168, 28, 21);
rect(1176, 462, 56, 63);
rect(1036, 315, 56, 63);
rect(924, 105, 28, 42);
rect(1110, 84, 20, 21);

//Leaves
fill(darkGreen);
triangle(420, 336, 490, 273, 560, 336);
triangle(420, 315, 490, 252, 560, 315);
triangle(420, 294, 490, 231, 560, 294);
triangle(420, 278, 490, 209, 560, 273);
triangle(504, 189, 546, 147, 588, 189);
triangle(504, 168, 546, 126, 588, 168);
triangle(504, 147, 546, 105, 588, 147);
triangle(532, 84, 574, 42, 616, 84);
triangle(532, 63, 574, 21, 616, 63);
triangle(336, 168, 378, 126, 420, 168);
triangle(336, 147, 378, 105, 420, 147);
triangle(784, 567, 896, 462, 1008, 567);
triangle(784, 546, 896, 441, 1008, 546);
triangle(784, 525, 896, 420, 1008, 525);
triangle(784, 504, 896, 399, 1008, 504);
triangle(784, 483, 896, 378, 1008, 483);
triangle(728, 357, 798, 294, 868, 357);
triangle(728, 336, 798, 273, 868, 336);
triangle(728, 315, 798, 252, 868, 315);
triangle(728, 210, 770, 168, 812, 210);
triangle(728, 189, 770, 147, 812, 189);
triangle(728, 168, 770, 126, 812, 168);
triangle(672, 126, 714, 84, 756, 126);
triangle(672, 105, 714, 63, 756, 105);
triangle(1120, 462, 1204, 378, 1288, 462);
triangle(1120, 441, 1204, 357, 1288, 441);
triangle(1120, 420, 1204, 336, 1288, 420);
triangle(980, 315, 1064, 231, 1148, 315);
triangle(980, 294, 1064, 210, 1148, 294);
triangle(980, 273, 1064, 189, 1148, 273);
triangle(896, 105, 938, 63, 980, 105);
triangle(896, 84, 938, 42, 980, 84);
triangle(896, 63, 938, 21, 980, 63);
triangle(1092, 84, 1120, 42, 1148, 84);
triangle(1092, 63, 1120, 21, 1148, 63);

//Strings and statements
String theHouse="The house of Jiaxin Huang";
println(theHouse);

//Conditionals and random
int a;
a=int(random(3));
println(a);
if (a==1) {
  //Smoke
  fill(gray);
  strokeWeight(2);
  circle(168, 315, 10);
  circle(150, 300, 15);
  circle(162, 330, 8);
  circle(175, 280, 30);
  circle(110, 310, 25);
  circle(112, 230, 35);
  circle(175, 200, 40);
  circle(100, 100, 50);
  circle(150, 150, 20);
  circle(100, 175, 25);
  println("Oh no! The kitchen is burning");
}

if (a==2) {
  fill(gray);
  int k=0;
  while (k<100) {
    int randa=int(random(0, 1280));
    int randb=int(random(0, 720));
    ellipse(randa, randb, 5, 8);
    k++;
  }
  println("IT IS RAINING!");
}
