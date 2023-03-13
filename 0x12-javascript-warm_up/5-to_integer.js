#!/usr/bin/node

const argv2 = Number.parseInt(process.argv[2]);

if (process.argv[2]) {
  if (Number.isNaN(argv2)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + argv2);
  }
} else if (process.argv[1]) {
  console.log('Not a number');
}
