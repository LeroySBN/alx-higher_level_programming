#!/usr/bin/node
const myStr = 'C is fun';
let count = Number.parseInt(process.argv[2]);

if (!process.argv[2]) {
  console.log('Missing number of occurrences');
} else {
  while (count > 0) {
    console.log(myStr);
    count--;
  }
}
