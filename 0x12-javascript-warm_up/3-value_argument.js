#!/usr/bin/node

// import built-in module "process"
const process = require('process');

const valueArgs = process.argv;
if (valueArgs[2]) {
  console.log(valueArgs[2]);
} else {
  console.log('No argument');
}
