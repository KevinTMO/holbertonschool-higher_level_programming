#!/usr/bin/node
const argv = require('process').argv;

if (isNaN(parseInt(argv[2]))) {
  console.log('Not a number');
} else {
  console.log(parseInt(argv[2]));
}

// AnotherWayToDoThis
// if (!parseInt(argv[2])) {
// console.log('Not a Number')
// }
