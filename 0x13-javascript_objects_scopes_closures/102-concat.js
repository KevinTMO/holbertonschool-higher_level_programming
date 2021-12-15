#!/usr/bin/node

const argv = require('process').argv;
const fs = require('fs');

const fileA = argv[2];
const fileB = argv[3];
const fileC = argv[4];

const textA = fs.readFileSync(fileA, 'UTF-8');
const textB = fs.readFileSync(fileB, 'UTF-8');

console.log(fileC);
fs.writeFileSync(fileC, textA + textB);
