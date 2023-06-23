float angle = 0.0;
void setup() {
  size(1000, 1000, P3D);
  background(0);
  strokeWeight(2);
  stroke(200);
}

void draw() {
  // create several 3D shapes
  background(0);
  fill(230);
  translate(500, 1000);
  //rotateX(angle/20);
  rotateY(angle/20);
  //rotateZ(30);
  box(500, 500, 500);
  translate(-100, -300);
  fill(100, 0, 0);
  box(100, 500, 100);
  translate(200, -50, 100);
  fill(0, 100, 0);
  sphere(100);
  translate(-200, -250, -100);
  fill(0, 0, 100);
  sphere(150);

  // set up camera to look at these objects
  //camera(500, 100, 1000, 500, 500, 0, 0, 1, 0);

  // experiementing with moving camera based on mouse
  camera(mouseX, mouseY, 1000, 500, 500, 0, 0, 1, 0);

  // experiementing with rotating camera
  //beginCamera();
  //camera(500, 100, 1000, 500, 500, 0, 0, 1, 0);
  //rotateY(angle/20);
  //endCamera();
  angle++;
}
