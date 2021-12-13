#!/usr/bin/node
const argv = require('process').argv;

let lstNmbr = argv.slice(2);
lstNmbr = lstNmbr.sort();

function sndMaxInt (lstNmbr) {
  if (lstNmbr.length < 2) {
    return 0;
  } else {
    lstNmbr.pop();
    return lstNmbr.pop();
  }
}

console.log(sndMaxInt(lstNmbr));
