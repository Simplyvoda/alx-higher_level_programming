#!/usr/bin/node
/*
This script displays the status code of a GET request
*/
const process = require('process');
const request = require('request');

const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
