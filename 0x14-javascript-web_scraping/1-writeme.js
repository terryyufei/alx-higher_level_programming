#!/usr/bin/node

// import the mode
const fs = require('fs');

// The first argument is the file path
const file = process.argv[2];

// The second argument is the string to write
const content = process.argv[3];

// write to file
fs.writeFile(file, content, 'utf-8', error => {
  if (error) {
    console.log(error);
  }
});
