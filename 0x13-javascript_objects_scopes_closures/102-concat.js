#!/usr/bin/node

const argv = require('process').argv;
const fs = require('fs');

const fileA = argv[2];
const fileB = argv[3];
const fileC = argv[4];

const textA = fs.readFileSync(fileA, 'utf8');
const textB = fs.readFileSync(fileB, 'utf8');

fs.writeFileSync(fileC, textA + textB);
