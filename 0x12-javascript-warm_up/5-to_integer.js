#!/usr/bin/node

const process = require('process');
const firstArg = process.argv[2];
const convertedFirstArg = parseInt(firstArg);

if (!isNaN(convertedFirstArg)) {
  console.log('My number:', convertedFirstArg);
} else {
  console.log('Not a number');
}
