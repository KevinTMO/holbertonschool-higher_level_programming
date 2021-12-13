#!/usr/bin/node
const argv = require('process').argv;
const firstArgv = argv[2];
const secondArgv = argv[3];

console.log(firstArgv + ' is ' + secondArgv);
