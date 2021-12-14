#!/usr/bin/node

const bsSquare = require('./5-square');

module.exports = class Square extends bsSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let iter = 1; iter <= this.height; iter++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
