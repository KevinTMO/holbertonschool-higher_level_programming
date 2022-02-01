#!/usr/bin/node
/*
Read a file and process it to utf-8
If there's an error print the error object
then print the data
*/

const fs = require('fs')

const arg = process.argv[2]


fs.readFile(arg, 'utf-8', function(err, data) {
    if (err) {
	console.error(err);
	return;
    }
    console.log(data);
});

/*

-------- USING FAST FUNCTION PARSING ARGS --------

const fs = require('fs')

const arg = process.argv[2]


fs.readFile(arg, 'utf-8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});

*/
