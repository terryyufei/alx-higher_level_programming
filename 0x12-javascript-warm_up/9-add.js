#!/usr/bin/node

const process = require('process');
const firstArg = parseInt(process.argv[2]);
const secondArg = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(firstArg, secondArg));
