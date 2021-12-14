#!/usr/bin/node

exports.converter = function (base) {
  function converter (nmbr) {
    return nmbr.toString(base);
  }
  return converter;
};
