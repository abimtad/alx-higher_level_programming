#!/usr/bin/node
// This script accepts a file path as an argument and reads
// the contents of the file and prints it to the console.
const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
