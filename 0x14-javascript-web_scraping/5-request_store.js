#!/usr/bin/node
/*
Read/Write a file and process it to utf-8
If there's an error print the error object
Save the data in a file
*/

const fs = require('fs');
const rq = require('request');
const url = process.argv[2];
const file = process.argv[3];

rq(url, function (err, data, content) {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(file, content, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});

/*

-------- USING FAST FUNCTION PARSING ARGS --------

const fs = require('fs');
const rq = require('request');
const url = process.argv[2];
const file = process.argv[3]

rq(url, (err, data, content) => {
    if (err) {
        console.error(err);
        return;
    } else {
        fs.writeFile(file, content, 'utf-8', (err) => {
            if (err) {
                console.error(err);
                return;
            }
        });
    }
});

*/
