#!/usr/bin/node

const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      let row = '';
      for (let j = 0; j < this.height; j++) {
        row += c;
      }
      console.log(row);
    }
  }
};
