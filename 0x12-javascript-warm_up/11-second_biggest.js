#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (isNaN(args[2]) || isNaN(args[3])) {
  console.log('0');
} else {
  const array = args.map(Number);
  array.slice(2, args.length);
  array.sort((a, b) => a - b);
  console.log(array[array.length - 2]);
}
