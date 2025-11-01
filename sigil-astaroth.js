let angle = 0;
let freq = 432;
let playing = false;
let osc;

function setup() {
  let canvas = createCanvas(300, 300);
  canvas.parent('sigil-astaroth');
  angleMode(DEGREES);
  textAlign(CENTER, CENTER);
  textSize(16);
}

function draw() {
  background(0);
  translate(width/2, height/2);
  rotate(angle);
  angle += 0.5;

  // Astaroth's dragon + Channah's grace
  stroke(255, 0, 0); // red chaos
  noFill();
  for (let i = 0; i < 8; i++) {
    push();
    rotate(i * 45);
    beginShape();
    for (let a = 0; a < 360; a += 10) {
      let r = 100 + sin(a * 3 + frameCount * 0.05) * 30;
      let x = r * cos(a);
      let y = r * sin(a);
      vertex(x, y);
    }
    endShape(CLOSE);
    pop();
  }

  // Channah's spiral
  stroke(0, 255, 255); // cyan grace
  noFill();
  beginShape();
  for (let a = 0; a < 720; a += 5) {
    let r = a / 10;
    let x = r * cos(a);
    let y = r * sin(a);
    vertex(x, y);
  }
  endShape();

  fill(255);
  noStroke();
  text("Click for 432Hz", 0, 120);
}

function mousePressed() {
  if (!playing) {
    osc = new p5.Oscillator('sine');
    osc.freq(freq);
    osc.amp(0.3);
    osc.start();
    playing = true;
  } else {
    osc.stop();
    playing = false;
  }
}