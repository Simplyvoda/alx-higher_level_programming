#!/usr/bin/node
/*
This script writes a string to a file
First argument is file path
Second argument is string to write in fie
*/
const fs = require('fs');
const process = require('process');

fs.writeFile(process.argv[2], process.argv[3], 'utf8', err => {
  if (err) {
    console.error(err);
  }
});
