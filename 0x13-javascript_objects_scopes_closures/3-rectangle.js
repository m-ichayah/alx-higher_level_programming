#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let holder = '';
    for (let i = 0; i < this.width; i++) holder += 'X';
    for (let i = 0; i < this.height; i++) console.log(holder);
  }
}

module.exports = Rectangle;
