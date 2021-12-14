#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';
    for (let row = 1; row <= this.height; row++) {
      for (let col = 1; col <= this.width; col++) {
        str += 'X';
      }
      if (row < this.height) {
        str += '\n';
      }
    }
    console.log(str);
    str = '';
  }

  rotate () {
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};

/*
 ANOTHER WAY TO DO THIS
  if (w <= 0 && h <= 0) {
    this.width = {};
    this.height = {};
  }
*/
