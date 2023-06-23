public class Timer {  //set the timer class
  int startTime;  //create startTime variable
  int interval;  //create the interval variable

  Timer(int timeInterval) {  //create the timer
    interval = timeInterval;  //set interval equal to timeInterval
  }

  void start() {  //create the start function
    startTime = millis();  //set startTime in milliseconds
  }

  boolean complete() {  //check if complete is true or false with boolean
    int elapsedTime = millis()-startTime;  //set elapsedTime equal to the millisecond minus the startTime
    if (elapsedTime>interval) {  //if the elapseTime is greater than the interval
      return true;  //the timer is complete
    } else {  //if the elapseTime is not greater than the interval
      return false;  //the timer is not complete
    }
  }
}
