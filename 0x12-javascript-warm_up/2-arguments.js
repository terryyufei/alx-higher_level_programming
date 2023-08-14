#!/usr/bin/node

const argumentsCount = process.argv.length - 2;

if (argumentsCount === 0) {
  console.log('No argument');
} else if (argumentsCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
