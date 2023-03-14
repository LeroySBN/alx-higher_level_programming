#!/usr/bin/node

/* class square that inherits from rectangle */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    let myChar;
    if (c) {
      myChar = c;
    } else {
      myChar = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      let row = '';
      for (let j = 0; j < this.size; j++) row += myChar;
      console.log(row);
    }
  }
}

module.exports = Square;
