function myFunction(id, timestamp) {
    let x = document.getElementById(id);
    x.currentTime = timestamp*0.001;
    x.play();
  }