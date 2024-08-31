#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(1);
const fileName = args[1];

if (!fileName) {
  console.log('Usage: <0-readme.js>  <file name>');
  process.exit(1);
}

fs.readFile(fileName, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }
  console.log(data);
  process.exit(0);
});
