#!/usr/bin/node
const argv = require('process').argv;

if (isNaN(parseInt(argv[2]))) {
  console.log('Missing number of ocurrences');
} else if (parseInt(argv[2])) {
  for (let index = 1; index <= parseInt(argv[2]); index++) {
    console.log('C is fun');
  }
}

// AnotherWayToDoThis
// if (!parseInt(argv[2])) {
// console.log('Missing number of ocurrences')
// }
