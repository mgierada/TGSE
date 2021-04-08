function myFunction(id, timestamp) {
  let x = document.getElementById(id);
  let position = timestamp * 0.001;
  if (position <= 0) {
    position = 0
  }
  x.currentTime = position;
  x.play();
  }