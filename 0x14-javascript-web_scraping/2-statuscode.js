#!/usr/bin/node
/*
Display the status code of a GET request
Process the first argument should be the URL
The syntax to output code should be: code: <status code>
*/

const rq = require('request');
const url = process.argv[2];

rq(url, function (err, req) {
  if (err) {
    console.error(err);
    return;
  }
  const resSt = req.statusCode;
  console.log('Code: ' + resSt);
});

/*

------ Fast function way ------

const rq = require('request');
const url = process.argv[2];

rq(url, (err, req) => {
    if (err) {
        console.error(err);
        return;
    }
    resSt = req.statusCode;
    console.log("Code: " + resSt);
})
*/
