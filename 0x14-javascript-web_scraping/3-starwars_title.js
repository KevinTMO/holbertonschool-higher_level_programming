#!/usr/bin/node
/*
Print to stdout the title of a Star Wars movie
Process the first argument to be the number of the episode
*/

const rq = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

rq(url, function (err, rqDt, name) {
  if (err) {
    console.error(err);
  } else {
    const movieName = JSON.parse(name).title;
    console.log(movieName);
  }
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
