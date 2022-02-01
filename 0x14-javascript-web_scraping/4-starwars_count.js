#!/usr/bin/node
/*
Print to stdout the title of a Star Wars movie
Process the first argument to be the number of the episode
*/

const rq = require('request');
const url = process.argv[2];

rq(url, function (err, rqDt, name) {
  if (err) {
    console.error(err);
    return;
  }
  const movies = JSON.parse(name).results;

  let count = 0;

  for (let index = 0; index < movies.length; index++) {
    const lst = movies[index].characters;

    for (let jindex = 0; jindex < lst.length; jindex++) {
      if (lst[jindex].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
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
