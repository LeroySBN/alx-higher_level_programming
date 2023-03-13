#!/usr/bin/node

function add (a, b) {
  return a + b;
}

if (process.argv[3]) {
  let sum = 0;
  sum = add(Number(process.argv[2]), Number(process.argv[3]));
  console.log(sum);
} else {
  console.log(NaN);
}
