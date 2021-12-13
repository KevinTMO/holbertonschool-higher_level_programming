#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let index = 1; index <= x; index++) {
    theFunction();
  }
};
