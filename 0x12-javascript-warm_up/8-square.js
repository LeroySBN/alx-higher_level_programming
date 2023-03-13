#!/usr/bin/node
const myChr = 'X';
let size = Number.parseInt(process.argv[2]);
let sizeh = size;

if (!process.argv[2]) {
  console.log('Missing size');
} else if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  let width = '';
  while (sizeh > 0) {
    while (size > 0) {
      width += myChr;
      size--;
    }
    console.log(width);
    sizeh--;
  }
}
