#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super();
    super.width = size;
    super.height = size;
  }
}

module.exports = Square;
