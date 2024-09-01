#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 1) {
  console.log('Usage: 6-completed_tasks.js <URL>');
  process.exit(1);
}

const URL = args[0];

const request = require('request');

request(URL, (err, _, body) => {
  if (err) {
    process.exit(1);
  }

  const response = JSON.parse(body);

  const result = {};

  for (const task of response) {
    if (!task.completed) continue;

    if (!(task.userId in result)) {
      result[task.userId] = 1;
    } else {
      result[task.userId] += 1;
    }
  }

  console.log(result);
  process.exit(0);
});
