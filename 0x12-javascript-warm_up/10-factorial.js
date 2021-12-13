#!/usr/bin/node
const argv = require('process').argv;

const nmbr = parseInt(argv[2]);

if (isNaN(nmbr)) {
  console.log(1);
} else {
  console.log(factorial(nmbr));
}

function factorial (nmbr) {
  if (nmbr === 0) {
    return (1);
  } else if (nmbr >= 1) {
    return (nmbr * factorial(nmbr - 1));
  }
}
