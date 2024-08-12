#!/usr/bin/node
// Read from file

const fs = require('fs');

const filePath = process.argv[2];

if (!filePath) {
  console.log('Usage: node script.js <file_path>');
  process.exit(1);
}

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  console.log(data);
});
