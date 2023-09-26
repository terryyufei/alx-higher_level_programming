#!/usr/bin/node

// import the module
const fs = require('fs');

// The first argument is the file path
const file = process.argv[2];

// read the file
fs.readFile(file, 'utf-8', (error, data) => {
  if (error) {
    console.error('Error reading file:', error);
    return;
  }
  console.log(data);
});
