#!/usr/bin/node
/*
Print to stdout the title of a Star Wars movie
Process the first argument to be the number of the episode
*/

const rq = require('request');
const url = process.argv[2];

rq(url, function (err, rqDt, content) {
  if (err) {
    console.error(err);
    return;
  }
  const lstTsk = JSON.parse(content);

  const dict = {};

  for (const index in lstTsk) {
    if (lstTsk[index].completed) {
      if (dict[lstTsk[index].userId] === undefined) {
        dict[lstTsk[index].userId] = 1;
      } else {
        dict[lstTsk[index].userId]++;
      }
    }
  }
  console.log(dict);
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
