#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  while (x) {
    function myFunction () {
      theFunction();
    }
    myFunction();
    x--;
  }
};
