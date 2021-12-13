#!/usr/bin/node
const argv = require('process').argv;
const firstArgv = argv[2];

if (argv.length < 3) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log(firstArgv);
}
