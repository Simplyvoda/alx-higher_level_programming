#!/usr/bin/node
/*
prints the title of a Star wars movie where episode
number matched integer
*/
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];

request.get(url + id, function (err, res, body) {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
