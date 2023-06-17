#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
<<<<<<< HEAD
      console.log('X'.repeat(this.width));
=======
      console.log(('X'.repeat(this.width)));
>>>>>>> f2c204d42e56c929512c49df13fe2be6a9deb652
    }
  }

  rotate () {
<<<<<<< HEAD
    let x = 0;
    x = this.width;
    this.width = this.height;
    this.height = x;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
=======
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
};
>>>>>>> f2c204d42e56c929512c49df13fe2be6a9deb652
