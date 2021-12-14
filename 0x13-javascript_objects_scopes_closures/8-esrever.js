#!/usr/bin/node

exports.esrever = function (list) {
  let lst = [];

  for (let idx = list.length; idx >= 0; idx--) {
    lst.push(list[idx]);
  }
  lst = lst.slice(1);
  return lst;
};
