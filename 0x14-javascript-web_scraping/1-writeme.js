#!/usr/bin/node
/*
Write into a file and process it to utf-8
If there's an error print the error object
then print the data
*/

const fs = require('fs');

const file = process.argv[2];
const data = process.argv[3];

fs.writeFile(file, data, 'utf-8', function (err) {
  if (err) {
    console.error(err);
  }
});

/*

-------- USING FAST FUNCTION PARSING ARGS --------

const fs = require('fs')

const file = process.argv[2]
const data = process.argv[3]

fs.writeFile(file, data, 'utf-8', (err) => {
    if (err) {
        console.error(err);
        return;
    }
});

*/
