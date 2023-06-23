// Credit: Miles Berry's Conways Game of Life in Processing YouTube video
// set up the board
int size = 15;
int cols = 1000/size;
int rows = 1000/size;
int [][] board = new int[cols][rows];
{ 
  for (int y = 0; y < rows; y++) {
    for (int x = 0; x < cols; x++) {
      board[x][y] = int(random(2)); // create 0s and 1s only in the board
    }
  }
}

// set up the screen
void setup() {
  size(1000, 1000);
  //frameRate(24);
}

// drawing the screen
void draw() {
  background(0);
  // compute the next
  int [][] next_board = new int[cols][rows];
  // not going to use first and last row/cols
  for (int y = 1; y < rows-1; y++) {
    for (int x = 1; x < cols-1; x++) {
      // call function to count the number of neighbours
      int neighbors = countNeighbors(x, y);
      // apply the game of life rules
      next_board[x][y] = ruleOfLife(board[x][y], neighbors);
    }
  }
  board = next_board;
  drawBoard();
  // make the status opposite (live or die) from current when mouse go through that area
  int cellX = mouseX/size;
  int cellY = mouseY/size;
  // constain values so program dont crash when mouse out of canvas
  cellX = constrain(cellX, 1, cols - 1);
  cellY = constrain(cellY, 1, rows - 1);  
  if (board[cellX][cellY] == 1){
    board[cellX][cellY] = 0;
  }
  else{
    board[cellX][cellY] = 1;
  }
  //board[cellX][cellY] = 1 - board[cellX][cellY];

  //show mouse position
  fill(255);
  ellipse(mouseX, mouseY, 50, 50);
  fill(0);
  rect(0, 0, 1000, 150);
  textAlign(CENTER, CENTER);
  fill(255);
  textSize(40);
  text("Click to Change Board", 500, 59);
  text("Move mouse to change status of Pixel", 500, 100);
}
void mousePressed() {
  board[mouseX / size][mouseY/ size] = 0;
}


// count the number of neighbours (will return an integer)
int countNeighbors (int x, int y) {
  int neighbors = 0;
  //go through the 3x3 grid around current cell
  for (int i = -1; i <= 1; i++) {
    for (int j = -1; j <= 1; j++) {
      neighbors += board[x+j][y+i];
    }
  }
  // take away content of middle cell
  neighbors -= board[x][y];
  return neighbors;
}
//apply the rules of live (will return an integer)
int ruleOfLife(int status, int neighbors) {
  // Any live cell with more than 3 neighbors die
  if (status == 1 && neighbors > 3) {
    return 0;
  } 
  // Any live cell with fewer than two live neighbors die
  else if (status == 1 && neighbors < 2) {
    return 0;
  } 
  // Any dead cell with exactly three live neighbors becomes a live cell
  else if (status == 0 && neighbors == 3) {
    return 1;
  } 
  // Any live cell with two or three live neightbors lives
  else {
    return status;
  }
}

// draw the board on the screen
void drawBoard() {
  for (int y = 0; y < rows; y++) {
    for (int x = 0; x < cols; x++) {
      // if status is alive then color
      if (board[x][y] == 1) {
        fill(random(0, 255), random(0, 255), random(0, 255));
      } else {
        fill(0);
      }
      if (keyPressed)
      {
        if (key == 'q')
        {
          ellipse(x * size + 10, y*size + 10, size + 10, size+ 10);
        }
        if (key == 'w')
        {
          ellipse(x * size + 2, y*size + 2, size + 2, size + 2);
        }
      }
      // draw the pixel
      ellipse(x * size, y*size, size, size);
    }
  }
}

void mouseClicked()
{
  for (int y = 0; y < rows; y++) {
    for (int x = 0; x < cols; x++) {
      board[x][y] = int(random(2)); // create 0s and 1s only in the board
    }
  }
}
