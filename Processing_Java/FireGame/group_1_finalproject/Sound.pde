class Sound {
  //SoundFile menuMusic;
  //SoundFile gameplayMusic;
  //SoundFile buttonClick;
  //SoundFile waterSplash;
  //SoundFile collect;
  //SoundFile gameLose;

  Sound() {
    //menuMusic = new SoundFile(sketch, "menuMusic.mp3");
    //gameplayMusic = new SoundFile(sketch, "gameplayMusic.mp3");
    //buttonClick = new SoundFile(sketch, "buttonClick.mp3");
    //waterSplash = new SoundFile(sketch, "waterSplash.mp3");
    //collect = new SoundFile(sketch, "collect.mp3");
    //gameLose = new SoundFile(sketch, "gameLose.mp3");
  }

  void playSound(PApplet sketch, String soundStr, float volume) {
    SoundFile sound = new SoundFile(sketch, soundStr);
    if (!isMuted) {
      if (soundStr == "menuMusic.mp3" || soundStr == "gameplayMusic.mp3") {
        sound.loop(1, volume);
      } else {
        sound.play(1, volume);
      }
    }
  }
  void stopSound(PApplet sketch, String soundStr) {
    SoundFile sound = new SoundFile(sketch, soundStr);
    if (!isMuted) {
      sound.stop();
    }
  }
}
